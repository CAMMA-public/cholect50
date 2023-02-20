#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CODE RELEASE TO SUPPORT RESEARCH.
COMMERCIAL USE IS NOT PERMITTED.
#==============================================================================
An implementation based on:
***
    C.I. Nwoye, T. Yu, C. Gonzalez, B. Seeliger, P. Mascagni, D. Mutter, J. Marescaux, N. Padoy. 
    Rendezvous: Attention Mechanisms for the Recognition of Surgical Action Triplets in Endoscopic Videos. 
    Medical Image Analysis, 78 (2022) 102433.
***  
Created on Thu Oct 21 15:38:36 2021
#==============================================================================  
Copyright 2021 The Research Group CAMMA Authors All Rights Reserved.
(c) Research Group CAMMA, University of Strasbourg, France
@ Laboratory: CAMMA - ICube
@ Author: Chinedu Innocent Nwoye
@ Website: http://camma.u-strasbg.fr
#==============================================================================
 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
     http://www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
#==============================================================================
"""

import os
import random
import numpy as np
from PIL import Image
import tensorflow as tf


class CholecT50():
    def __init__(self, 
                dataset_dir, 
                dataset_variant="cholect45-crossval",
                test_fold=1,
                augmentation_list=['original', 'vflip', 'hflip', 'contrast', 'rot90'],
                normalize=True,
                num_parallel_calls=8):
        """ Args
                dataset_dir : common path to the dataset (excluding videos, output)
                list_video  : list video IDs, e.g:  ['VID01', 'VID02']
                aug         : data augumentation style
                split       : data split ['train', 'val', 'test']
            Call
                batch_size: int, 
                shuffle: True or False
            Return
                tuple ((image), (tool_label, verb_label, target_label, triplet_label))
        """
        self.normalize   = normalize
        self.dataset_dir = dataset_dir
        self.list_dataset_variant = {
            "cholect45-crossval": "for CholecT45 dataset variant with the official cross-validation splits.",
            "cholect50-crossval": "for CholecT50 dataset variant with the official cross-validation splits",
            "cholect50-challenge": "for CholecT50 dataset variant as used in CholecTriplet challenge",
            "cholect50": "for the CholecT50 dataset with original splits used in rendezvous paper",
            "cholect45": "a pointer to cholect45-crossval",
        }
        assert dataset_variant in self.list_dataset_variant.keys(), print(dataset_variant, "is not a valid dataset variant")
        video_split  = self.split_selector(case=dataset_variant)
        train_videos = sum([v for k,v in video_split.items() if k!=test_fold], []) if 'crossval' in dataset_variant else video_split['train']
        test_videos  = sum([v for k,v in video_split.items() if k==test_fold], []) if 'crossval' in dataset_variant else video_split['test']
        if 'crossval' in dataset_variant:
            val_videos   = train_videos[-5:]
            train_videos = train_videos[:-5]
        else:
            val_videos   = video_split['val']
        self.train_records = ['VID{}'.format(str(v).zfill(2)) for v in train_videos]
        self.val_records   = ['VID{}'.format(str(v).zfill(2)) for v in val_videos]
        self.test_records  = ['VID{}'.format(str(v).zfill(2)) for v in test_videos]
        self.augmentation_list  = augmentation_list
        self.num_parallel_calls = self.get_num_parallel(num_parallel_calls)
        self.build_train_dataset()
        self.build_val_dataset()
        self.build_test_dataset()

    def split_selector(self, case='cholect50'):
        switcher = {
            'cholect50': {
                'train': [1, 15, 26, 40, 52, 65, 79, 2, 18, 27, 43, 56, 66, 92, 4, 22, 31, 47, 57, 68, 96, 5, 23, 35, 48, 60, 70, 103, 13, 25, 36, 49, 62, 75, 110],
                'val'  : [8, 12, 29, 50, 78],
                'test' : [6, 51, 10, 73, 14, 74, 32, 80, 42, 111]
            },
            'cholect50-challenge': {
                'train': [1, 15, 26, 40, 52, 79, 2, 27, 43, 56, 66, 4, 22, 31, 47, 57, 68, 23, 35, 48, 60, 70, 13, 25, 49, 62, 75, 8, 12, 29, 50, 78, 6, 51, 10, 73, 14, 32, 80, 42],
                'val':   [5, 18, 36, 65, 74],
                'test':  [92, 96, 103, 110, 111]
            },
            'cholect45-crossval': {
                1: [79,  2, 51,  6, 25, 14, 66, 23, 50,],
                2: [80, 32,  5, 15, 40, 47, 26, 48, 70,],
                3: [31, 57, 36, 18, 52, 68, 10,  8, 73,],
                4: [42, 29, 60, 27, 65, 75, 22, 49, 12,],
                5: [78, 43, 62, 35, 74,  1, 56,  4, 13,],
            },
            'cholect50-crossval': {
                1: [79,  2, 51,  6, 25, 14, 66, 23, 50, 111],
                2: [80, 32,  5, 15, 40, 47, 26, 48, 70,  96],
                3: [31, 57, 36, 18, 52, 68, 10,  8, 73, 103],
                4: [42, 29, 60, 27, 65, 75, 22, 49, 12, 110],
                5: [78, 43, 62, 35, 74,  1, 56,  4, 13,  92],
            },
        }
        return switcher.get(case)
            
    def augmentation(self, img, label):
        self.switcher_img = {                
                'original'   :  img,
                'scaling'    :  self.scale(img),
                'vflip'      :  tf.image.random_flip_up_down(img),
                'hflip'      :  tf.image.random_flip_left_right(img),
                'transpose'  :  self.transpose(img),
                'rot90'      :  tf.image.rot90(img, k = 1), 
                'brightness' :  tf.image.random_brightness(img, 0.5),
                'contrast'   :  tf.image.random_contrast(img, 0.3, 0.5),
            }
        for case in self.augmentation_list:
            img = self.switcher_img.get(case, img)
        img = self.resize(img)
        return img, label

    def scale(self, img):
        try:
            rate    = tf.random.uniform(shape=[2], minval=0.5, maxval=2.0, dtype=tf.float32, name='resize_rate')
            r_shape = tf.cast(tf.cast(tf.shape(img)[1:3],tf.float32) * rate, tf.int32)
            return tf.image.resize_with_crop_or_pad(img, r_shape[0], r_shape[1])
        except:
            rate     = tf.random_uniform(shape=[2], minval=0.5, maxval=2.0, dtype=tf.float32, name='resize_rate') 
            r_shape = tf.cast(tf.cast(tf.shape(img)[1:3],tf.float32) * rate, tf.int32)
            return tf.image.resize_image_with_crop_or_pad(img, r_shape[0], r_shape[1])

    def transpose(self, img):
        try:
            return tf.image.transpose(img)
        except:
            return tf.image.transpose_image(img)

    def resize(self, img):
        try:
            return tf.image.resize(images=img, size=[256, 448])
        except:
            return tf.image.resize_images(images=img, size=[256, 448])

    def get_num_parallel(self, n):
        try:
            return tf.data.experimental.AUTOTUNE
        except:
            return n    

    def list_augmentations(self):
        print(self.switcher_img.keys())

    def list_dataset_variants(self):
        print(self.list_dataset_variant)

    def generator(self, records):
        for record in records:
            video_path      = os.path.join(self.dataset_dir, "data/{}".format(record.decode("utf-8")))
            triplet_file    = np.loadtxt(os.path.join(self.dataset_dir, "triplet/{}.txt".format(record.decode("utf-8"))), dtype=np.int, delimiter=',',)
            tool_file       = np.loadtxt(os.path.join(self.dataset_dir, "instrument/{}.txt".format(record.decode("utf-8") )), dtype=np.int, delimiter=',',)
            verb_file       = np.loadtxt(os.path.join(self.dataset_dir, "verb/{}.txt".format(record.decode("utf-8") )), dtype=np.int, delimiter=',',)
            target_file     = np.loadtxt(os.path.join(self.dataset_dir, "target/{}.txt".format(record.decode("utf-8") )), dtype=np.int, delimiter=',',)
            for i,v,t,ivt in zip(tool_file, verb_file, target_file, triplet_file):
                assert i[0]==v[0]==t[0]==ivt[0]
                image_path  = os.path.join(video_path, "{}.png".format(str(ivt[0]).zfill(6)))
                image       = Image.open(image_path)
                image       = image.resize(size=(448,256))
                yield image, (i[1:], v[1:], t[1:], ivt[1:])               

    def build_train_dataset(self):
        self.train_dataset = tf.data.Dataset.from_generator(
                self.generator,
                args = [self.train_records],
                output_types = (tf.float32, (tf.int32, tf.int32, tf.int32, tf.int32)),
                output_shapes = ([256, 448,3], ([6], [10], [15], [100]))
            )
        self.train_dataset = self.train_dataset.map(self.augmentation, num_parallel_calls=self.num_parallel_calls)           

    def build_val_dataset(self):
        self.val_dataset = tf.data.Dataset.from_generator(
                self.generator,
                args = [self.val_records],
                output_types = (tf.float32, (tf.int32, tf.int32, tf.int32, tf.int32)),
                output_shapes = ([256, 448,3], ([6], [10], [15], [100]))
            )
        self.val_dataset = self.val_dataset.map(self.augmentation, num_parallel_calls=self.num_parallel_calls)   

    def build_test_dataset(self):
        self.test_dataset = []
        for video in self.test_records:
            test_dataset = tf.data.Dataset.from_generator(
                self.generator,
                args = [[video]],
                output_types = (tf.float32, (tf.int32, tf.int32, tf.int32, tf.int32)),
                output_shapes = ([256, 448,3], ([6], [10], [15], [100]))
            )
            self.test_dataset.append(test_dataset)

    def build(self):
        return (self.train_dataset, self.val_dataset, self.test_dataset)


if __name__ == "__main__":
    print("Refers to https://github.com/CAMMA-public/cholect45 for the usage guide.")