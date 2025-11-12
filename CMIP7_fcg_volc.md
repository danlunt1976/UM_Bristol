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

### How to process data

add info here how to process the CMIP data into the right format - whether it needs to be ancillary files, text files etc, which categroies to use, units required etc

### How to implement the forcing into HadCM3

* Paul says that he has implemented CMIP5 volcanic forcing into HadCM3.
* This is implemented as an Aerosol Optical Depth (AOD)
* The AOD file is monthly, and consists of 4 numbers for each month - S/N Hemisphere, and high versus low latitudes.
* Paul has used this for Last Millennium work with Mike Evans.
* For CMIP5, an AOD file was produced, which Paul then regridded to this format.
* For CMIP6, the system was that groups contacted a team in Zurich, who converted that group's forcings into whatever format was needed in that model.  We never did this for CMIP6, so we cannot currently run with CMIP6 volcanic forcing.
* If we can get the CMIP7 volcanic forcings into the required AOD format with 4 numbers per year, then the existing HadCM3 code should work.
* Dan will make a CMIP7 version of the volcanic forcing file.




