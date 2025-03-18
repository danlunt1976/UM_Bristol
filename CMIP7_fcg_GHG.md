## GHG forcings for HadCM3

### Where to access data

<info here where to find CMIP GHG data>

### How to process data

<info here how to process the CMIP data into the right format - whether it needs to be ancillary files, text files etc, which categroies to use, units required etc>

### How to implement the forcing into HadCM3

Greenhouse gas concentrations are included in HadCM3 via a umui panel, or can be hand-edited directly after the job is processed. The former is easier to track and copy. The latter is easier if there are many data points.

These instructions apply to all well-mixed GHGs, which in HadCM3 are:
- CO2
- CH4
- N2O
- various halogneated CFC/HFC species

Note:
- for some uses we want HadCM3 to be "emissions driven" for CO2, and so will use CO2 emissions ancialllries and the interactive carbon cycle. See [CO2 emissions documentation](CMIP7_fcg_CO2.md)
- some forcing is given in very granular (H)(C)FC species - these can often be lumped together into CFC-equivalents. See, e.g., [Jones et al HadGEM2 documentation, sec 3.3](https://gmd.copernicus.org/articles/4/543/2011/gmd-4-543-2011.html)


