# bachelorproject
Image-based analysis of knockdown-dependent shape transitions of migrating MDA-MB-231 cancer cells in a wound healing assay

### Abstract
Cancer metastasis describes the spread of cancer cells from the primary tumor to distant sites in the body. It is accomplished by various cellular and molecular mechanisms that are currently researched in order to understand them and the resulting migratory behaviour of cancer cells. A mechanism also present in migrating cancer cells is the epithelial to mesenchymal transition (EMT). It includes cell shape transitions and enables cells to invade tissue, resist stress and disseminate. In the thesis related to this repository, the shape transitions of migrating MDA-MB-231 breast cancer cells are researched in a wound healing assay. The assay contains cells under 4 different control siRNA knockdowns, where migratory behaviour is known, as well as cells under 352 other siRNA knockdowns, where migratory behaviour is analysed. Therefore, a high-throughput experiment was conducted generating a time-series image data set with three experimental replicates. In order to gain information on the impact of various siRNA knockdowns on the migratory behavior of breast cancer cells, an image analysis workflow, utilizing several deep learning image analysis tools, is implemented. An algorithm in the workflow detects the leading edges of cells closing the wound, enabling the calculation of wound area closing over time, the leading edge velocities and positional features of single cells. Furthermore, single-cell trajectories are computed and analysed and single-cell shape features are extracted, used for directionality computations and a clustering assay.

### Methods and Results
* Scratch detection algorithm
* Cell feature extraction
* Cell trajectory analysis
