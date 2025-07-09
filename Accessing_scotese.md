
[Back to Collaborations](Collaborations.md)

# Accessing Phanerozoic simulation data

# Introduction

This document describes how to access BRIDGE climate outputs.  In particular, it focuses on ensembles of HadCM3L Phanerozoic simulations.

If you do download these simulations, then please let us know, and we always like to be involved in the science that you carry out with the simulations!  In particular, some of the simulations are unpublished, and if you use these then we would ask to be included as co-authors in any papers that use them.

We have a number of HadCM3L Phanerozoic ensembles; each one can be identified by its 5-letter PUMA (Providing Unified Model Access) code.  Each ensemble consists of 109 simulations through the Phanerozoic.

The “standard” ensembles that we currently have are:

“**texy**” series: These are the “Smooth CO2” simulations described in Valdes et al (2021).

“**texp**” series: These are the “Foster CO2” simulations described in Valdes et al (2021).

"**tfke**" series: These are similar to the Valdes et al (2021) simulations, but have several improvements to the underlying climate model (e.g. tuned atmospheric and ocean physics to give more polar amplification, in line with paleo temperature proxies), better ocean solver, reduction of gridpoint noise).  Also a change to the late Cretaceous and early Cenozoic CO2, to be more in line with Rae et al. (2021).  These simulations are currently unpublished, but we are in the process of writing them up.  They were included in Judd et al (2024), but only a very limited number of variables.

"**tfks**” series: As tfke, but with a CO2 evolution through the Phanerozoic that is tuned to give GMSTs in line with Scotese et al (2021).  These simulations are currently unpublished, but we are in the process of writing them up.

**“xqbp”** series: As tfks but with more output variables.  Run for 110 years.

13/1/2023: The current “best” ensemble is tfke if you have most confidence in the CO2 proxies + model climate sensitivity, and tfks if you have most confidence in the temperature proxies from Scotese et al. (2021).

The naming convention of the 109 simulations is as follows, e.g. for tfke the simulation names are:

tfke{a..z}  
tfkE{a..z}  
tfKe{a..z}  
tfKE{a..z}  
tFke{a..e}  

where tfkea is 0Ma and tFkee is 540 Ma.

However, note that the last 5 simulations of the texp series are texq{a..e} rather than tExp{a..e}, and that some of the simulation names in texp are appended with a “1” or a “2” – for a list see here: [https://www.paleo.bristol.ac.uk/ummodel/scripts/html_bridge/scotese_02.html](https://www.paleo.bristol.ac.uk/ummodel/scripts/html_bridge/scotese_02.html)

There are also some other ensembles available, but they are not all published, and some may not be fully spun up, so please do get in contact before using them.  See Appendix 1.

# Standard text for describing the model in Valdes et al (2021)

We use a version of the coupled atmosphere-ocean General Circulation Model (GCM), HadCM3 (Gordon et al., 2000). The specific underlying version, HadCM3BL-M2.1aD, is described in detail in Valdes et al. (2017), with additional modifications applied in order to simulate deep-time past climates, described in Valdes et al (2021).  The model has a horizontal resolution of 3.75$^\circ$ × 2.5$^\circ$ in longitude–latitude in both the atmosphere and the ocean, and a vertical resolution with 19(20) unequally spaced vertical levels in the atmosphere(ocean).  Although HadCM3 is a relatively low-resolution and low complexity model compared to the latest state-of-the art models in CMIP6, its performance in simulating modern climate is comparable to many CMIP5 models (Valdes et al., 2017).

# Standard text for describing tfks, tfke simulations

*tfke and tfks*  
The simulations are similar to those described in detail in Valdes et al (2021).  Compared to the simulations presented in Valdes et al (2021), the simulations used in this paper have undergone a number of developments, associated with improvements to the model itself, and to the experimental design. The most significant of these are summarised here.  The version of the climate model used in this paper has an update that includes modification to Cloud Condensation Nuclei (CCN) density and cloud droplet effective radius, following the work of Sagoo et al. (2013) and Kiehl and Shields (2013). This update increases higher latitude temperatures without significantly changing tropical temperatures, thereby reducing the pole-to-equator temperature gradient, and better aligning higher latitude temperatures with proxy observations. This update has been verified to be effective under a range of climate conditions, including hot, cool, and icehouse conditions, as well as under pre-industrial boundary conditions. As a result, it is suitable for application throughout the Phanerozoic. In addition, other internal model parameters were tuned, following Irvine et al. (2013). The ocean barotropic flow solver requires all islands in the paleogeography to be manually defined, to allow non-zero flow through ocean gateways. Although Antarctica was defined as an island in the Valdes et al. (2021) post-Eocene simulations, no other islands were defined. For the simulations in this paper, all islands were defined through the Phanerozoic.  A smoothing function was applied in the atmosphere and ocean to avoid gridpoint noise that develops slowly in very long simulations.  In the Valdes et al simulations, the bare-soil albedo is a uniform constant, whereas in these simulations the bare-soil albedo is calculated as a function of the soil carbon content.

*tfke only*  
In the Valdes et al simulations, the atmospheric CO2 is consistent with that of Foster et al (2017).  In these simulations, the atmospheric CO2 was modified in the late Cretaceous and Cenozoic to be consistent with the CO2 record of Rae et al (2021).

*tfks only*  
In the Valdes et al simulations, the atmospheric CO2 is consistent with that of Foster et al (2017).  In these simulations, the atmospheric CO2 was modified in such a way that the model-predicted global mean surface temperatures were consistent with those of Scotese et al (2021).


# Climate variables

You can access the HadCM3L climate outputs from e.g.:

[https://www.paleo.bristol.ac.uk/ummodel/data/tfkea/climate/tfkeaa.pdclann.nc](https://www.paleo.bristol.ac.uk/ummodel/data/tfkea/climate/tfkeaa.pdclann.nc)

for the tfkea 0Ma simulation, and by analogy for the other simulations. 

The link above is formed from: ummodel/data/\[EXP\]/climate/\[EXP\]\[TYPE\]cl\[SEAS\].nc
where
* EXP is the simulation name (see above)
* TYPE can be “a.pc” (atmospheric dynamics variables), “a.pd” (atmospheric physics variables), “a.pi” or “a.pt” (land surface variables), “o.pf” (ocean seasonal variables), “o.pg” (ocean annual variables).
* SEAS can be “jan”, “feb” etc. or “djf”, “jja” etc. or “ann”.  Note that TYPE=“o.pg” only exists with SEAS=“ann”.      

In Linux, you can script the download of multiple files, see Appendix 2.


# Sediments and other derived quantities

You can access the implied geological sediments, and other derived quantities such as bioclimatic-related variables from e.g.:

[https://www.paleo.bristol.ac.uk/ummodel/data/tfkea/sed/tfkea_sed.nc](https://www.paleo.bristol.ac.uk/ummodel/data/tfkea/sed/tfkea_sed.nc)  

for the tfkea 0Ma simulation, and by analogy for the other simulations. 

The link above is formed from: ummodel/data/\[EXP\]/sed/\[EXP\]\_sed.nc

where

* EXP is the simulation name (see above)


# Boundary conditions and chronologies

You can access the spatial boundary conditions from e.g.:

[https://www.paleo.bristol.ac.uk/ummodel/data/tfkea/inidata/tfkea.qrparm.mask.nc](https://www.paleo.bristol.ac.uk/ummodel/data/tfkea/inidata/tfkea.qrparm.mask.nc)  

for the tfkea 0Ma simulation, and by analogy for the other simulations. 

The link above is formed from: ummodel/data/\[EXP\]/inidata/\[EXP\].\[BOUND\].nc

where

* EXP is the simulation name (see above)

* BOUND can be “qrparm.mask” (land-sea mask and river runoff routing), “qrparm.omask” (ocean mask and bathymetry), “qrparm.orog” (topography and gravity wave-drag parameters), “qrparm.soil” (soil parameters).

The CO2 values (in ppmv, column 3) and dates (in Ma, column 2) for each simulation are available in the following locations/files:

texy* = Table 2 of Valdes et al (2021), column “CO2 for the smooth CO2”

texp* = Table 2 of Valdes et al (2021), column “CO2 for the Foster CO2”

tfke* = [https://www.paleo.bristol.ac.uk/~ggdjl/climate_data/co2_all_03_nt.dat](https://www.paleo.bristol.ac.uk/~ggdjl/climate_data/co2_all_03_nt.dat)

tfks* = [https://www.paleo.bristol.ac.uk/~ggdjl/climate_data/co2_all_04_nt.dat](https://www.paleo.bristol.ac.uk/~ggdjl/climate_data/co2_all_04_nt.dat)

The solar constant for each simulation is available either from the output files (see variable downSol_mm_TOA in the 'pdclann' output files), or in this file:

Valdes et al (2021) simulations = [https://www.paleo.bristol.ac.uk/~ggdjl/climate_data/solar_all_tfgw.dat]

tfke*,tfks* = [https://www.paleo.bristol.ac.uk/~ggdjl/climate_data/solar_all_tfke.dat]



# References

Foster, G.L., Royer, D.L. ,and Lunt, D.J., Future climate forcing potentially without precedent in the last 420 million years. Nature Communications, 8, 14845 doi: 10.1038/ncomms14845, 2017.

Gordon, C., Cooper, C., Senior, C. A., Banks, H., Gregory, J. M., Johns, T. C., Mitchell, J. F. B., and Wood, R. A.: The simulation of SST, sea ice extents and ocean heat transports in a version of the Hadley Centre coupled model without flux adjustments, Clim. Dynam., 16, 147–168, 2000.

P. J. Irvine, L. J. Gregoire, D. J. Lunt, P. J. Valdes, An efficient method to generate a perturbed parameter ensemble of a fully coupled AOGCM without flux-adjustment. Geosci. Model Dev. 6, 1447–1462 (2013). doi:10.5194/gmd-6-1447-2013

Judd, E.J., Tierney, J.E., Lunt, D.J., Montanez, I.P., Huber, B.T., Wing, S.L., Valdes, P.J., A 485-million-year history of Earth’s surface temperature, Science, 385,eadk3705(2024). doi:10.1126/science.adk3705

J. T. Kiehl, C. A. Shields, Sensitivity of the Palaeocene-Eocene Thermal Maximum climate to cloud properties. Philos. Trans. Soc. A. 371, 20130093 (2013). doi:10.1098/rsta.2013.0093

Malanoski, C.M., Farnsworth, A., Lunt, D.J., Valdes, P.J., Saupe, E.E., Climate change is an important predictor of extinction risk on macroevolutionary timescales, Science, 383, 1130-1134, 2024. DOI:10.1126/science.adj5763

Rae, James W.B., Zhang, Yi Ge, Liu, Xiaoqing, Foster, Gavin L., Stoll, Heather M. and Whiteford, Ross D.M. (2021) Atmospheric CO2 over the past 66 million years from marine archives. Annual Review of Earth and Planetary Sciences, 49, 609-641. (doi:10.1146/annurev-earth-082420-063026).

N. Sagoo, P. Valdes, R. Flecker, L. J. Gregoire, The Early Eocene equable climate problem: Can perturbations of climate model parameters identify possible solutions? Philos. Trans. R. Soc. A. 371, 20130123 (2013). doi:10.1098/rsta.2013.0123

Scotese, CR, Song, H, Mills, BJW et al. (1 more author) (2021) Phanerozoic Paleotemperatures: The Earth’s Changing Climate during the Last 540 million years. Earth-Science Reviews, 215. 103503. ISSN 0012-8252 https://doi.org/10.1016/j.earscirev.2021.103503.

Valdes, P. J., Scotese, C. R., and Lunt, D. J.: Deep ocean temperatures through time, Clim. Past, 17, 1483–1506, https://doi.org/10.5194/cp-17-1483-2021, 2021.


# Appendix 1

Here is a table including the simulations listed above, plus some other (unpublished) simulations.  I think this is all correct, but I have not double-checked, so please use with caution (and some I haven’t checked at all yet, marked with a “?”).  There are some runs in addition to the ones listed below, but I haven’t added them yet *note to Dan – see document Scotese_runs.docx*.  In addition, many of them are not all published, and some may not be fully spun up, so please do get in contact before using them:

|                   |                    |                 |                |                     |                  |        |                       |                                                      |
| ----------------- | ------------------ | --------------- | -------------- | ------------------- | ---------------- | ------ | --------------------- | ---------------------------------------------------- |
| “puma” name \[1\] | “movie” name \[2\] | CO2             | solar constant | model version \[3\] | initialised from | run by | Benchmark publication | Other publications \[4\]                             |
|                   |                    |                 |                |                     |                  |        |                       |                                                      |
| texs,texx         | noco2,noco2a       | 1x PI           | fixed          | ?                   | ?                | PJV    |                       |                                                      |
| texv,texv1        | solar,solara       | 1x PI           | varying        | ?                   | ?                | PJV    |                       | Judd et al (2024)                                    |
| texz,texz1        | 2co2,2co2a         | 2x PI           | varying        | ?                   | ?                | PJV    |                       | Judd et al (2024), Malanoski et al (2024) [Model 4?] |
| teya,teya1        | 4co2,4co2a         | 4x PI           | varying        | ?                   | ?                | PJV    |                       | Judd et al (2024), Malanoski et al (2024) [Model 5?] |
| tex[f-j],texy     | spinup, spinupa    | Valdes “smooth” | varying        | Vn1a                | ?                | PJV    | Valdes et al (2021)   | Judd et al (2024)                                    |
| tex[p-q]          | 02                 | Foster          | varying        | Vn1b                | ?                | PJV    | Valdes et al (2021)   | Judd et al (2024), Malanoski et al (2024) [Model 3?] |
| teyd,teyd1        | 03,03a             | Foster          | varying        | Vn2a                | texp             | PJV    |                       |                                                      |
| teye              | 04                 | Foster          | varying        | Vn2b                | teyd1            | PJV    |                       | Malanoski et al (2024) [Model 2]                     |
| tfgw              | n/a                | Foster          | varying        | Vn2c                | teye             | DJL    |                       | Judd et al (2024)                                    |
| tfja              | n/a                | Foster/Rae      | varying        | Vn2d                | tfgw             | DJL    |                       |                                                      |
| tfke              | scotese_07         | Foster/Rae      | varying        | Vn2d                | tfja             | DJL    | Lunt et al (in prep)  | Judd et al (2024), Malanoski et al (2024) [Model 1]  |
| tfks              | scotese_08         | Scotese         | varying        | Vn2d                | tfke             | DJL    | Lunt et al (in prep)  | Judd et al (2024)                                    |
| xqbp              |                    | Scotese         | varying        | Vn2d                | tfks             | TYC    |                       |                                                      |

\[1\] PUMA refers to the "Providing Unified Model Access" service.  If two names are listed, then the second is initialised from the end of the first, is therefore more spun-up, and is usually the most appropriate to use.  If accessing model outputs in netcdf format using the instructions above, then this is the experiment name to use.

\[2\] access a full list of simulations, and some standard plots, from: https://www.paleo.bristol.ac.uk/ummodel/scripts/html_bridge/scotese_[movie name].html

\[3\] See Lunt et al (in prep) for what these actually mean.

\[4\] This list is far from complete!


# Appendix 2

See below for an example linux script to automate the download of files.  The following script will download all the tfke annual and djf data, for the atmospheric physics (a.pd) and ocean seasonal (o.pf) files.  Note that I think it only works with ksh.  It uses the ‘curl’ command to get the files.

```

#!/bin/ksh

# exp is the ensemble identifier

exp=tfke

# set up the loop over all simulations

expa=${exp}

expb=`sed 's/./\U&/4' <<< "${expa}"`

expc=`sed 's/./\U&/3' <<< "${expa}"`

expd=`sed 's/./\U&/3' <<< "${expb}"`

expe=`sed 's/./\U&/2' <<< "${expa}"`

expids="${expa} ${expb} ${expc} ${expd} ${expe}"

my_loop={a..z}

# loop over the simulations

for expid in ${expids} ; do

if [ "$expid" = ${expe} ] ; then

      my_loop={a..e}

fi

for ext in ${my_loop} ; do

exp=${expid}${ext}

# loop over the different file types

  for type in a.pd o.pf ; do

    for seas in ann djf ; do   

      # now finally get the file:

      filename=${exp}${type}cl${seas}.nc

      url="https://www.paleo.bristol.ac.uk/ummodel/data/${exp}/climate/${filename}"

      echo ${url}

      curl -k -o ${filename} ${url}

    done

  done

done

done

exit
```

