<div align="center">
<a href="http://camma.u-strasbg.fr/">
<img src="../files/logo_cholect50.gif" width="100%">
</a>
</div>

------------------------------------------------------

<div align="right"><a href="../README.md" id="links">Home</a> &nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;
<a href="README-Splits.md" id="links">Data splits</a>  &nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp; 
<a href="README-Downloads.md" id="links">Downloads</a>  &nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp; 
<a href="README-Loader.md" id="links">Data loader</a>  &nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp; 
<a href="README-Challenges.md" id="links">Challenges</a>  &nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;  
<a href="README-Leaderboards.md" id="links">Leaderboards</a> </div>

------------------------------------------------------
<br>


Data Format
============

## Contents
The CholecT50 dataset folder includes:
  - **videos**/: 50 cholecystectomy videos
  - **labels**/: triplet annotations on 50 videos
  - a **label mapping** text file
  - a **LICENCE** file
  - a **README** file

<br>

<details>
  <summary>  
  <b>Expand to view the dataset directory structure: </b>
  </summary>
  
  ```
    ──CholecT50
        ├───videos
        │   ├───VID01
        │   │   ├───000000.png
        │   │   ├───000001.png
        │   │   ├───000002.png
        │   │   ├───
        │   │   └───N.png
        │   ├───VID02
        │   │   ├───000000.png
        │   │   ├───000001.png
        │   │   ├───000002.png
        │   │   ├───
        │   │   └───N.png
        │   ├───
        │   └───VIDN
        │       ├───000000.png
        │       ├───000001.png
        │       ├───000002.png
        │       ├───
        │       └───N.png
        |
        ├───labels
        │   ├───VID01.json
        │   ├───VID02.json
        │   ├───VID03.json
        │   ├───
        │   └───VIDNN.json
        |
        ├───label_mapping.txt        
        ├───LICENSE
        └───README.md
   ```
</details>

<br>

------------------------------------------------
Videos and Images
================================================

This contains the surgical videos. Each video directory contains unequal `N` image frames extracted sequentially from the video at 1 FPS. The pixel resolution is 854x480x3. 
The filenames are sequentially numbered as imageID.png. 
The filenames are the imageIDs padded with leading zeros upto `6` digits, hence, `000001`.png==`1`, `000023`.png==`23`, `021563`.png==`21563`, etc.

To ensure anonymity, frames corresponding to out-of-body views are entirely blacked (RGB `0 0 0`) out.

<br>

------------------------------------------------
Labels
================================================

The `labels` directory contains a JSON file per video which contains labels for triplets, instruments, verbs, targets, and phase per frame.


<details>
  <summary>  
  <b>Expand to view the structure of the JSON file: </b>
  </summary>
    <pre>
      ──VIDX.json
          ├───<b>video: <o>(int)</o></b> - <g><i>video ID.</i></g>
          ├───<b>fps: <o>(int)</o></b> - <g><i>frame rate (usually 1).</i></g>
          ├───<b>num_frames: <o>(int)</o></b> - <g><i>number of sampled frames.</i></g>
          ├───<b>categories: <o>list[]</o></b> - <g><i>containing category dictionary per task.</i></g>
          │   ├───<b>triplet: <o>dict()</o></b> - <g><i>ID to triplet categories.</i></g>
          │   ├───<b>instrument: <o>dict()</o> </b>- <g><i>ID to instrument categories</i></g>
          │   ├───<b>verb: <o>dict()</o> </b>- <g><i>ID to verb categories.</i></g>
          │   ├───<b>target: <o>dict()</o> </b>- <g><i>ID to target categories.</i></g>
          │   └───<b>phase: <o>dict()</o> </b>- <g><i>ID to phase categories.</i></g>
          |
          ├───<b>annotations: <o>dict()</o> </b> <g><i>mapping frame ID to frame annotations:</i></g>
          │   ├───<b>0: <o>list[]</o> </b> - <g><i>triplet instance variables in frame 0.</i></g>
          │   ├───<b>1: <o>list[]</o> </b> - <g><i>triplet instance variables in frame 1.</i></g>
          │   ├───<b>2: <o>list[]</o> </b> - <g><i>triplet instance variables in frame 2.</i></g>
          │   ├─── . . .
          │   └───<b>N: <o>list[]</o> </b> - <g><i>triplet instance variables in frame N.</i></g>
          |
          ├───<b>info: <o>text</o></b> - <g><i> dataset description: name, date, version, bbox format, copyright, etc.</i></g>
          └───<b>licenses: <o>text</o></b> - <g><i>license info including the ID, name and url.</i></g>
    </pre>
</details>

<br>

## Annotation format
There can be zero, one, or multiple triplet instances per frame. 
Here, a frame ID is mapped to a list of all triplet instances in the frame.
Each *triplet instance* is a vector of 15 items describing the triplet, instrument, verb, target, and phase informaton for that instance example. The vector values can vary across triplet instances, however, the phase label is unchanged within a frame.


<img src="../files/var.png" width="95%">

Keys:
- **ID**: <font color="orange">(int)</font> category identity
- **SC**: <font color="orange">(float)</font> confidence score : `1` for groundtruths, probability `[0...1]` for predictions
- **BX**: <font color="orange">(float)</font> bounding box x1 cordinate (left), scaled by the image width
- **BY**: <font color="orange">(float)</font> bounding box y1 cordinate (top), scaled by the image height
- **BW**: <font color="orange">(float)</font> bounding box width, scaled by the image width
- **BH**: <font color="orange">(float)</font> bounding box height, scaled by the image height
Value is `-1` for null or absence.

<br>


------------------------------------------------
Label Mapping
================================================

The `label_mapping.txt` file contains a table, consisting of 6 columns for mapping triplet IDs to their component IDs.
This is useful for decomposing a triplet to its constituting components.
The first column indicates the triplet ID (that is instrument-verb-target paring IDs).
The second column indicates the instrument ID.
The third column indicates the verb IDs.
The fourth column indicates the target IDs.
The fifth column indicates the instrument-verb pairing IDs.
The sixth column indicates the instrument-target pairing IDs.

### Example usage: 

The first row in the maps.txt shows:
`1,0,2,0,2,0`
This means that triplet iD `1` can be mapped to `<0, 2, 0>` which is `{grasper, dissect, gallbladder}`.
<br>

