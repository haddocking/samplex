SAMPLEX
=======

## Smooth Automated Mapping of Proteins from Listed EXtreme (SAMPLEX) ###

## Authors: Mickael Krzeminski 

## Version: 1.0, August 2009

## Reference:

When using SAMPLEX cite:

* M. Krzeminski, K. Loth, R. Boelens and A.M.J.J. Bonvin SAMPLEX: Automatic mapping of perturbed and unperturbed regions of proteins and complexes. BMC Bioinformatics, 11, 51 (2010).


The activity of proteins within the cell is characterized by their motions, flexibility, interactions or even the particularly intriguing case of partially unfolded states. In the last two cases, a part of the protein is affected either by binding or unfolding and the detection of the respective perturbed and unperturbed region(s) is a fundamental part of the structural characterization of these states. This can be achieved by comparing experimental data of the same protein in two different states (bound/unbound, folded/unfolded). For instance, measurements of chemical shift perturbations (CSPs) from NMR 1H-15N HSQC experiments gives an excellent opportunity to discriminate both moieties.


SAMPLEX is an innovative, automatic and unbiased method to distinguish perturbed and unperturbed regions in a protein existing in two distinct states (folded/partially unfolded, bound/unbound). The SAMPLEX program takes as input a set of data and the corresponding three-dimensional structure and returns the confidence for each residue to be in a perturbed or unperturbed state. Its performance is demonstrated for different applications including the prediction of disordered regions in partially unfolded proteins and of interacting regions in protein complexes.


The method is not restricted to NMR data, but is generic and can be applied to a wide variety of information. It requires as input a 3D structure of the protein, and a data table containing residue numbers with their associated property to be classified.



##Usage:##
```
	python samplex_1.0.py [-ng -f save.samp | -f save.samp]
```


Requirements
------------

   SAMPLEX only requires:
		1. A structure file
		2. A data file

An example is provided with all distribution. Please, always test it the first time you
use SAMPLEX.


	1. Structure file

   As the algorithm that governs SAMPLEX is based on the three dimension structure of
the bio-molecule, the program first need the structure file, which specifies the ensemble
of files that contain the atomic coordinates of the molecule. In case where there is only
one file, please DO NOT specify this pdb file, but write in the structure file the location
of this single file. Of note, the ensemble of specified files must contain the same atoms
(NMR ensemble for instance).


	2. Data file

   The data file contains the perturbation information that SAMPLEX will treat.
The perturbation data file must look like the following:
			7	0.2911
			11	0.0712
			20	0.1101
			21	0.0810
			27	0.2310
			...

The values that are specified depends on the data type and the way the user interpret them. For
instance, a convenient experiment in NMR is to measure the 1H-15N HSQC spectrum of the same protein in
two different states. Once the peak are attributed for each amide group, the chemical shift pertur-
bations can be estimated with: sqrt[pow(DHN, 2)+pow(DN/6.515, 2) (Farmer, 1996; Mulder et al., 1999)



Interface
----------

   SAMPLEX is before all of graphical usage. It uses Python language and requires some crucial
libraries to be run. In case where these libraries are not present in the normal installation
directory of Python, the program will complain and invit you to use a non-graphical interface.


	1. Graphical interface (GI)

   The GI is by default run. With the option -f, the user can load directly a previously saved
file to gain time, instead of filling all requiered fields, as following:
```
	samplex_1.0.py -f save.samp
```
You can also run SAMPLEX without specifying any save file. SAMPLEX will automatically invit you
to load one. You can ignore and cancel this proposition if you want to start from scratch.
In case where some problems are met while reading the save file, SAMPLEX will use some values by
default.


   The GI is split into two parts: the general information and the advanced option. In the former
one, you have to specify the working directory, where will be created the output files, and where
SAMPLEX will first look at to find other files (if their location are specified relatively). Then,
the location of the structure file and the experimental file must be specified.

The advanced options gives the user the possibility to specify the confidence range that makes a
residue considered as perturbed, non-perturbed or intermediate. Moreover, the progression of calculations
can be visualized with PyMol. This options must be checked to be run. In PyMol, for each run, the
unperturbed, perturbed and intermediate regions are colored in blue, red and purple, respectively.


			
	2. Non-Graphical interface (NGI)

   In the NGI, the user must provide a correct saved file. An example of this file is provided with
the distribution. If an error is encountered in the save file, the program will abandon and stop.
The user will have to check the specified save file manually before re-running SAMPLEX.
In this NGI, no PyMol interface will be run.








Known problems
--------------

Obviously, many different platforms trigger problems on some of them. The following part list
the possible errors you can meet and how to fix them.

1. I got a message similar to "samplex_1.0.py: Command not found." upon running SAMPLEX. Why ?
  This can be due to the pathway python has been installed on your computer. We assume for a Linux
distribution for instance that your /usr/bin/env file can locate it. If it is not the case, replace
the very first line of the script by the correct location, as following:
```
    #!/usr/bin/env python	-->	#!/usr/bin/python
```
		alternatively simply call samplex with python as:
```
    python samplex_1.0.py
```
The other reason can come that you are not in the directory where is located the main Python script
of SAMPLEX. In such a case, change directory or specify either a CORRECT absolute or relative pathway.

2. Samplex stops with some strange error message.
   This is often related to the graphical interface. You can run samplex in its non-graphical mode by adding the --ng option
For this edit first the paramter file to define all files and paramters and then call samplex with:
```
   samplex_1.0.py -ng -f save.samp
```
