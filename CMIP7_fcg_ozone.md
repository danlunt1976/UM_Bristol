[back to CMIP7 ancillaries](CMIP7_ancillaries.md)

## Ozone forcings for HadCM3

### Where to access data
Data description: https://input4mips-cvs.readthedocs.io/en/latest/dataset-overviews/ozone/

Download data from: https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&activeFacets=%7B%22source_id%22%3A%22FZJ-CMIP-ozone-1-2%22%7D

This download link would direct you to CMIP7 ozone data version1.2. But if not, you can search by `source_id = FZJ-CMIP-ozone-1-2`

There are 6 datasets available with similar filenames; and timestamp or Version belonging to 20251010 or 20251025.

*In my understanding,* three of them are original datasets, the other three are replicas (Check Dataset Metadata: `replica = true or false`). Here I only downloaded original datasets. One of the three original datasets that containing 4 files is a subset of another one that holds 5 files. 

So actually there are 2 datasets useful:
1. **monthly climatology** for 185001-185012.
Actually download: 
- dataset: input4MIPs.CMIP7.CMIP.FZJ.FZJ-CMIP-ozone-1-2.atmos.`monC`.vmro3.gn
	- file: vmro3_input4MIPs_ozone_CMIP_FZJ-CMIP-ozone-1-2_gn_**185001-185012-clim**.nc
		- metadata comment: CMIP7 pi-control ozone forcing climatology averaged over 21-year simulation with QBO signal (182901-184912) and repeating 1850 emissions
		- Data description webpage: This dataset averages over a longer simulation, essentially removing variability like the QBO. If you wish to use this forcing for your piControl, simply apply it on repeat.
- version: 20251010; replica=false; size=41.81 MB

2. **monthly transient files**, including 1 file for **piControl** (time range equal to 182901-184912) and 4 files for **historical forcing** (185001-202212). 
Actually download:
- dataset: input4MIPs.CMIP7.CMIP.FZJ.FZJ-CMIP-ozone-1-2.atmos.`mon`.vmro3.gn
	- file1: vmro3_input4MIPs_ozone_CMIP_FZJ-CMIP-ozone-1-2_gn_**182901-184912**.nc (for piControl)
		- The 182901-184912 file should **ONLY** use for piControl and do not include it in historical forcing. 
		- This transient piControl forcing includes QBO signal of 182901-184912, but uses average solar forcing of 185001-187012 and repeating 1850 emissions. If you wish to use this forcing for your piControl, simply apply it on repeat.
	- file2: vmro3_input4MIPs_ozone_CMIP_FZJ-CMIP-ozone-1-2_gn_**185001-189912**.nc (historical forcing)
		- CMIP7 historical ozone forcing with nudged QBO signal, historical solar forcing, and historical emissions (same for below).
	- file3:  vmro3_input4MIPs_ozone_CMIP_FZJ-CMIP-ozone-1-2_gn_**190001-194912**.nc (historical forcing)
	- file4: vmro3_input4MIPs_ozone_CMIP_FZJ-CMIP-ozone-1-2_gn_**195001-199912**.nc (historical forcing)
	- file5: vmro3_input4MIPs_ozone_CMIP_FZJ-CMIP-ozone-1-2_gn_**200001-202212**.nc (historical forcing)
- version: 20251025; replica=false; size=4.88 GB


### How to process data
#### original metadata:
- dimensions:
	- time = UNLIMITED ; 
	- plev = 66 ;  # pressure, hPa 
	- lat = 96 ; # 1.875°
	- lon = 144 ; # 2.5°
	- bnds = 2 
 - float vmro3(time, plev, lat, lon) ;
	- string vmro3:long_name = "vmro3" ;
	- string vmro3:units = "mole mole-1" ; # volume/mole mixing ratio
	- string vmro3:cell_methods = "time: mean" ;
- global attributes:
	- grid = "1p9x2p5 degree latitude x longitude" ;
	- nominal_resolution = "250 km" ;

- check lat, lon, plev values: `ncks -H -C -v lat,lon,plev input.nc`
	- lat = -90, -88.105-, -86.211, ... , 86.211, 88.105, 90
	- lon = 0, 2.5, 5, 7.5, ... , 350, 352.5, 355, 357.5 
	- plev = 1000, 925, 850, 800, 780, 750, 700, 650, 600, 500, 450, 400, 350, 300, 285, 250, 200, 170, 150, 130, 115, 100, 90, 80, 70, 60, 50, 40, 35, 30, 25, 20, 15, 10, 7, 5, 4, 3, 2, 1.5, 1, 0.7, 0.5, 0.4, 0.3, 0.2, 0.15, 0.1, 0.07, 0.05, 0.04, 0.03, 0.02, 0.015, 0.01, 0.007, 0.005, 0.004, 0.003, 0.002, 0.0015, 0.001, 0.0008, 0.0005, 0.0003, 0.0001 ;
#### convert: remap and zonmean
- target: convert to N48 resolution and then calculate zonal mean. 
- original format: 4D(time, plev=66, lat=96, lon=144) | 1.875°x2.5°
- target format: 3D(time, plev=66, lat=73, lon=0) | 2.5°x0


- One integrated step: `cdo -s zonmean -remapbil,r96x73 input.nc output_N48_zonmean.nc`
	- vmro3 is intensive variable, so choose **bilinear** method to convert lat and lon.

- OR two steps: 
1. convert horizontal resolution to N48: `cdo -s remapbil,r96x73 input.nc output_N48.nc`

output: 
	- 4D(time, plev=66, lat=72, lon=96) | 2.5°x3.75°
	- lat = -90, -87.5, -85, ..., 85, 87.5, 90 ;
	- lon = 0, 3.75, 7.5, ..., 348.75, 352.5, 356.25 ;

2. calculate zonal mean: `cdo -s zonmean input_N48.nc output_N48_zonmean.nc`

output:
	- 3D(time, plev=66, lat=73, lon=0) | 2.5°x0
	- lat = -90, -87.5, -85, ..., 85, 87.5, 90;
	- lon = 0;

#### mergetime
merge 4 historical transient files into one.
```
cdo -s mergetime \
  input_185001-189912_N48_zonmean.nc \
  input_190001-194912_N48_zonmean.nc \
  input_195001-199912_N48_zonmean.nc \
  input_200001-202212_N48_zonmean.nc \
  output_185001-202212_N48_zonmean.nc`
```
`mergetime` concatenates along `time` and will sort by time if needed.


The original file size is too large. So prefer conversion first, and mergetime later.
### How to implement the forcing into HadCM3

<add info here how to incorporate into a model run>
