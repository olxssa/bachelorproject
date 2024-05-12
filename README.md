# bachelorproject
*Image-based analysis of knockdown-dependent shape transitions of migrating MDA-MB-231 cancer cells in a wound healing assay*

### Abstract
Cancer metastasis describes the spread of cancer cells from the primary tumor to distant sites in the body. It is accomplished by various cellular and molecular mechanisms that are currently researched in order to understand them and the resulting migratory behaviour of cancer cells. A mechanism also present in migrating cancer cells is the epithelial to mesenchymal transition (EMT). It includes cell shape transitions and enables cells to invade tissue, resist stress and disseminate. 

In the thesis related to this repository, the shape transitions of migrating MDA-MB-231 breast cancer cells are researched in a wound healing assay. The assay contains cells under 4 different control siRNA knockdowns, where migratory behaviour is known, as well as cells under 352 other siRNA knockdowns, where migratory behaviour is analysed. Therefore, a high-throughput experiment was conducted generating a time-series image data set with three experimental replicates. In order to gain information on the impact of various siRNA knockdowns on the migratory behavior of breast cancer cells, an image analysis workflow, utilizing several deep learning image analysis tools, is implemented. An algorithm in the workflow detects the leading edges of cells closing the wound, enabling the calculation of wound area closing over time, the leading edge velocities and positional features of single cells. Furthermore, single-cell trajectories are computed and analysed and single-cell shape features are extracted, used for directionality computations and a clustering assay.

### Methods and Results
This repository gives an overview of the code used to analyse biological time-series image data. 

All example images displayed are from knockdown NTC1 (non-targeting control), derived from cell line MDA-MB-231. In further analysis, the word ’cell’ in combination with an image analysis explanation refers to the objects contained in the cytoplasma channel of the images, since it characterizes the outline and area of the cell.

1. [Image pre-processing]():
* Image stitching using the Fiji plugin ['Microscopy Image Stitching Tool'](https://www.nature.com/articles/s41598-017-04567-y)
* Image drift correction using the Fiji plugin ['NanoJ Core'](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7655149/)

2. [Scratch detection]():
* The scratch detection algorithm
* Closure of wound area
* Velocity of tissue borders
* Distance fields
   
3. [Cell feature extraction]():
* Cell segmentation using [Cellpose 2.0](https://www.nature.com/articles/s41592-022-01663-4)
* Extraction of cell features using scikit-image 
* Nuclei displacement polarity
* Leiden Clustering of cell features
   
4. [Cell trajectory analysis]():
* Tracking of single cells using [DeepCell-Tracking](https://github.com/vanvalenlab/deepcell-tracking)
* Trajectory measures Mean Squared Displacment (MSD) and Persistency
