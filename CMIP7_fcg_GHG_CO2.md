[back to CMIP7 ancillaries](CMIP7_ancillaries.md)

## Contents
- [Contents](#contents)
- [1. GHG forcings for HadCM3 (inc CO2 concs)](#1-ghg-forcings-for-hadcm3-inc-co2-concs)
  - [1.1 Where to access data](#11-where-to-access-data)
  - [1.2 How to process data](#12-how-to-process-data)
  - [1.3 How to implement the forcing into HadCM3](#13-how-to-implement-the-forcing-into-hadcm3)
- [2. CO2 emissions for HadCM3](#2-co2-emissions-for-hadcm3)
  - [2.1 Where to access data](#21-where-to-access-data)
  - [2.2 How to process data](#22-how-to-process-data)
  - [2.3 How to implement the forcing into HadCM3](#23-how-to-implement-the-forcing-into-hadcm3)
- [3. Combining multiple forcings](#3-combining-multiple-forcings)
  - [emissions + solar forcing](#emissions--solar-forcing)
    - [xqchi + xqcpa](#xqchi--xqcpa)
  - [emissions + GHGs conc](#emissions--ghgs-conc)
  - [emissions + solar + land-use](#emissions--solar--land-use)
    - [xqchz + xqchj](#xqchz--xqchj)

## 1. GHG forcings for HadCM3 (inc CO<sub>2</sub> concs)

For testing purposes, we used CMIP6 GHGs forcings. CMIP7 forcings are becoming available recently, which would also be documented.

### 1.1 Where to access data

<!-- info here where to find CMIP GHG data -->
1. CMIP6
   
   CMIP6 forcings are available for many model groups, here is the [general instructions for model groups](https://pcmdi.llnl.gov/CMIP6/Guide/modelers.html). Forcings data is kept centrally in an activity called `input4mips`. There is a long [document with details](https://docs.google.com/document/d/1pU9IiJvPJwRvIgVaSDdJ4O0Jeorv_2ekEtted34K9cA/edit?tab=t.0), and here is the [database](https://aims2.llnl.gov/search/input4MIPs).

   It might take a while to familiarise yourself with this database, as this is the combined efforts from different groups, and, there are a lot of forcings. To search for a variable, we could choose an option under `Classifications` tab in the menu on the left, and then go to `variable ID`. You could do free random exploration if you are free, but for downloading, you might want to know exactly what forcings to get in advance (follow the instructions above). For example, if `methane` is the target, then probably 'mole_fraction_of_CH4_in_air' is bettern than 'CH<sub>4</sub>'.
   
   - Normally there should also be a paper documenting a particular forcing, in that case there should be other more friendly options available elsewhere. If not, you have to get a wget script attached to searched results, and run the scripts to download data – simply cd to the directory where you downloaded the wget script, and run with `bash ./wget_example_script`, or you might want to add execute permission first, `chmod +x wget_example_script`, and then run with `./wget_example_script`.

   - For GHGs, there is another source where you could have [an overview](https://greenhousegases.science.unimelb.edu.au/#!/view).

   - Finally, here is the [paper for GHGs](https://gmd.copernicus.org/preprints/gmd-2016-169/gmd-2016-169.pdf). Data could be downloaded from the supplimentary.

> [!TIP]
> Sometimes the script could fail because you do not have authrisation or certificates. This used to be quite important, but recently for most data, you can skip those by adding '-s' after the bash script, i.e., `$./wget_example_script -s`.


2. CMIP7
   
   We do not need CMIP7 concentrations as we use emissions. But for those interested, there is a [comparison](https://github.com/climate-resource/CMIP6-vs-CMIP7-GHG-Concentrations/tree/main) between CMIP6 and CMIP7 concentrations.

   In general, the differences are small, but a max radiative forcing of 0.05 W/m<sup>2</sup> is estimated.

[back to Contents](#contents)

### 1.2 How to process data

<!-- info here how to process the CMIP data into the right format - whether it needs to be ancillary files, text files etc, which categroies to use, units required etc -->

Following the methods documented above, we should get some csv or excel data containing GHGs concs and CO<sub>2</sub> concs in different formats – temporally, they could be annual mean, monthly mean, and spatially, hemispheric mean, global mean. As in the model, atmospheric circulation is rather quick, it does not matter much if we are targeting at the GMST changes with time. We only need global annual mean data.

However, these data are not directly useable as they are normally given in ppmv (for CO<sub>2</sub>) while models require their Mass Mixing Ratio (MMR). Here is a summary of units for common species.

| Species | CO<sub>2</sub> | CH<sub>4</sub> | N<sub>2</sub>O | *CFC-12-eq** | *HFC-134a-eq** |
| :-----: | :------------: | :------------: | :------------: | :----------: | :------------: |
|  Units  |      ppmv      |      ppbv      |      ppbv      |     pptv     |      pptv      |

To convert, e.g. ppmv to MMR is straightforward. For CO<sub>2</sub>, suppose the conc is C ppmv, and we know the molar mass of CO<sub>2</sub> is 44 g/mol, while the average molar mass of air is 28.97 g/mol, we can then have,
> $MMR(CO_2) = C * \frac{M(CO_2)}{M(air)} \times 10^{-6}$

And similarly for other forcings. Scripts for processing could be found [here](https://github.com/Climateyousheng/cmip7/tree/main/scripts).

[back to Contents](#contents)

### 1.3 How to implement the forcing into HadCM3

Greenhouse gas concentrations are included in HadCM3 via a umui panel, or can be hand-edited directly after the job is processed. The former is easier to track and copy. The latter is easier if there are many data points.

These instructions apply to all well-mixed GHGs, which in HadCM3 are:
- CO<sub>2</sub>
- CH<sub>4</sub>
- N<sub>2</sub>O
- various halogneated CFC/HFC species

There are two problems when implementing all these forcings to HadCM3(L). 
 - Firstly, for a transient run, it will be accurate to input these forcings as annual mean year by year. 
> In the umui panel, under `Model Selection`>`Atmosphere`>`Scientific Parameters and Sections`>`Spec of trace gases and sulphate loading`, choose `Gen 2-stream LW rad absorption by CFC12`. For example, we can see there are 3 methods to define specification of CFC12 absorption, either exclude it, or include using a constant value or include using the complex method of specification. We choose complex method. And then there come two method, either linear interpolation of exponential increase. The latter is useful when we want to explore e.g., 1% CO<sub>2</sub> scenario, the former is used here as we want to define several turning points and interpolate linearly (at most 50 years to define). As this is for test, we think it would be reasonable to define the time series every 30 years from 1850 to 2014 – the year 1850, 1880, 1910, 1940, 1970, 2000 and 2014. 
 - Secondly, there are so many CFC/HFC species (40 gases in CMIP6 if you'd like to know) which would not be "possible" to input one by one. 

In addition to this, normally three equivalent concs are given, 'HFC-134a-eq','CFC-12-eq', and 'CFC-11-eq' which provide radiative efficiency weighted sums of a group of species, details could be found [here](https://docs.google.com/document/d/1pU9IiJvPJwRvIgVaSDdJ4O0Jeorv_2ekEtted34K9cA/edit?tab=t.0).

Thus three options are given for modelers:

- Option 1: Implement all 43 greenhouse gases.
- Option 2: Implement the four most important GHGs, namely CO<sub>2</sub>, CH<sub>4</sub>, N<sub>2</sub>O, CFC-12, and summarize the effect of all other 39 gases with CFC-11-eq.
- Option 3: Implement the three most important GHGs, namely CO<sub>2</sub>, CH<sub>4</sub>, N<sub>2</sub>O, and summarize the radiative effect of the ozone depleting substances in a CFC-12-eq conc, and the radiative effect of all other fluorinated gases in a HFC-134a-eq conc.

We chose Option 3 by default. Detailed concs are listed below:

| year\GHGs | CO<sub>2</sub> ($10^{-4}$) | CH<sub>4</sub> ($10^{-7}$) | N<sub>2</sub>O ($10^{-7}$) | CFC-12-eq ($10^{-10}$) | HFC-134a-eq ($10^{-10}$) |
| :-------: | :------------------------: | :------------------------: | :------------------------: | :--------------------: | :----------------------: |
|   1850    |           4.318            |           4.475            |           4.148            |         0.8958         |          0.6746          |
|   1880    |           4.397            |           4.810            |           4.212            |         0.8958         |          0.6746          |
|   1910    |           4.547            |           5.397            |           4.289            |         0.8958         |          0.6758          |
|   1940    |           4.729            |           6.202            |           4.370            |         1.345          |          0.7203          |
|   1970    |           4.933            |           7.813            |           4.498            |         13.78          |          1.020           |
|   2000    |           5.606            |           9.844            |           4.797            |         57.02          |          3.681           |
|   2014    |           6.038            |           10.014           |           4.967            |         56.93          |          9.054           |

More details of HadCM3 test runs on GHGs could be found here, [section xqchc](https://github.com/Climateyousheng/cmip7/blob/main/HadCM3/expts_descriptions.md)

[back to Contents](#contents)

## 2. CO<sub>2</sub> emissions for HadCM3

1. CO<sub>2</sub> concentrations
   
   Similar to other GHGs, CO<sub>2</sub> concentrations could also be found in the supplimentary (csv file). We could get the annual data from the csv file.

2. **CO<sub>2</sub> emissions**
   
   For testing purpose, we've used old version of emission data, including **SRES A2** scenario and **CMIP6** scenario (which might be a high scenario as indicated by the AMOC decline (~35%) at the end of this century).

### 2.1 Where to access data

Historical CO<sub>2</sub> concs are included in the GHGs data as indicated above. CO<sub>2</sub> emissions are separately stored. To access, go to [ESGF](https://aims2.llnl.gov/search?project=input4MIPs&versionType=all&&activeFacets=%7B%22source_id%22%3A%5B%22CEDS-CMIP-2025-03-18%22%2C%22CEDS-CMIP-2025-03-18-supplemental%22%5D%7D), in the `Classifications` filter, click `Variable ID`, select `CO2_em_anthro` and `CO2_em_AIR_anthro`, respectively, and download the data. 

Also, supplimentary to these, `CO2_em_SOLID_BIOFUEL_anthro` records solid biofuel (from biomass and biofuel combustion in households and some industrial settings – such as wood, dung, or charcoal burning for cooking or heating) separately, this should not be used to avoid double counting. This is separated because, 1), it has similar emission factors (lots of black carbon, CO, organics) to natural biomass burning (e.g. forest fires), and 2) seasonality and spatial patterns distinct from fossil fuel use, and 3) it would be easier to compare/combine this with biomass burning datasets like GFED or FINN. 

For more details of how the Community Emissions Data System (CEDS) produced emissions data, refer to [Hoesly et al., 2018](https://gmd.copernicus.org/articles/11/369/2018/gmd-11-369-2018.pdf#page=25.19). For proper config of aerosols and reactive gases in climate models, refer to  [Lamarque et al., 2010](https://acp.copernicus.org/articles/10/7017/2010/).

[back to Contents](#contents)

### 2.2 How to process data

Emissions are provided at monthly resolution, on a 0.5 degrer grid, with 50-years per data file. Files are in netcdf4 v4 (HDFv5) format with CF-compliant and ESGF-compliant metadata.

[back to Contents](#contents)

### 2.3 How to implement the forcing into HadCM3

More details of HadCM3 test runs on CO<sub>2</sub> could be found here, [See section xqchd](https://github.com/Climateyousheng/cmip7/blob/main/HadCM3/expts_descriptions.md).

> [!NOTE]
> - for some uses we want HadCM3 to be "emissions driven" for CO<sub>2</sub>, and so will use CO<sub>2</sub> emissions ancialllries and the interactive carbon cycle. [See section xqche, xqchf, xqcht](https://github.com/Climateyousheng/cmip7/blob/main/HadCM3/expts_descriptions.md)
> - some forcings are given in very granular (H)(C)FC species - these can often be lumped together into CFC-equivalents. See, e.g., [Jones et al HadGEM2 documentation, sec 3.3](https://gmd.copernicus.org/articles/4/543/2011/gmd-4-543-2011.html)

[back to Contents](#contents)

## 3. Combining multiple forcings

### emissions + solar forcing

#### xqchi + xqcpa

Since they use quite divergent basic configs (e.g., the latter use a higher resolution ocean model, thus scientific parameters are massively different). The diff file sits in `bc4:~nd20983/umui_jobs/diff.xqchi.xqcpa`, but this is difficult to deploy. Alternatively, we had a look at the difference between `tdaag` (parent of `xqcpa`), and `xqcpa`.

`diff.tdaag.xqcpa`
```
Job tdaag Title 2022-10-14: HadCM3M21D: Pre-Industrial: Reduced STASH
Job xqcpa Title copy from tdaag. Change TSI as CMIP6 recommendation
Difference in window subindep_ScriptMod
 -> Model Selection
   -> Sub-Model Independent
     -> Script Inserts and Modifications
Differences in Table Defined Environment Variables
 8c8,13
<  SOLAR 1365.0
---
>  SOLAR 1361.0
>  L_SEC_VAR .TRUE.
>  L_SOLAR_SPEC .TRUE.
>  SOLAR_FILE /home/mf22281/um_updates/varying_TSI_CMIP6.dat
>  ORB_REAL_YEAR 0
>  ORB_OFFSET_YEAR 0








Difference in window subindep_Runlen
 -> Model Selection
   -> Sub-Model Independent
     -> Start Date and Run Length Options
Entry box: Years
 Job tdaag: Entry is set to '100'
 Job xqcpa: Entry is set to '450'

Difference in window subindep_Compile_Mods
 -> Model Selection
   -> Sub-Model Independent
     -> Compilation and Modifications
       -> Modifications for the model
Differences in Table Fortran mods
 75c75
<  $PV_UPDATES/solar_orbit_real1950.mod Y
---
>  $PV_UPDATES/solar_orbit_real1950_ver03.mod Y
```

And these differences were merged to `xqchz`, except for the running length, we keep it as from '1750–2014', i.e., 265 model years.

Though new exec was created, we got problems running it — no fatal error could be spotted. Error code is 29:

> forrtl: severe (29): file not found, unit 615, file /mnt/storage/private/bridge/um_output/nd20983/xqchz/datam/fort.615

After diagonosing, we found that the pathname of solar forcing file is not complete. `/home/mf22281/um_updates/varying_TSI_CMIP6.dat` was used in the original `xqcpa`, while this failed to be converted into `/user/home/mf22281/um_updates/varying_TSI_CMIP6.dat` on bc4.

We manually edited `SCRIPT` and `CNTLATM`,

In `SCRIPT`: SOLAR_VAR_FILE='/user/home/mf22281/um_updates/varying_TSI_CMIP6.dat'

In `CNTLATM`: SOLAR_FILE='/user/home/mf22281/um_updates/varying_TSI_CMIP6.dat'

And this fixed the problem now.



[back to Contents](#contents)

### emissions + GHGs conc


[back to Contents](#contents)

### emissions + solar + land-use

#### xqchz + xqchj

Based on xqchz, we made several changes following xqchj (copy from xqcni), expt is `xqchy`.

1. environment: MY_VEG_DIST=$HOME/../glxaf/ancil/hyde_veg_dist

```
Difference in window subindep_FileDir
 -> Model Selection
   -> Sub-Model Independent
     -> File & Directory Naming. Time Convention & Envirmnt Vars.
Differences in Table Defined Environment Variables for Directories
 5c5
<  MY_DUMPS $HOME/../tw23150/dumps
---
>  MY_DUMPS $HOME/dumps
15a16
>  MY_VEG_DIST $HOME/ancil/hyde_veg_dist
```

2. model mods: see changes in parenthesis

```
Difference in window subindep_Compile_Mods
 -> Model Selection
   -> Sub-Model Independent
     -> Compilation and Modifications
       -> Modifications for the model
Differences in Table Fortran mods
 20a21,22
>  /user/home/ggpjv/um_updates/export_production Y
>  /user/home/ggpjv/um_updates/remin_temp_depend_05a Y
67c69
<  $PV_UPDATES/mods/vn4.5/hadam3/mod1702 Y            (removed)
---
>  /user/home/tw23150/mods/mod1702_cdj_2024.mf77 Y    (added)
87,89d88
<  /user/home/ggpjv/um_updates/export_production Y
<  /user/home/ggpjv/um_updates/remin_temp_depend_05a Y
<  /user/home/tw23150/mods/acn1f406 Y
90a90
>  /user/home/tw23150/mods/disturb_grid_fix.mf77 Y    (added)
```

3. atmos ancil: use xqchj config

```
Difference in window atmos_InFiles_PAncil_Disturb
 -> Model Selection
   -> Atmosphere
     -> Ancillary and input data files
       -> Climatologies & potential climatologies
         -> Vegetation Distribution: Disturbance.
Radio button: Disturbed fraction of vegetation to be:
 Job xqchi: Entry is set to 'Configured'
 Job xqchj: Entry is set to 'Updated from ancil'
Entry box: and file name
 Job xqchi: Entry is set to 'qrfrac.disturb.H3Bris.anc'
 Job xqchj: Entry is set to 'Hyde_veg_dist_mod_v1_1750'
Entry box: Enter directory or Environment Variable
 Job xqchi: Entry is set to '$MY_DUMPS/ancil'
 Job xqchj: Entry is set to '/user/home/glxaf/ancil/hyde_veg_dist'
Entry box: Every
 Job xqchi: Entry is inactive
 Job xqchj: Entry is set to '1'
Radio button: Time
 Job xqchi: Entry is inactive
 Job xqchj: Entry is set to 'Years'
 ```

4. prognostic tracers (not new as we did the same with emissions run but good to kept as a reminder).

```
```

Now we still got the same filepath error seen before (forrel 615).

Here, we changed the variable for solar files to:

in SCRIPT:

`SOLAR_FILE=$HOME/../mf22281/um_updates/varying_TSI_CMIP6.dat`

in CNTLATM:

`SOLAR_VAR_FILE='$HOME/../mf22281/um_updates/varying_TSI_CMIP6.dat'`

It seems this path does not work...We have to replace it to absolute path:

in SCRIPT:

`SOLAR_FILE=/user/home/mf22281/um_updates/varying_TSI_CMIP6.dat`

in CNTLATM:

`SOLAR_VAR_FILE='/user/home/mf22281/um_updates/varying_TSI_CMIP6.dat'`


[back to Contents](#contents)
