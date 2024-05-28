# bachelorproject
*Image-based analysis of knockdown-dependent shape transitions of migrating MDA-MB-231 cancer cells in a wound healing assay*

### Abstract
Cancer metastasis describes the spread of cancer cells from the primary tumor to distant sites in the body. It is accomplished by various cellular and molecular mechanisms that are currently researched in order to understand them and the resulting migratory behaviour of cancer cells. A mechanism also present in migrating cancer cells is the epithelial to mesenchymal transition (EMT). It includes cell shape transitions and enables cells to invade tissue, resist stress and disseminate. 

In the [thesis](https://box.hu-berlin.de/f/29a696d5bda24bc1b796/) related to this repository, the shape transitions of migrating MDA-MB-231 breast cancer cells are researched in a wound healing assay. The assay contains cells under 4 different control siRNA knockdowns, where migratory behaviour is known, as well as cells under 352 other siRNA knockdowns, where migratory behaviour is analysed. Therefore, a high-throughput experiment was conducted generating a time-series image data set with three experimental replicates. In order to gain information on the impact of various siRNA knockdowns on the migratory behavior of breast cancer cells, an image analysis workflow, utilizing several deep learning image analysis tools, is implemented. An algorithm in the workflow detects the leading edges of cells closing the wound, enabling the calculation of wound area closing over time, the leading edge velocities and positional features of single cells. Furthermore, single-cell trajectories are computed and analysed and single-cell shape features are extracted, used for directionality computations and a clustering assay.

### Wound healing assay
Studying cell migration in controlled experimental settings provides valuable insights into the dynamic behaviors of cancer cells during the metastatic process as well as in understanding cancer cell phenotype. Visualization of growth, individual cell movements, cell-cell interactions, and the overall progression of migration in response to various stimuli or treatments can be made visible through wound healing assays. Image-based data of cells moving while reacting to a perturbation captures a snapshot of the cell's condition. To observe and quantify morphological and comparable features in time and space it is essential to understand the relation of signaling networks and resulting migratory behavior. Wound healing, the movement of cells into a wound to accomplish gap closure, is a way to perturb a system to show its reaction on a change in its microenvironment. Other cell migration assays are chemotaxis, where cells migrate in response to a chemical environment, haptotaxis, meaning cell migration happens within a gradient of chemoattractants, and transmigration, which refers to cells moving through a vascular endothelium. When using the technique of a wound healing assay, a gap is created by mechanically scratching a confluent monolayer of cells with a needle in order to remove some of them. After that, cells move inward to fill the void as visible in:
![wound healing](/images/GIF_005023.gif)
Compatible with image based readout the scratch assay offers enhanced accuracy, sensitivity and robustness in learning about the underlying mechanisms governing cancer cell movement in comparison to other migration assays.

### siRNA knockdowns
Recent research has increasingly focused on identifying key regulatory molecules and signaling pathways that influence cancer cell migration, with particular attention given to small interfering RNA (siRNA) knockdown approaches. By analysing the effects of gene knockdowns on cell morphology, migration dynamics, and collective behavior, critical insights into the roles of specific genes and proteins in signaling networks of cancer metastasis can be gained. By that, potential drug targets may be identified. Gene knockdown experiments can be achieved through for example CRISPR/Cas or RNA interference (RNAi) gene editing, which allows to selectively inhibit the expression of target genes involved in cell motility. The effectiveness of siRNA in inhibiting the expression of key oncogenes and signaling pathways implicated has been shown in various cancer types.

In the conducted wound healing experiment, a wound closing more intensely would suggest an aggressively growing siRNA knockdown. In comparison, cells closing a wound less fast than the wild type cells indicate the detection of a potential drug target.

### Methods and Results
This repository gives an overview of the code used to analyse biological time-series image data. It is divided into the four sub-topics 1. Image pre-processing, 2. Scratch detection, 3. Cell feature analysis and 4. Cell trajectory analysis. Each sub-topic is represented by either a Jupyter Notebook or a Python script covering some code as well as explanations and graphics.

1. [Image pre-processing](https://github.com/olxssa/bachelorproject/blob/main/image_stitching_AND_drift_correction_exp2_MIST.ijm):
* Image stitching using the Fiji plugin ['Microscopy Image Stitching Tool'](https://www.nature.com/articles/s41598-017-04567-y)
* Image drift correction using the Fiji plugin ['NanoJ Core'](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7655149/)

2. [Scratch detection]():
* The scratch detection algorithm
* Closure of wound area
* Velocity of tissue borders
* Distance fields
   
3. [Cell feature analysis]():
* Cell segmentation using [Cellpose 2.0](https://www.nature.com/articles/s41592-022-01663-4)
* Extraction of cell features using scikit-image 
* Nuclei displacement polarity
* Leiden Clustering of cell features
   
4. [Cell trajectory analysis]():
* Tracking of single cells using [DeepCell-Tracking](https://github.com/vanvalenlab/deepcell-tracking)
* Trajectory measures Mean Squared Displacment (MSD) and Persistency

### Disclaimers
* All example images displayed are from knockdown NTC1 (non-targeting control), derived from cell line MDA-MB-231. 
* In the analysis, the word ’cell’ in combination with an image analysis explanation refers to the objects contained in the cytoplasma channel of the images, since it characterizes the outline and area of the cell.
