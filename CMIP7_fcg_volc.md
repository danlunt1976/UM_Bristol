[back to CMIP7 ancillaries](CMIP7_ancillaries.md)

## Volcanic forcing for HadCM3

### Where to access data

CMIP7 stratospheric volcanic CO$_2$ emissions and aerosol optical properies are defined here:
[https://input4mips-cvs.readthedocs.io/en/latest/dataset-overviews/stratospheric-volcanic-so2-emissions-aod/](https://input4mips-cvs.readthedocs.io/en/latest/dataset-overviews/stratospheric-volcanic-so2-emissions-aod/)  

There is a paper in review here:
[https://doi.org/10.5194/egusphere-2025-4990](https://doi.org/10.5194/egusphere-2025-4990)

The list of variables is here:
[https://docs.google.com/document/d/1blX5kv0We1BteqWzMKs0OuhazAcAonay/edit](https://docs.google.com/document/d/1blX5kv0We1BteqWzMKs0OuhazAcAonay/edit)  
They provide: ext, ssa, asy, reff, sad, vd, and nd.  We need SAOD.  In the paper, they show a plot (Figure 11) of SAOD at 550nm, which is exactly what we need!  I have emailed Thomas Aubrey at Oxford asking for the data behind that Figure.


The version number for CMIP7 production runs is CMIP_UOEXETER-CMIP-2-2-1 .  
The CMIP7 ext data can be downloaded from the ESGF, here:  
[https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&&activeFacets=%7B%22source_id%22%3A%5B%22UOEXETER-CMIP-2-2-1%22%5D%7D](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&&activeFacets=%7B%22source_id%22%3A%5B%22UOEXETER-CMIP-2-2-1%22%5D%7D)  
Filenames are:  
ext_input4MIPs_aerosolProperties_CMIP_UOEXETER-CMIP-2-2-1_gnz_175001-202312.nc (1750-2023)  
ext_input4MIPs_aerosolProperties_CMIP_UOEXETER-CMIP-2-2-1_gnz_185001-202112-clim.nc (1850-2021 climatology)  
I did this via a wget script.  I created an account on the ESGF, which gave me an OpenID and a password.  I am not sure if I had to do that step or not.  Anyway, I downloaded the wget script, and ran it on miocnee using `bash -s wget_script_2025-11-19_5-58-29.sh`.  I used the DKRZ node, as the LLN and CEDA ones didn't seem to be working.


Thomas emailed me and sent me the CMIP6 data for variable ext:  
CMIP_1850_2014_extinction_550nm_strat_only_v3.nc


### How to process data

Dan is currently writing some python script to do the regridding etc.

### How to implement the forcing into HadCM3

* Paul says that he has implemented CMIP5 volcanic forcing into HadCM3.
* This is implemented as an Aerosol Optical Depth (AOD)
* The AOD file is monthly, and consists of 4 numbers for each month - S/N Hemisphere, and high versus low latitudes.
* Paul has used this for Last Millennium work with Mike Evans.
* For CMIP5, an AOD file was produced, which Paul then regridded to this format.
* For CMIP6, the system was that groups contacted a team in Zurich, who converted that group's forcings into whatever format was needed in that model.  We never did this for CMIP6, so we cannot currently run with CMIP6 volcanic forcing.
* If we can get the CMIP7 volcanic forcings into the required AOD format with 4 numbers per year, then the existing HadCM3 code should work.
* Dan will make a CMIP7 version of the volcanic forcing file.
* Paul's email:

The job you need is xqgra

This is an all-singing prototype CMIP7 CO2 prescribed HadCM3 setup. Some of the forcings are made up and some are CMIP6. I think none are CMIP7 yet (but solar and CO2 are ready). It does not include aerosols either.

The only two (three) changes to include volcanic forcing are:

In Sub-Model Independent -> Script Inserts and Modifications  
There is a variable called VOLCANIC_FILE, and it is set to $ANCIL_ROOT/ancil/CMIP7/eVolv2k_v3_-500_1900_mon.dat  
(ANCIL_ROOT=/user/home/ggpjv/swsvalde)  
In Modifications for the model  
There is an update: $PV_UPDATES/volkr/volvar_updated_03.mod  
(where PV_UPDATES=/user/home/ggpjv/swsvalde/um_updates)  
You also need to add in:  
Sub-Model Independent -> Post Processing -> Local post processing scripts.  
~swsvalde/scripts/add_volcanic_file

I think this is correct. There was a small issue about namelist clashes so I am not 100% certain that the volcanic update will stand alone from the other updates.

The format of the volcanic file is very simple. It is a plain text file with each line being year, month, and then 4 AOD numbers, going from south to north ie.AOD(90S to 30S), AOD(30S to 0), AOD (0 to 30N) and AOD(30-90N).

To calculate the AOD, I did an area weighted average of a more latitudinally structured input from the eVolv2k_v3 dataset (the protocol of the last 2k PMIP simulation).




