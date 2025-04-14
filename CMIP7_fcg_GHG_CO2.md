[back to CMIP7 ancillaries](CMIP7_ancillaries.md)

## 1. GHG forcings for HadCM3

For testing purposes, we used CMIP6 GHGs forcings. CMIP7 forcings are becoming available recently, which would also be documented.

### 1.1 Where to access data

<!-- info here where to find CMIP GHG data -->
1. CMIP6
   
   CMIP6 forcings are available for many model groups, here is the [general instructions for model groups](https://pcmdi.llnl.gov/CMIP6/Guide/modelers.html). Forcings data is kept centrally in an activity called `input4mips`. There is a long [document with details](https://docs.google.com/document/d/1pU9IiJvPJwRvIgVaSDdJ4O0Jeorv_2ekEtted34K9cA/edit?tab=t.0), and here is the [database](https://aims2.llnl.gov/search/input4MIPs).

   It might takes a while to familiarise yourself with this database, as this is the combined efforts from different groups, and, there are a lot of forcings. To search for a variable, we could choose an option under `Classifications` tab in the menu on the left, and then go to `variable ID`. You could do free random exploration if you are free, but for downloading, you might want to know exactly what forcings to get in advance (follow the instructions above). For example, if `methane` is the target, then probably 'mole_fraction_of_CH4_in_air' is bettern than 'CH<sub>4</sub>'.
   
   - Normally there should also be a paper documenting a particular forcing, in that case there should be other more friendly options available elsewhere. If not, you have to get a wget script attached to searched results, and run the scripts to download data.

   > [!TIP]
   > Sometimes the script could fail because you do not have authrisation or certificates. This used to be quite important, but recently for most data, you can skip those by adding '-s' after the bash script, i.e., `$./wget_example_script -s`.

   - For GHGs, there is another source where you could have [an overview](https://greenhousegases.science.unimelb.edu.au/#!/view).

   - Finally, here is the [paper for GHGs](https://gmd.copernicus.org/preprints/gmd-2016-169/gmd-2016-169.pdf). Data could be downloaded from the supplimentary.


### 1.2 How to process data

<!-- info here how to process the CMIP data into the right format - whether it needs to be ancillary files, text files etc, which categroies to use, units required etc -->

### 1.3 How to implement the forcing into HadCM3

Greenhouse gas concentrations are included in HadCM3 via a umui panel, or can be hand-edited directly after the job is processed. The former is easier to track and copy. The latter is easier if there are many data points.

These instructions apply to all well-mixed GHGs, which in HadCM3 are:
- CO<sub>2</sub>
- CH<sub>4</sub>
- N<sub>2</sub>O
- various halogneated CFC/HFC species

More details of HadCM3 test runs on GHGs could be found here, [section xqchc](https://github.com/Climateyousheng/cmip7/blob/main/HadCM3/expts_descriptions.md)

## 2. CO<sub>2</sub> conc/emissions for HadCM3

1. CO<sub>2</sub> concentrations
   
   Similar to GHGs, CO<sub>2</sub> concentrations could also be found in the supplimentary (csv file). We could get the annual data from the csv file.

2. CO<sub>2</sub> emissions
   
   For testing purpose, we've used old version of emission data, including **SRES A2** scenario and **CMIP6** scenario (which might be a high scenario as indicated by the AMOC decline (~35%) at the end of this century).

### 2.1 Where to access data

### 2.2 How to process data

### 2.3 How to implement the forcing into HadCM3

More details of HadCM3 test runs on CO<sub>2</sub> could be found here, [See section xqchd](https://github.com/Climateyousheng/cmip7/blob/main/HadCM3/expts_descriptions.md).

> [!NOTE]
> - for some uses we want HadCM3 to be "emissions driven" for CO<sub>2</sub>, and so will use CO<sub>2</sub> emissions ancialllries and the interactive carbon cycle. [See section xqche, xqchf, xqcht](https://github.com/Climateyousheng/cmip7/blob/main/HadCM3/expts_descriptions.md)
> - some forcing is given in very granular (H)(C)FC species - these can often be lumped together into CFC-equivalents. See, e.g., [Jones et al HadGEM2 documentation, sec 3.3](https://gmd.copernicus.org/articles/4/543/2011/gmd-4-543-2011.html)


