[back to CMIP7 ancillaries](CMIP7_ancillaries.md)

## Ozone forcings for HadCM3
Contact Linlin Chen for more information and files (mf22281@bristol.ac.uk, linlontouzi@outlook.com).  

Data figures could be find from: [CMIP7_Ozone.pptx](<Attachments/CMIP7_fcg_ozone/CMIP7_Ozone.pptx>)  

Process data and scripts could be found from: `Siliruan:/home/bridge/mf22281/CMIP7/CMIP7-Ozone`  

File list ready for HadCM3BL model running:  
- climatology: 
`vmro3*_185001-185012-clim_73x96x19hybrid_zonmean.nc`  
- piControl transient: 
`vmro3*_182901-184912_73x96x19hybrid_zonmean.nc`  
- historical transient: 
`vmro3*_185001-202212_73x96x19hybrid_zonmean.nc`  

### Where to access data
Data description: https://input4mips-cvs.readthedocs.io/en/latest/dataset-overviews/ozone/

Download data from: https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&activeFacets=%7B%22source_id%22%3A%22FZJ-CMIP-ozone-1-2%22%7D

This download link would direct you to CMIP7 ozone data version1.2. But if not, you can search by `source_id = FZJ-CMIP-ozone-1-2`

There are 6 datasets available with similar filenames. They have timestamp or Version belonging to 20251010 or 20251025. *In my understanding,* three of them are original datasets, the other three are replicas (Check Dataset Metadata: `replica = true or false`). Here I only downloaded original datasets. One of the three original datasets that containing 4 files is a subset of another one that holds 5 files. 

So actually there are 2 datasets useful:
1. **monthly climatology** for 185001-185012.
- dataset: input4MIPs.CMIP7.CMIP.FZJ.FZJ-CMIP-ozone-1-2.atmos.`monC`.vmro3.gn
	- file: vmro3_input4MIPs_ozone_CMIP_FZJ-CMIP-ozone-1-2_gn_**185001-185012-clim**.nc
		- metadata comment: CMIP7 pi-control ozone forcing climatology averaged over 21-year simulation with QBO signal (182901-184912) and repeating 1850 emissions
		- Data description webpage: This dataset averages over a longer simulation, essentially removing variability like the QBO. If you wish to use this forcing for your piControl, simply apply it on repeat.
- version: 20251010; replica=false; size=41.81 MB

2. **monthly transient files**, including 1 file for **piControl** (time range equal to 182901-184912) and 4 files for **historical forcing** (185001-202212). 
- dataset: input4MIPs.CMIP7.CMIP.FZJ.FZJ-CMIP-ozone-1-2.atmos.`mon`.vmro3.gn
	- file1: vmro3_input4MIPs_ozone_CMIP_FZJ-CMIP-ozone-1-2_gn_**182901-184912**.nc (for piControl)
		- The 182901-184912 file should **ONLY** use for piControl and do **NOT** include it in historical forcing. 
		- This transient piControl forcing includes QBO signal of 182901-184912, but uses average solar forcing of 185001-187012 and repeating 1850 emissions. If you wish to use this forcing for your piControl, simply apply it on repeat.
	- file2: vmro3_input4MIPs_ozone_CMIP_FZJ-CMIP-ozone-1-2_gn_**185001-189912**.nc (historical forcing)
		- CMIP7 historical ozone forcing with nudged QBO signal, historical solar forcing, and historical emissions (same for below).
	- file3:  vmro3_input4MIPs_ozone_CMIP_FZJ-CMIP-ozone-1-2_gn_**190001-194912**.nc (historical forcing)
	- file4: vmro3_input4MIPs_ozone_CMIP_FZJ-CMIP-ozone-1-2_gn_**195001-199912**.nc (historical forcing)
	- file5: vmro3_input4MIPs_ozone_CMIP_FZJ-CMIP-ozone-1-2_gn_**200001-202212**.nc (historical forcing)
- version: 20251025; replica=false; size=4.88 GB


### How to process data

#### step1: regrid to HadCM3B long/lat grid 
- target: convert to HadCM3B longitude and latitude resolution
- input file: `vmro3*.nc`
- input variable: `vmro3(time, plev=66, lat=96, lon=144)`
	- time=monthly, plev=hPa, lat=1.875°, long=2.5°
	- variable: vmro3, units = "mole mole-1" ; # volume/mole mixing ratio
	- nominal_resolution = "250 km" 
- output file: `vmro3*_73x96.nc`
- output variable: `vmro3(time, plev=66, lat=73, lon=96) `
	- time=monthly, plev=hPa, lat=2.5°, long=3.75°  
- script: `Siliruan:/home/bridge/mf22281/CMIP7/CMIP7-Ozone/regrid.sh`

**check metadata:**
`ncdump -h input.nc`

**check lat, lon, plev values**: 
`ncks -H -C -v lat,lon,plev input.nc`     
`cdo sinfo input.nc`     
`cdo showlevel input.nc`     

**Steps**: 
- define lat,lon:
`nano grid_73x96.txt`
```grid_73x96.txt
gridtype  = lonlat
xsize     = 96
ysize     = 73
xfirst    = 0
xinc      = 3.75
yfirst    = 90
yinc      = -2.5
```

- regrid
```shell
cdo -selname,vmro3 -remapbil,grid_73x96.txt input.nc output_73x96.nc
```
- vmro3 is intensive variable, so choose **bilinear** method to convert lat and lon.  

#### step2: interpolate to hybrid levels

##### Step2.1: prepare surface pressure data
In theory, surface pressure data should be the actual surface pressure on a month-by-month basis throughout the period 1850-2013. However, for simplicity, we will **use the climatological averages**. This is also better as it makes the future scenarios straightforward too.

- target: merge surface pressure data from 12 single-month files to 1 file of 12 months
- input file: `Siliruan:swsvalde/ummodel/data/obsel/climate/obsela.pdcljan.nc` (and similarly for other months)
- input variable: `p_mm_srf(t=1, surface=1, latitude=73, longitude=96)` (Pa)
- output file: `Siliruan:/home/bridge/mf22281/CMIP7/CMIP7-Ozone/ps_12mon.nc`
- output variable: `ps(time=12, lat=73, lon=96)` (Pa)
- script: `Siliruan:/home/bridge/mf22281/CMIP7/CMIP7-Ozone/merge_files.sh`
- main command: `ncrcat -O input1.nc input2.nc output.nc`

##### Step2.2: convert to hybrid levels
- target: Convert ozone vmro3(time,plev,lat,lon) from pressure levels to hybrid levels (19) using NCL `pres2hybrid_Wrap` function. At each latitude, longitude and level (lev[k]) pressures are computed using: `p(k) = A(k)*P0 + B(k)*PS`. (See [NCL: pres2hybrid](https://www.ncl.ucar.edu/Document/Functions/Built-in/pres2hybrid.shtml) for more information.)
- input file: `vmro3*_73x96.nc` 
- input variable: `vmro3(time, plev=66, lat=73, lon=96)`
- output file: `vmro3*_73x96x19hybrid.nc`
- output variable: `vmro3(time, hybrid_eta_x1000=19, lat=73, lon=96)`
- script: `Siliruan:/home/bridge/mf22281/CMIP7/CMIP7-Ozone/pres2hybrid_zonmean_vmro3.ncl`
- main command:
```ncl
vmro3_hyb = pres2hybrid_Wrap(plev, ps_full, p0, o3, A, B, intflg)
; output dims: (time,hybrid,lat,lon)
```
where,
- `plev`: based on vmro3(plev). **Convert unit** from hPa to Pa (`plev=plev*100`), then **reverse order** from bottom->top to top->bottom (`plev=plev(::-1`).
- `ps_full`: surface pressure. based on `ps(12,lat,lon)`(Pa). **Expand time dimension** from 12 month to targeted 12\*years dimension.
- `p0`=100000.0 Pa
- `o3`: vmro3
- `A`: coefficient `A=AP/p0`. `A` is model dependent. For HadCM3B,
```NCL
AP = (/ \
    0.00000000000000E+00, 0.00000000000000E+00, 0.00000000000000E+00, 0.00000000000000E+00, \
    0.47251826759436E+03, 0.24080372627472E+04, 0.58093227790796E+04, 0.94699333641095E+04, \
    0.12323530274880E+05, 0.14006976046769E+05, 0.14688062426321E+05, 0.14577724933620E+05, \
    0.13660085920729E+05, 0.11801444655940E+05, 0.88617287598797E+04, 0.55294175974212E+04, \
    0.29594332110381E+04, 0.14797166055190E+04, 0.46058805420888E+03 /)
```
**Reverse `A` to top->bottom order (`A=A(::-1`)**
  - `B`: coefficient `B`. `B`is model dependent. For HadCM3B,
```ncl
B  = (/ \
    0.99699892520659E+00, 0.97495591297058E+00, 0.93041678475353E+00, 0.86983230217049E+00, \
    0.78750330272592E+00, 0.67549398891862E+00, 0.54141001935591E+00, 0.40982251224795E+00, \
    0.29886781207532E+00, 0.21462797853660E+00, 0.15287099931014E+00, 0.10392452480327E+00, \
    0.63025956286467E-01, 0.31486806956303E-01, 0.10629490630593E-01, 0.15600687762778E-02, \
    0.00000000000000E+00, 0.00000000000000E+00, 0.00000000000000E+00 /)
```
**Reverse `B` to top->bottom order (`B=B(::-1`)**
- `intflg`=1, values set to nearest valid value

Also set vertical hybrid levels, which could be found in any ozone ancil file, e.g., `tdezc1.qrclim.ozone.nc`, `hybrid_p_x1000(hybrid_p_x1000=19)`.
For HadCM3B,
```ncl
hybrid_eta_x1000 = (/ \
    996.996, 974.867, 930.25, 869.8323, 792.2285, 699.5743, 599.5032, \
    504.5218, 422.103, 354.6977, 299.7516, 249.7017, 199.6268, \
    149.5012, 99.24676, 56.85421, 29.59433, 14.79717, 4.605881 /)
```
**Reverse `hybrid_eta_x1000` to top->bottom order (`hybrid_eta_x1000=(::-1)`)**

#### step3: calculate zonal average
- input file: `vmro3*_73x96x19hybrid.nc`
- input variable: `vmro3(time, hybrid_eta_x1000=19, lat=73, lon=96)`
- output file: `vmro3*73x96x19hybrid_zonmean.nc`
- output variable: `O3(time, hybrid_eta_x1000=19, lat=73)`
- script: `Siliruan:/home/bridge/mf22281/CMIP7/CMIP7-Ozone/pres2hybrid_zonmean_vmro3.ncl`
- main command:
```ncl
O3 = dim_avg_n_Wrap(vmro3_hyb, 3)      
; (time,hybrid_eta_x1000,lat)
```

or  use CDO:
```bash
cdo -zonmean \
  -selname,vmro3 \
 input.nc output_zonmean.nc
```


#### step4: mergetime
merge 4 historical transient files into one.
```
cdo -O mergetime \
  input_185001-189912_72x96x19hybrid_zonmean.nc \
  input_190001-194912_72x96x19hybrid_zonmean.nc \
  input_195001-199912_72x96x19hybrid_zonmean.nc \
  input_200001-202212_72x96x19hybrid_zonmean.nc \
  output_185001-202212_72x96x19hybrid_zonmean.nc
```
`mergetime` concatenates along `time` and will sort by time if needed.
script: `Siliruan:/home/bridge/mf22281/CMIP7/CMIP7-Ozone/mergetime.sh`

The original file size is too large. So prefer conversion first, and mergetime later.

### How to implement the forcing into HadCM3

<add info here how to incorporate into a model run>
