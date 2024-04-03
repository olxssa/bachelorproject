// Experiment 2: started June 22, 2017 at 19:53:39
// This macro takes 3 flex files per timepoint (17) and knockdown (384) and stitches them using MIST. After that it creates one stack and then one hyperstack per knockdown (384). Afterwards it performs drift correction on every hyperstack.
// The list containing the knockdown numbers was created using Python and pasted into the macro script.

list = newArray('001001','001002','001003','001004','001005','001006','001007','001008','001009','001010','001011','001012','001013','001014','001015','001016','001017','001018','001019','001020','001021','001022','001023','001024','002001','002002','002003','002004','002005','002006','002007','002008','002009','002010','002011','002012','002013','002014','002015','002016','002017','002018','002019','002020','002021','002022','002023','002024','003001','003002','003003','003004','003005','003006','003007','003008','003009','003010','003011','003012','003013','003014','003015','003016','003017','003018','003019','003020','003021','003022','003023','003024','004001','004002','004003','004004','004005','004006','004007','004008','004009','004010','004011','004012','004013','004014','004015','004016','004017','004018','004019','004020','004021','004022','004023','004024','005001','005002','005003','005004','005005','005006','005007','005008','005009','005010','005011','005012','005013','005014','005015','005016','005017','005018','005019','005020','005021','005022','005023','005024','006001','006002','006003','006004','006005','006006','006007','006008','006009','006010','006011','006012','006013','006014','006015','006016','006017','006018','006019','006020','006021','006022','006023','006024','007001','007002','007003','007004','007005','007006','007007','007008','007009','007010','007011','007012','007013','007014','007015','007016','007017','007018','007019','007020','007021','007022','007023','007024','008001','008002','008003','008004','008005','008006','008007','008008','008009','008010','008011','008012','008013','008014','008015','008016','008017','008018','008019','008020','008021','008022','008023','008024','009001','009002','009003','009004','009005','009006','009007','009008','009009','009010','009011','009012','009013','009014','009015','009016','009017','009018','009019','009020','009021','009022','009023','009024','010001','010002','010003','010004','010005','010006','010007','010008','010009','010010','010011','010012','010013','010014','010015','010016','010017','010018','010019','010020','010021','010022','010023','010024','011001','011002','011003','011004','011005','011006','011007','011008','011009','011010','011011','011012','011013','011014','011015','011016','011017','011018','011019','011020','011021','011022','011023','011024','012001','012002','012003','012004','012005','012006','012007','012008','012009','012010','012011','012012','012013','012014','012015','012016','012017','012018','012019','012020','012021','012022','012023','012024','013001','013002','013003','013004','013005','013006','013007','013008','013009','013010','013011','013012','013013','013014','013015','013016','013017','013018','013019','013020','013021','013022','013023','013024','014001','014002','014003','014004','014005','014006','014007','014008','014009','014010','014011','014012','014013','014014','014015','014016','014017','014018','014019','014020','014021','014022','014023','014024','015001','015002','015003','015004','015005','015006','015007','015008','015009','015010','015011','015012','015013','015014','015015','015016','015017','015018','015019','015020','015021','015022','015023','015024','016001','016002','016003','016004','016005','016006','016007','016008','016009','016010','016011','016012','016013','016014','016015','016016','016017','016018','016019','016020','016021','016022','016023','016024');
 
path_input = '/home/basar/Olyssa/Exp2_2017_06_22/'
path_output = '/home/basar/Olyssa/exp2/'
path_done = '/home/basar/Olyssa/exp2_done/'

for (k=0; k<list.length; k++) {
	for (j=0; j<17; j++) {
		// import image sub-tile 001 (mid), split into the two color channels C=0 (nuc) and C=1 (cyto), enhance image contrast, merge both channels, transform the nuc-cyto stack to RGB and save as 002
		run("Bio-Formats Importer", "open=" + path_input + list[k] + "001_" + j + ".flex autoscale color_mode=Default rois_import=[ROI manager] split_channels view=Hyperstack stack_order=XYCZT");
		selectImage("" + list[k] + "001_" + j + ".flex - C=0");
		run("Enhance Contrast", "saturated=0.35");
		selectImage("" + list[k] + "001_" + j + ".flex - C=1");
		run("Enhance Contrast", "saturated=0.35");
		run("Merge Channels...", "c1=[" + list[k] + "001_" + j + ".flex - C=1] c2=[" + list[k] + "001_" + j + ".flex - C=0] create");
		run("Stack to RGB");
		saveAs("Tiff", path_output + list[k] + "002_" + j + "_RGB.tif");
		run("Close All");
		
		// import image sub-tile 002 (left), split into the two color channels C=0 (nuc) and C=1 (cyto), enhance image contrast, merge both channels, transform the nuc-cyto stack to RGB and save as 001
		run("Bio-Formats Importer", "open=" + path_input + list[k] + "002_" + j + ".flex autoscale color_mode=Default rois_import=[ROI manager] split_channels view=Hyperstack stack_order=XYCZT");
		selectImage("" + list[k] + "002_" + j + ".flex - C=0");
		run("Enhance Contrast", "saturated=0.35");
		selectImage("" + list[k] + "002_" + j + ".flex - C=1");
		run("Enhance Contrast", "saturated=0.35");
		run("Merge Channels...", "c1=[" + list[k] + "002_" + j + ".flex - C=1] c2=[" + list[k] + "002_" + j + ".flex - C=0] create");
		run("Stack to RGB");
		saveAs("Tiff", path_output + list[k] + "001_" + j + "_RGB.tif");
		run("Close All");
		
		// import image sub-tile 003 (right), split into the two color channels C=0 (nuc) and C=1 (cyto), enhance image contrast, merge both channels, transform the nuc-cyto stack to RGB and save as 003
		run("Bio-Formats Importer", "open=" + path_input + list[k] + "003_" + j + ".flex autoscale color_mode=Default rois_import=[ROI manager] split_channels view=Hyperstack stack_order=XYCZT");
		selectImage("" + list[k] + "003_" + j + ".flex - C=0");
		run("Enhance Contrast", "saturated=0.35");
		selectImage("" + list[k] + "003_" + j + ".flex - C=1");
		run("Enhance Contrast", "saturated=0.35");
		run("Merge Channels...", "c1=[" + list[k] + "003_" + j + ".flex - C=1] c2=[" + list[k] + "003_" + j + ".flex - C=0] create");
		run("Stack to RGB");
		saveAs("Tiff", path_output + list[k] + "003_" + j + "_RGB.tif");
		run("Close All");
		
		// execute image stitching with the tool 'MIST' (Microscopy Image Stitching Tool)
		run("MIST", "gridwidth=3 gridheight=1 starttile=1 imagedir=/home/basar/Olyssa/exp2 filenamepattern=" + list[k] + "00{p}_" + j + "_RGB.tif filenamepatterntype=SEQUENTIAL gridorigin=UL assemblefrommetadata=false assemblenooverlap=false globalpositionsfile=[] numberingpattern=HORIZONTALCOMBING startrow=0 startcol=0 extentwidth=3 extentheight=1 timeslices=0 istimeslicesenabled=false outputpath=" + path_output + " displaystitching=true outputfullimage=true outputmeta=true outputimgpyramid=false blendingmode=LINEAR blendingalpha=NaN compressionmode=UNCOMPRESSED outfileprefix="+list[k]+"_"+j+"_stitched_MIST unit=MICROMETER unitx=1.0 unity=1.0 programtype=AUTO numcputhreads=16 loadfftwplan=true savefftwplan=true fftwplantype=MEASURE fftwlibraryname=libfftw3 fftwlibraryfilename=libfftw3.dll planpath=/home/olyssa/lib/fftw/fftPlans fftwlibrarypath=/home/olyssa/lib/fftw stagerepeatability=0 horizontaloverlap=15.0 verticaloverlap=7.0 numfftpeaks=0 overlapuncertainty=1 isusedoubleprecision=false isusebioformats=false issuppressmodelwarningdialog=false isenablecudaexceptions=false translationrefinementmethod=SINGLE_HILL_CLIMB numtranslationrefinementstartpoints=16 headless=false loglevel=MANDATORY debuglevel=NONE");

		// save stitched image 
		saveAs("Tiff", path_output + list[k] + "_" + j + "_fused_MIST.tif");
		run("Close All");
	}
	// opening stitched images of one time series
	run("Close All");
	for (i=0; i<17; i++) {
		run("Bio-Formats Importer", "open=" + path_output + list[k] + "_" + i + "_fused_MIST.tif autoscale color_mode=Composite rois_import=[ROI manager] view=Hyperstack stack_order=XYCZT");
	}
	// concatenate the time series images, transform to hyperstack and save the hyperstack
	run("Concatenate...", "open image1=" + list[k] + "_0_fused_MIST.tif image2=" + list[k] + "_1_fused_MIST.tif image3=" + list[k] + "_2_fused_MIST.tif image4=" + list[k] + "_3_fused_MIST.tif image5=" + list[k] + "_4_fused_MIST.tif image6=" + list[k] + "_5_fused_MIST.tif image7=" + list[k] + "_6_fused_MIST.tif image8=" + list[k] + "_7_fused_MIST.tif image9=" + list[k] + "_8_fused_MIST.tif image10=" + list[k] + "_9_fused_MIST.tif image11=" + list[k] + "_10_fused_MIST.tif image12=" + list[k] + "_11_fused_MIST.tif image13=" + list[k] + "_12_fused_MIST.tif image14=" + list[k] + "_13_fused_MIST.tif image15=" + list[k] + "_14_fused_MIST.tif image16=" + list[k] + "_15_fused_MIST.tif image16=" + list[k] + "_15_fused_MIST.tif image17=" + list[k] + "_16_fused_MIST.tif");
	run("Stack to Hyperstack...", "order=xyczt(default) channels=3 slices=1 frames=17 display=Composite");
	saveAs("Tiff", path_output + list[k] + "_hyperstack_MIST.tif");
	run("Close All");
	
	// open the hyperstack 
	run("Bio-Formats Importer", "open=" + path_output + list[k] + "_hyperstack_MIST.tif autoscale color_mode=Colorized rois_import=[ROI manager] split_channels view=Hyperstack stack_order=XYCZT");
	selectImage("" + list[k] + "_hyperstack_MIST.tif - C=2");
	close();
	// perform drift estimation and correction using the channel C=0, save the nuc-channel time series image stack
	selectImage("" + list[k] + "_hyperstack_MIST.tif - C=0");
	run("Estimate Drift", "time=1 max=0 reference=[previous frame (better for live)] show_cross-correlation show_drift_plot show_drift_table apply choose=[" + path_output + list[k] + "_hyperstack_MIST_C=0.njt]");
	saveAs("Tiff", path_done + list[k] + "_hyperstack_drift_corrected_nuc_MIST.tif");
	close();
	selectImage("" + list[k] + "_hyperstack_MIST.tif - C=0");
	close();
	// select the cyto-channel time series image stack and perform the same drift correction as applied to the nuc-channel stack, save cyto-channel image stack
	selectImage("" + list[k] + "_hyperstack_MIST.tif - C=1");
	run("Correct Drift", "choose=[" + path_output + list[k] + "_hyperstack_MIST_C=0DriftTable.njt]");
	saveAs("Tiff", path_done + list[k] + "_hyperstack_drift_corrected_cyto_MIST.tif");
	
	run("Close All");
}



//other stitching plugin:

//run("Grid/Collection stitching", "type=[Grid: row-by-row] order=[Right & Down                ] grid_size_x=3 grid_size_y=1 tile_overlap=4 first_file_index_i=1 directory=" + path_output + " file_names=" + list[k] + "00{i}_" + j + "_RGB.tif output_textfile_name=TileConfiguration"+list[k]+".txt fusion_method=[Linear Blending] regression_threshold=0.30 max/avg_displacement_threshold=2.50 absolute_displacement_threshold=3.50 compute_overlap computation_parameters=[Save computation time (but use more RAM)] image_output=[Fuse and display]");
//saveAs("Tiff", path_output + list[k] + "_" + j + "_RGB_stitched.tif");
//run("Close All");






