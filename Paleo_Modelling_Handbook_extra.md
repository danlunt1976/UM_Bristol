
## Exploring more paleoclimate model simulations

You are welcome to explore other variables in the xbmsa, xbmsb, and xbmsc simulations.  In the Lunt et al (2008) paper I only plotted a handful of variables, so you may be able to find some new and exciting discoveries about the closure of the Panama Seaway!  Similarly with the texps2 simulation - feel free to look at this in more detail and explore mid-Cretaceous climate.  

However, you may want to explore other simulations as well.  We have lots of potentially exciting data that we have never even looked at.  You can access any of our simulations, if you know the 5-letter or 6-letter code of that simulation.  For the various file types and naming conventions, see sections 'Climate variables' and 'Timeseries' and 'Sediments and other derived quantities' and 'Boundary conditions and chronologies' in this document, which focuses on our Phanerozoic simulations but is applicable to any simulations:
 [https://danlunt1976.github.io/UM_Bristol/Accessing_scotese.html](https://danlunt1976.github.io/UM_Bristol/Accessing_scotese.html)
**However, please don't publish with the unpublished simulations without discussing with Dan first (d.j.lunt@bristol.ac.uk)!**

Broadly speaking, these are the different types of simulation that are available to explore:

### 1) Published simulations in the BRIDGE archive

We have a webpage that lists the [simulations from a selection of our published papers](https://www.paleo.bristol.ac.uk/ummodel/scripts/papers/).  Click on a paper that you are interested in, e.g. [Farnsworth et al, 2019](https://www.paleo.bristol.ac.uk/ummodel/scripts/papers/Farnsworth_et_al_2019b.html) which explores the evolution of the East Asian monsoon over the last 150 million years, or [Armstrong et al, 2023](https://www.paleo.bristol.ac.uk/ummodel/scripts/papers/Armstrong_et_al_2023.html) which explores the evolution of the African monsoon over the last 800 thousand years (both include global outputs with many different variables).  This takes you to a table which lists the experiment names in that paper (typically a 5 or 6-letter code similar to the 'xbmsa' we used earlier).  If you click on one of the experiment names, it will take you to a table of plots, but you can download the data and make your own plots, as this gives more flexibility, and allows you to carry out analysis.

Again, there are loads of variables that I have never looked at in these simulations, so have fun exploring!  These data are open access, so feel free to use them in publications.  In addition, the Paleo Modelling Group at the University of Bristol are always happy to be involved as collaborators if you think that would be useful - just get in contact (d.j.lunt@bristol.ac.uk).

### 2) Phanerozoic simulations

We have recently been working on multiple suites of Phanerozoic simulations.  Some of these are published in Valdes et al (2021).  You can see an overview of the Valdes et al (2021) simulations [here](https://www.paleo.bristol.ac.uk/ummodel/scripts/papers/Valdes_et_al_2021.html), and then click on 'Detailed list of runs' for the ensemble that you are interested in.  In addition we also have some unpublished runs (in particular the 'tfke' and 'tfks') which you can explore. 

Detailed descriptions of all our Phanerozoic simulations, download instructions, and naming conventions are available in this document:
 [https://danlunt1976.github.io/UM_Bristol/Accessing_scotese.html](https://danlunt1976.github.io/UM_Bristol/Accessing_scotese.html)
**However, please don't publish with the unpublished simulations without discussing with Dan first (d.j.lunt@bristol.ac.uk)!**

### 3) Phanerozoic simulations with biogeochemistry

Paul Valdes has carried out some initial ocean biogeochemistry simulations through the Phanerozoic.  **These are completely unpublished so again, please don't publish with these without discussing with Dan and Paul Valdes first (d.j.lunt@bristol.ac.uk and p.j.valdes@bristol.ac.uk)!**   This is the 'teyj' series.  You can see an overview of the experiment names, and view some pre-produced plots here:
[https://www.paleo.bristol.ac.uk/ummodel/scripts/html_bridge/scotese_OBC_02.html](https://www.paleo.bristol.ac.uk/ummodel/scripts/html_bridge/scotese_OBC_02.html)
To access the actual netcdf data for the biogeochemistry variables, you will need to download the data, and then view it in Python, or in Panoply.  The data are in the 'o.pg' files (see [https://danlunt1976.github.io/UM_Bristol/Accessing_scotese.html](https://danlunt1976.github.io/UM_Bristol/Accessing_scotese.html) for details), which can be downloaded, for example for the preindustrial control, from:
[https://www.paleo.bris.ac.uk/ummodel/data/teyja/climate/teyjao.pgclann.nc](https://www.paleo.bris.ac.uk/ummodel/data/teyja/climate/teyjao.pgclann.nc)
or e.g. for the early Cambrian from:
[https://www.paleo.bris.ac.uk/ummodel/data/teYje/climate/teYjeo.pgclann.nc](https://www.paleo.bris.ac.uk/ummodel/data/teYje/climate/teYjeo.pgclann.nc)
### 4) Glacial-interglacial Plio-Pleistocene simulations

We also have some a very recent set of simulations through the last 3.6 million years, carried out by Paul Valdes and Jeanne Millot-Weil.  Their naming conventions are available in Appendix 4, and you can download them following the guidance in Appendix 3.  **These are completely unpublished so again, please don't publish with these without discussing with Dan and Jeanne Millot-Weil and Paul Valdes first (d.j.lunt@bristol.ac.uk and xk22684@bristol.ac.uk and p.j.valdes@bristol.ac.uk)!**   

This is a set of 919 simulations through the plio-Pleistocene (3.6 Ma to 0 Ma), including changes to topography bathymetry, land-sea mask, ice sheets, orbit, and CO2.  
The naming convention is:  
xxxx{a..z} ; xxxx{A..Z} ; xxxx{0..9} = 26+26+10=62 simulations per set  
where xxxx is: tfmc, tfmC, tfMc, tfMC, tFmc, tFmC, tFMc, tFMC, tfmd, tfmD, tfMd, tfMD, tFmd, tFmD = 14 full sets  
and where xxxx is tFMd{a..z}, tFMd{A..Y} = 26+25 = 51 simulations  
TOTAL = 14\*62 + 51 = 868+51 = 919 simulations  

The age of of each simulation is such that there is 1 simulation per kyr from 0 to 24ka (25 simulations), and then 1 simulation every 4 years (919-25 simulations).  So the total covered is 24kyr+((919-25=894)\*4=3576 kyr) = 3.6Myr.  

#### Downloading multiple simulations 

If you are wanting to download lots of simulations (e.g. a Phanerozoic or Plio-Pleistocene ensemble), then downloading each simulation manually in turn will take a long time.  Instead, if you have Mac or Linux machine, then you can write a script to automate this; see Appendix 2 in this document:
[https://danlunt1976.github.io/UM_Bristol/Accessing_scotese.html](https://danlunt1976.github.io/UM_Bristol/Accessing_scotese.html)


## Exploring additional variables

In addition to the climate and boundary condition files you already explored, you can also download some other useful data from the simulations.  

In particular, we have run an offline sediments model, with input from the modelled temperature and precipitation for all of the simulations. This includes modelled predictions of regions, of evaporites, coals, bauxite etc. These modelled predictions can be compared with the geological record of sedimentological data, in order to evaluate the model, and/or to indicate regions of potential sediments in regions where the geological record may be incomplete.   
Download instructions for these, and other derived quantities, can be found in this document:
[https://danlunt1976.github.io/UM_Bristol/Accessing_scotese.html](https://danlunt1976.github.io/UM_Bristol/Accessing_scotese.html)

We also have timeseries of some variables.  The climate files above all represent the climatological average of several (typically 30 or 50 or 100 years) at the end of the model simulation.  However, the simulation may be thousands of years long.  We do not save the entire timeseries for all variables, but we do for some key variables.
These can be downloaded, for example for experiment texps2 (mid Cretaceous), for the variable temp_mm_1_5m (near-surface air temperature):     
https://www.paleo.bristol.ac.uk/ummodel/data/texps2/monthly/texps2.temp_mm_1_5m.monthly.nc  
For more info see this document:
[https://danlunt1976.github.io/UM_Bristol/Accessing_scotese.html](https://danlunt1976.github.io/UM_Bristol/Accessing_scotese.html)
