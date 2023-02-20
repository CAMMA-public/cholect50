<div align="center">
<a href="http://camma.u-strasbg.fr/">
<img src="../files/logo_cholect50.gif" width="100%">
</a>
</div>

------------------------------------------------------

<div align="right"><a href="../README.md" id="links">Home</a> &nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp; 
<a href="README-Format.md" id="links">Data format</a> &nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp; 
<a href="README-Splits.md" id="links">Data splits</a>  &nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp; 
<a href="README-Downloads.md" id="links">Downloads</a>  &nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp; 
<a href="README-Challenges.md" id="links">Challenges</a>  &nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;  
<a href="README-Leaderboards.md" id="links">Leaderboards</a> </div>

------------------------------------------------------
<br>


Data Loader
================================================
We provide data loader for the following frameworks:

- PyTorch :  [`dataloader_pth.py`](dataloader_pth.py)
- TensorFlow v1 & v2 :  [`dataloader_tf.py`](dataloader_tf.py)
- . . .

  >>> Pull request for other framework is highly welcome.

... *if you use any part of this code, you are kindly requested to cite the CholecT50 dataset [[1]](#cite-cholect50)  in order to properly credit the authors and clinicians for their efforts in generating the dataset.*

<br> 

>## Requirements
- pillow
- torch & torchvision `for pyTorch users`
- tensorflow `for TensorFlow users`


<br> 

>## Usage
<details>
  <summary> <b>Code</b>: <font color="orange"> import libraries: </font> </summary>

  ``` python
  import ivtmetrics # install using: pip install ivtmetrics

  # for PyTorch
  import dataloader_pth as dataloader
  from torch.utils.data import DataLoader

  # for TensorFlow v1 & v2
  import tensorflow as tf
  import dataloader_tf as dataloader
  ```

</details>

<br>

<details>
  <summary> <b>Code</b>: <font color="orange"> initialize the metrics library:</font> </summary>

  ``` python    
  metrics = ivtmetrics.Recognition(num_class=100)
  ```

</details>


<br>

<details>
  <summary> <b>Code</b>: <font color="orange"> build dataset pipeline:</font> </summary>    

  Loading the cholect45 cross-validation variant with test set as fold 1 as follows:

  ```python
  # initialize dataset: 
  dataset = dataloader.CholecT50( 
            dataset_dir="/path/to/your/downloaded/dataset/cholect45/", 
            dataset_variant="cholect45-crossval",
            test_fold=1,
            augmentation_list=['original', 'vflip', 'hflip', 'contrast', 'rot90'],
            )

  # build dataset
  train_dataset, val_dataset, test_dataset = dataset.build()
  ```

  List of currently supported data augumentations:
  - use `dataset.list_augmentations()` to see the full list.
  - use `dataset.list_dataset_variants()` to see all the supported dataset variants

</details>

<br>


<details>
  <summary> <b>Code</b>: <font color="orange"> wrap as default data loader:</font> </summary>

 - *PyTorch :*


 ```python
# train and val data loaders
train_dataloader = DataLoader(train_dataset, batch_size=32, shuffle=True, prefetch_factor=3,)
val_dataloader   = DataLoader(val_dataset, batch_size=32, shuffle=True)

# test data set is built per video, so load differently
test_dataloaders = []
for video_dataset in test_dataset:
  test_dataloader = DataLoader(video_dataset, batch_size=32, shuffle=False)
  test_dataloaders.append(test_dataloader)
``` 

 - *TensorFlow v2 :*

```python
# train and val data loaders
train_dataloader = train_dataset.shuffle(20).batch(32).prefetch(5) # see tf.data.Dataset for more options
val_dataloader   = val_dataset.batch(32)

# test data set is built per video, so load differently
test_dataloaders = []
for video_dataset in test_dataset:
  test_dataloader = video_dataset.batch(32).prefetch(5)
  test_dataloaders.append(test_dataloader)
``` 

- *TensorFlow v1 :*

```python
# construct an iterator and train data loaders
train_dataset = train_dataset.shuffle(20).batch(32).prefetch(5) # see tf.data.Dataset for more options
iterator      = tf.data.Iterator.from_structure(output_types=train_dataset.output_types, output_shapes=train_dataset.output_shapes) 
init_train    = iterator.make_initializer(train_dataset) 

# using the same iterator, construct val data loaders
val_dataset = val_dataset.batch(32)
init_val    = iterator.make_initializer(val_dataset) 

# test data set is built per video, so load differently with the same iterator
init_tests = []
for video_dataset in test_dataset:
  video_dataset = video_dataset.batch(32)
  init          = iterator.make_initializer(video_dataset) 
  init_tests.append(init)

# outputs from iterator
tf_img, (tf_label_i, tf_label_v, tf_label_t, tf_label_ivt) = iterator.get_next()
```
</details>

<br>


<details>
  <summary> <b>Code</b>: <font color="orange"> reading the dataset during experiment:</font> </summary>

- *PyTorch and TensorFlow v2 :*

```python
total_epochs = 10
model = YourFantasticModel(...)
for epoch in range(total_epochs):
  # training
  for batch, (img, (label_i, label_v, label_t, label_ivt)) in enumerate(train_dataloader):
    pred_ivt = model(img)
    loss(label_ivt, pred_ivt)
      
  # validate
  for batch, (img, (label_i, label_v, label_t, label_ivt)) in enumerate(val_dataloader):
    pred_ivt = model(img)

# testing: test per video
for test_dataloader in test_dataloaders:
  for batch, (img, (label_i, label_v, label_t, label_ivt)) in enumerate(test_dataloader):
    pred_ivt = model(img)
    metrics.update(label_ivt, pred_ivt)
  metrics.video_end() # important for video-wise AP
```


- *TensorFlow v1 :*

```python
total_epochs = 10
model = YourFantasticModel(...)

with tf.Session() as sess:
  sess.run(tf.global_variables_initializer())

  for epoch in range(total_epochs):
    # training
    sess.run([tf.local_variables_initializer(), init_train])
    while True:
      try:
        img, label_i, label_v, label_t, label_ivt = \
          sess.run([tf_img, tf_label_i, tf_label_v, tf_label_t, tf_label_ivt])
        pred_ivt = model(img)
        loss(label_ivt, pred_ivt)
      except tf.errors.OutOfRangeError: 
        # do what ever you want after an epoch train here  
        break      

    # validate
    sess.run([tf.local_variables_initializer(), init_val])
    while True:
      try:
        img, label_i, label_v, label_t, label_ivt = \
          sess.run([tf_img, tf_label_i, tf_label_v, tf_label_t, tf_label_ivt])
        pred_ivt = model(img)
        loss(label_ivt, pred_ivt)
      except tf.errors.OutOfRangeError: 
        # do what ever you want after an epoch val here
        break  

  # testing: test per video  
  for init_test in init_tests:
    sess.run([tf.local_variables_initializer(), init_test])
    while True:
      try:
        img, label_i, label_v, label_t, label_ivt = \
          sess.run([tf_img, tf_label_i, tf_label_v, tf_label_t, tf_label_ivt])
        pred_ivt = model(img)
        metrics.update(label_ivt, pred_ivt)
      except tf.errors.OutOfRangeError:
        metrics.video_end() # important for video-wise AP
        break    
```
</details>

<br>

<details>
  <summary> <b>Code</b>: <font color="orange"> obtain results:</font> </summary>


```python
AP_i    = metrics.compute_video_AP("i")["AP"]
mAP_it  = metrics.compute_video_AP("it")["mAP"]
mAP_ivt = metrics.compute_video_AP("ivt")["mAP"]
```
</details>

<br> 

- For TensorFlow, we recommend the use of [TFRecord](https://www.tensorflow.org/tutorials/load_data/tfrecord) for high-speed data loading.
- See [ivtmetrics](https://github.com/CAMMA-public/ivtmetrics) github for more details on metrics usage.

<br>



------------------------------------------------
References
================================================
<div id="cite-cholect50">

* **[1]** C.I. Nwoye, T. Yu, C. Gonzalez, P. Mascagni, D. Mutter, J. Marescaux, N. Padoy. Recognition of instrument-tissue interactions in endoscopic videos via action triplets.International Conference on Medical Image Computing and Computer-Assisted Intervention (MICCAI) 2020.
  ```
  @inproceedings{nwoye2020recognition,
     title={Recognition of instrument-tissue interactions in endoscopic videos via action triplets},
     author={Nwoye, Chinedu Innocent and Gonzalez, Cristians and Yu, Tong and Mascagni, Pietro and Mutter, Didier and Marescaux, Jacques and Padoy, Nicolas},
     booktitle={International Conference on Medical Image Computing and Computer-Assisted Intervention (MICCAI)},
     pages={364--374},
     year={2020},
     organization={Springer}
  }
  ```
  <div align="right">

   [![Read on ArXiv](https://img.shields.io/badge/arxiv-2109.03223-red)](https://arxiv.org/abs/2109.03223) 
  </div>
  <br>
</div>

* **[2]** C.I. Nwoye, T. Yu, C. Gonzalez, B. Seeliger, P. Mascagni, D. Mutter, J. Marescaux, N. Padoy. Rendezvous: Attention Mechanisms for the Recognition of Surgical Action Triplets in Endoscopic Videos. Medical Image Analysis 2022.
  ```
  @article{nwoye2021rendezvous,
    title={Rendezvous: Attention Mechanisms for the Recognition of Surgical Action Triplets in Endoscopic Videos},
    author={Nwoye, Chinedu Innocent and Yu, Tong and Gonzalez, Cristians and Seeliger, Barbara and Mascagni, Pietro and Mutter, Didier and Marescaux, Jacques and Padoy, Nicolas},
    journal={Medical Image Analysis},
    volume={78},
    pages={102433},
    year={2022}
  }
  ```
  <div align="right">

   [![ArXiv paper](https://img.shields.io/badge/arxiv-2007.05405-red)](https://arxiv.org/abs/2007.05405)
  </div>
  <br>
---