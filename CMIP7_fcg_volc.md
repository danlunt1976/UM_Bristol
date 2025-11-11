[back to CMIP7 ancillaries](CMIP7_ancillaries.md)

## Volcanic forcing for HadCM3

### Where to access data

add info here where to find CMIP volcanic data

### How to process data

add info here how to process the CMIP data into the right format - whether it needs to be ancillary files, text files etc, which categroies to use, units required etc

### How to implement the forcing into HadCM3

* Paul says that he has implemented CMIP5 volcanics into HadCM3.
* This is implemented as an Aerosol Optical Depth (AOD)
* The AOD file is monthly, and consists of 4 numbers for eachmonth - S/N Hemipsher, and high versus low latitudes.
* Paul has used this for Last Millennium work with Mike Evans.
* For CMIP5, and AOD file ws produced, which Paul then regridded to this format.
* For CMIP6, the system was the groups contacted a group in Zurich, who converted that group's forcings into whatever format was needed in that model.  We never did this for CMIP6, so we cannot currently run with CMIP6 volcanics.
* If we can get the CMIP7 volcanc forcings into the required AOD format with 4 numbner per year, then the existing HadCM3 code should work.
