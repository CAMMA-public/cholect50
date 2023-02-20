
<div align="center">
<a href="http://camma.u-strasbg.fr/">
<img src="../files/logo_cholect50.gif" width="100%">
</a>
</div>

------------------------------------------------------

<div align="right"><a href="../README.md" id="links">Home</a> &nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp; 
<a href="README-Format.md" id="links">Data format</a> &nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp; 
<a href="README-Splits.md" id="links">Data splits</a>  &nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp; 
<a href="README-Loader.md" id="links">Data loader</a>  &nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp; 
<a href="README-Challenges.md" id="links">Challenges</a>  &nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;  
<a href="README-Leaderboards.md" id="links">Leaderboards</a> </div>

------------------------------------------------------
<br>


Downloads
================================================
This dataset is publicly released under the Creative Commons licence [CC-BY-NC-SA 4.0](../LICENSE). This implies that:

- the dataset cannot be used for commercial purposes,
- the dataset can be transformed (additional annotations, etc.),
- the dataset can be redistributed as long as it is redistributed under - the same license with the obligation to cite the contributing work which led to the generation of the CholecT50 and CholecT40 datasets.

-----

If you wish to have access to any of the CholecTriplet datasets, kindly fill the request form associated with it. 
When using the dataset, you are kindly requested to cite the associated publication in order to properly credit the authors and clinicians for their efforts in generating the dataset.

<br>

---------------

<br>

>## CholecT50 
- **<font color="green">Official release date:</font>** February 20, 2023
- **<font color="green">Associated publication:</font>** Nwoye, et.al. 2022 [[1]](#cite-cholect50)
- **<font color="green">Download access:</font>** [Request form](https://forms.gle/GbMj8TwNoNpMUJuv9)
    <details>
      <summary><b><font color="green">More info:</font></b></summary>
      <table>
        <td width=35%>
          <table style="border-top:solid; border-bottom:solid; border-left:solid; border-right:solid">
            <tr  style="border-bottom:solid;"><th colspan=2>VIDEO DETAILS</th></tr>
            <tr><th># videos </th><td>50</td></tr>
            <tr><th># frames </th><td>100.9K</td></tr>
            <tr><th># videos with bbox </th><td>5</td></tr>
            <tr><th># videos with bbox - triplet matching </th><td>5</td></tr>
          </table>
        </td>
        <td>
          <table style="border-top:solid; border-bottom:solid; border-left:solid; border-right:solid">
            <tr  style="border-bottom:solid;"><th colspan=4>LABEL STATISTICS</th></tr>
            <tr><th> Label</th><th>Type</th><th># Category</th><th># Instances</th></tr>
            <tr>
              <td><b>triplets</b></td><td>binary</td><td>100 </td><td> 151.0K </td>
            </tr>
            <tr>
              <td><b>instruments</b></td><td>binary</td><td> 6 </td><td> 151.0K </td>
            </tr>
            <tr>
              <td><b>instruments</b></td><td>bbox</td><td> 6 </td><td> 13.0K </td>
            </tr>
            <tr>
              <td><b>verbs</b></td><td>binary</td><td> 10 </td><td> 151.0K </td>
            </tr>
            <tr>
              <td><b>targets</b></td><td>binary</td><td> 15 </td><td> 151.0K </td>
            </tr>
            <tr>
              <td><b>phases</b></td><td>binary</td><td> 7 </td><td> 100.9K </td>
            </tr>
          </table>
        </td>
      </tr>
      </table>
    </details> 

<br>


---------------

<br>

> ## CholecT50 Challenge Validation set

- **<font color="green">Official release date:</font>** June 1, 2022
- **<font color="green">Associated publication:</font>** Nwoye, et.al. 2023 [[3]](#cite-ct2022)
- **<font color="green">Download access:</font>** [Download now](https://s3.unistra.fr/camma_public/datasets/cholect50/CholecT50-Challenge-Validation.zip)
    <details>
      <summary><b><font color="green">More info:</font></b></summary>
      <table>
        <td width=35%>
          <table style="border-top:solid; border-bottom:solid; border-left:solid; border-right:solid">
            <tr  style="border-bottom:solid;"><th colspan=2>VIDEO DETAILS</th></tr>
            <tr><th># Clips (videos slices)</th><td>5</td></tr>
            <tr><th># frames </th><td>1.1K</td></tr>
            <tr><th># Clips with bbox </th><td>5</td></tr>
            <tr><th># Clips with bbox - triplet matching </th><td>5</td></tr>
          </table>
        </td>
        <td>
          <table style="border-top:solid; border-bottom:solid; border-left:solid; border-right:solid">
            <tr  style="border-bottom:solid;"><th colspan=4>LABEL STATISTICS</th></tr>
            <tr><th> Label</th><th>Type</th><th># Category</th><th># Instances</th></tr>
            <tr>
              <td><b>triplets</b></td><td>binary</td><td>100 </td><td> 1.3K </td>
            </tr>
            <tr>
              <td><b>instruments</b></td><td>binary</td><td> 6 </td><td> 1.3K </td>
            </tr>
            <tr>
              <td><b>instruments</b></td><td>bbox</td><td> 6 </td><td> 1.3K </td>
            </tr>
            <tr>
              <td><b>verbs</b></td><td>binary</td><td> 10 </td><td> 1.3K </td>
            </tr>
            <tr>
              <td><b>targets</b></td><td>binary</td><td> 15 </td><td> 1.3K </td>
            </tr>
            <tr>
              <td><b>phases</b></td><td>binary</td><td> 7 </td><td> 1.1K </td>
            </tr>
          </table>
        </td>
      </tr>
      </table>
      
    </details> 

<p>

- Here, bbox labels are outsourced from m2cai16-tool-location [[4]](#cite-m2cbx) dataset.<br>
</p>

<br>

---------------
<br>

>## CholecT45

- **<font color="green">Official release date:</font>** April 12, 2022
- **<font color="green">Associated publication:</font>** Nwoye, et.al. 2022 [[1]](#cite-cholect50)
- **<font color="green">Download access:</font>** [Request form](https://forms.gle/jTdPJnZCmSe2Daw7A)
    <details>
      <summary><b><font color="green">More info:</font></b></summary>
      <table>
        <td width=35%>
          <table style="border-top:solid; border-bottom:solid; border-left:solid; border-right:solid">
            <tr  style="border-bottom:solid;"><th colspan=4>VIDEO DETAILS</th></tr>
            <tr><th># videos </th><td>45</td></tr>
            <tr><th># frames </th><td>90.5K</td></tr>
          </table>
        </td>
        <td>
          <table style="border-top:solid; border-bottom:solid; border-left:solid; border-right:solid">
            <tr  style="border-bottom:solid;"><th colspan=2>LABEL STATISTICS</th></tr>
            <tr><th> Label</th><th>Type</th><th># Category</th><th># Instances</th></tr>
            <tr>
              <td><b>triplets</b></td><td>binary</td><td>100 </td><td> 137.9K </td>
            </tr>
            <tr>
              <td><b>instruments</b></td><td>binary</td><td> 6 </td><td> 137.9K </td>
            </tr>
            <tr>
              <td><b>verbs</b></td><td>binary</td><td> 10 </td><td> 137.9K </td>
            </tr>
            <tr>
              <td><b>targets</b></td><td>binary</td><td> 15 </td><td> 137.9K </td>
            </tr>
            <tr>
              <td><b>phases</b></td><td>binary</td><td> 7 </td><td> 90.5K </td>
            </tr>
          </table>
        </td>
      </tr>
      </table>
    </details> 

<br>

---------------

<br>

>## CholecT40
- **<font color="green">Official release date:</font>** N/A
- **<font color="green">Associated publication:</font>** Nwoye, et.al. 2020 [[2]](#cite-cholect40)
- **<font color="green">Download access:</font>** [Request form](https://forms.gle/jTdPJnZCmSe2Daw7A)
    <details>
      <summary><b><font color="green">More info:</font></b></summary>
      <table>
        <td width=35%>
          <table style="border-top:solid; border-bottom:solid; border-left:solid; border-right:solid">
            <tr  style="border-bottom:solid;"><th colspan=2>VIDEO DETAILS</th></tr>
            <tr><th># videos </th><td>40</td></tr>
            <tr><th># frames </th><td>83.2K</td></tr>
          </table>
        </td>
        <td>
          <table style="border-top:solid; border-bottom:solid; border-left:solid; border-right:solid">
            <tr  style="border-bottom:solid;"><th colspan=4>LABEL STATISTICS</th></tr>
            <tr><th> Label</th><th>Type</th><th># Category</th><th># Instances</th></tr>
            <tr>
              <td><b>triplets</b></td><td>binary</td><td>128 </td><td> 135K </td>
            </tr>
            <tr>
              <td><b>instruments</b></td><td>binary</td><td> 6 </td><td> 135K </td>
            </tr>
            <tr>
              <td><b>verbs</b></td><td>binary</td><td> 8 </td><td> 135K </td>
            </tr>
            <tr>
              <td><b>targets</b></td><td>binary</td><td> 19 </td><td> 135K </td>
            </tr>
          </table>
        </td>
      </tr>
      </table>
    </details> 

<br>

------------------------------------------------
References
================================================

<div id="cite-cholect50">

* **[1]** C.I. Nwoye, T. Yu, C. Gonzalez, B. Seeliger, P. Mascagni, D. Mutter, J. Marescaux, N. Padoy. Rendezvous: Attention Mechanisms for the Recognition of Surgical Action Triplets in Endoscopic Videos. Medical Image Analysis 2022.
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
  <div align=right>

   [![Journal Publication](https://img.shields.io/badge/Elsevier-Medical%20Image%20Analysis-orange)](https://doi.org/10.1016/j.media.2022.102433)
   [![Read on ArXiv](https://img.shields.io/badge/arxiv-2109.03223-red)](https://arxiv.org/abs/2109.03223) 
   [![GitHub](https://img.shields.io/badge/github-rendezvous-blue)](https://github.com/CAMMA-public/rendezvous)
   [![Result Demo](https://img.shields.io/youtube/views/d_yHdJtCa98?label=video%20demo&style=social)](https://www.youtube.com/watch?v=d_yHdJtCa98&t=61s)
   </div><br></div>


<div id="cite-cholect40">

* **[2]** C.I. Nwoye, T. Yu, C. Gonzalez, P. Mascagni, D. Mutter, J. Marescaux, N. Padoy. Recognition of instrument-tissue interactions in endoscopic videos via action triplets.International Conference on Medical Image Computing and Computer-Assisted Intervention (MICCAI) 2020.
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
  <div align=right>

  [![Journal Publication](https://img.shields.io/badge/Spinger-LNCS%2012263-magenta)](https://link.springer.com/chapter/10.1007/978-3-030-59716-0_35)
  [![ArXiv paper](https://img.shields.io/badge/arxiv-2007.05405-red)](https://arxiv.org/abs/2007.05405)
  [![GitHub](https://img.shields.io/badge/github-tripnet-blue)](https://github.com/CAMMA-public/tripnet)
  </div><br></div>


<div id="cite-ct2022">

* **[3]**  C.I. Nwoye, T. Yu, S. Sharma, A. Murali, D. Alapatt A. Vardazaryan, K. Yuan, ... , D. Mutter, N. Padoy. CholecTriplet2022: Show me a tool and tell me the triplet: an endoscopic vision challenge for surgical action triplet detection. arXiv PrePrint arXiv:2204.14746. 2023.
  ```
  @article{nwoye2023cholectriplet2022,
    title={CholecTriplet2022: Show me a tool and tell me the triplet: an endoscopic vision challenge for surgical action triplet detection.},
    author={Nwoye, Chinedu Innocent and Yu, Tong and Sharma, Saurav and Murali, Aditya and Alapatt, Deepak and Vardazaryan, Armine ... Gonzalez, Cristians and Padoy, Nicolas},
    journal={arXiv preprint arXiv:2204.14746},
    year={2023}
  }
  ```
  <div align="right">

    [![Read on ArXiv](https://img.shields.io/badge/arxiv-2204.04746-red)](https://arxiv.org/abs/2204.04746)   
  </div><br></div>
  

<div id="cite-m2cbx">

* **[4]** A. Jin, S. Yeung, J. Jopling, J. Krause, D. Azagury, A. Milstein, L. Fei-Fei: Tool
detection and operative skill assessment in surgical videos using region-based convolutional
neural networks. In: WACV, pp. 691–699. 2018
  ```
  @inproceedings{jin2018tool,
     title={Tool detection and operative skill assessment in surgical videos using region-based convolutional neural networks},
     author={Jin, A., Yeung, S., Jopling, J., Krause, J., Azagury, D., Milstein, A., Fei-Fei, L.},
     booktitle={WACV},
     pages={691--699},
     year={2018}
  }
  ```
  <div align="right">


    [![Journal Publication](https://img.shields.io/badge/IEEE-WACV%2018.00081-blue)](https://ieeexplore.ieee.org/abstract/document/8354185)
    [![Read on ArXiv](https://img.shields.io/badge/arxiv-1802.08774-red)](https://arxiv.org/abs/1802.08774)   
  </div><br></div>