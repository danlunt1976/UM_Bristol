[back to CMIP7 ancillaries](CMIP7_ancillaries.md)

## Volcanic forcing for HadCM3


### Where to access data

Information about how to access the CMIP7 stratospheric volcanic CO$_2$ emissions and aerosol optical properties is given here:
[https://input4mips-cvs.readthedocs.io/en/latest/dataset-overviews/stratospheric-volcanic-so2-emissions-aod/](https://input4mips-cvs.readthedocs.io/en/latest/dataset-overviews/stratospheric-volcanic-so2-emissions-aod/)  

There is a paper that describes the forcings, currently in review, here:
[https://doi.org/10.5194/egusphere-2025-4990](https://doi.org/10.5194/egusphere-2025-4990)

The list of variables that they provide is here:
[https://docs.google.com/document/d/1blX5kv0We1BteqWzMKs0OuhazAcAonay/edit](https://docs.google.com/document/d/1blX5kv0We1BteqWzMKs0OuhazAcAonay/edit)  
They provide: *ext, ssa, asy, reff, sad, vd, and nd*.  We need SAOD (stratospheric aerosol optical depth).  In the paper, they show a plot (Figure 11) a latitudinal profile of SAOD at 550nm, which is similar to what is needed by HadCM3 (see below):
 [CMIP6-7-SAOD_Aubrey.png](<Attachments/CMIP7_fcg_volc/CMIP6-7-SAOD_Aubrey.png>)

I (Dan L) emailed Thomas Aubrey at Oxford, and he confirmed that the SAOD can be calculated simply by vertically integrating the variable *ext*.

The version number for CMIP7 production runs is CMIP_UOEXETER-CMIP-2-2-1 .  
The CMIP7 *ext* data can be downloaded from the ESGF, for example here:  
[https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&&activeFacets=%7B%22source_id%22%3A%5B%22UOEXETER-CMIP-2-2-1%22%5D%7D](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&&activeFacets=%7B%22source_id%22%3A%5B%22UOEXETER-CMIP-2-2-1%22%5D%7D)  
The key file is:  
`ext_input4MIPs_aerosolProperties_CMIP_UOEXETER-CMIP-2-2-1_gnz_175001-202312.nc` (1750-2023).  I (Dan L) accessed this via a wget script.  I created an account on the ESGF, which gave me an OpenID and a password.  I am not sure if I had to do that step or not.  Anyway, I downloaded the wget script, and ran it on miocene using `bash -s wget_script_2025-11-19_5-58-29.sh`.  **I used the DKRZ node, as the LLN and CEDA ones didn't seem to work.  Actually, next time I tried this, only the LLN one worked, and I ran the wget script without the bash -s**

Thomas Aubrey also emailed me (Dan L) and sent me the CMIP6 data for variable *ext*:  
`CMIP_1850_2014_extinction_550nm_strat_only_v3.nc`


### How to process data

Paul Valdes has implemented volcanic forcing previously in HadCM3.  In this implementation, the model requires an Aerosol Optical Depth (AOD) at 550nm for each month of the simulation, and for 4 latitude bands, provided via an input file.  The format of the volcanic input file is very simple. It is a plain text file with each line being year, month, and then 4 AOD numbers, going from south to north i.e. AOD(90S to 30S), AOD(30S to 0), AOD(0 to 30N) and AOD(30N-90N).

*Last Millennium*
Paul Valdes has implemented Lat Millennium volcanic forcing into HadCM3.  To calculate the AOD, he did an area weighted average of a more latitudinally structured input from the eVolv2k_v3 dataset (the protocol of the last 2k PMIP simulation).  Paul has used this for Last Millennium work with Mike Evans.  The associated file, which has volcanic AOD at 550nm from 500BCE to 1900 CE, can be found on BC4:
`$ANCIL_ROOT/ancil/CMIP7/eVolv2k_v3_-500_1900_mon.dat`  (ANCIL_ROOT=/user/home/ggpjv/swsvalde)

*CMIP5*
Paul said that he implemented CMIP5 volcanic forcing in HadCM3, by regridding an AOD file that was provided by CMIP.  I (Dan L) don't have a record of this file or how it was produced.

*CMIP6*
For CMIP6, Paul said that the system was that groups contacted a team in Zurich, who converted that group's forcings into whatever format was needed in that model.  We did not do this for CMIP6, and haven't yet run with CMIP6 volcanic forcing.  However, as stated above, Thomas Aubrey has sent me (Dan L) the CMIP6 data for variable *ext*, from which we could calculate CMIP6 AOD.

*CMIP7*
I (Dan L) used the CMIP7 *ext* data in the `ext_input4MIPs_aerosolProperties_CMIP_UOEXETER-CMIP-2-2-1_gnz_175001-202312.nc` file above.  The 550nm data was used, and vertically integrated through each 500m deep vertical slice to create AOD, and then regridded to the required resolution, and output in the required format.  The [python code can be found here](<Attachments/CMIP7_fcg_volc/CMIP7_volcanic.ipynb>).
The first check is that we can read in the data and integrated correctly.  To do this, I produced a [plot for comparison with the AOD plot from Aubrey et al](<Attachments/CMIP7_fcg_volc/aod550_cmip7.png>).  This looks OK.  I then [converted this to the HadCM3 latitudinal resolution](<Attachments/CMIP7_fcg_volc/aod550_cmip7_hadcm3.png>).  This itself can [be compared with Paul's Last Millennium file](<Attachments/CMIP7_fcg_volc/aod550_valdes_hadcm3.png>).  This also looks sensible.  Finally, I produced a:  
* [CMIP7 volcanic file in the format required by HadCM3](<Attachments/CMIP7_fcg_volc/CMIP7_aod_550_1750_2023.dat>).      
and a 
* [CMIP7 volcanic file in the format required by HadCM3, for zero volcanic forcing](<Attachments/CMIP7_fcg_volc/CMIP7_aod_550_1750_2023_novolc.dat>). Note that a value of AOD of 1 is used for zero forcing, instead of 0, consistent with a comment in the code that says that a value of 1 should be used because 0 causes a numerical instability.      

### How to implement the forcing into HadCM3

The information below is from an email from Paul:

The job you need is xqgra

This is an all-singing prototype CMIP7 CO2 prescribed HadCM3 setup. Some of the forcings are made up and some are CMIP6. I think none are CMIP7 yet (but solar and CO2 are ready). It does not include aerosols either.

The only (three) changes to include volcanic forcing are:

(1) In Sub-Model Independent -> Script Inserts and Modifications  
There is a variable called VOLCANIC_FILE, and it is set to $ANCIL_ROOT/ancil/CMIP7/eVolv2k_v3_-500_1900_mon.dat  
(ANCIL_ROOT=/user/home/ggpjv/swsvalde)  

(2) In Modifications for the model  
There is an update: $PV_UPDATES/volkr/volvar_updated_03.mod  
(where PV_UPDATES=/user/home/ggpjv/swsvalde/um_updates)  

(3) You also need to add in:  
Sub-Model Independent -> Post Processing -> Local post processing scripts.  
~swsvalde/scripts/add_volcanic_file

I think this is correct. There was a small issue about namelist clashes so I am not 100% certain that the volcanic update will stand alone from the other updates.








