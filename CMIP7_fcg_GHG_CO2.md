[back to CMIP7 ancillaries](CMIP7_ancillaries.md)

## GHG forcings for HadCM3

### Where to access data

<!-- info here where to find CMIP GHG data -->

### How to process data

<!-- info here how to process the CMIP data into the right format - whether it needs to be ancillary files, text files etc, which categroies to use, units required etc -->

### How to implement the forcing into HadCM3

Greenhouse gas concentrations are included in HadCM3 via a umui panel, or can be hand-edited directly after the job is processed. The former is easier to track and copy. The latter is easier if there are many data points.

These instructions apply to all well-mixed GHGs, which in HadCM3 are:
- CO<sub>2</sub>
- CH<sub>4</sub>
- N<sub>2</sub>O
- various halogneated CFC/HFC species

More details of HadCM3 test runs on GHGs could be found here, [section xqchc](https://github.com/Climateyousheng/cmip7/blob/main/HadCM3/expts_descriptions.md)

## CO<sub>2</sub> conc/emissions for HadCM3

### Where to access data

### How to process data

### How to implement the forcing into HadCM3

More details of HadCM3 test runs on CO<sub>2</sub> could be found here, [See section xqchd](https://github.com/Climateyousheng/cmip7/blob/main/HadCM3/expts_descriptions.md).

> [!NOTE]
> - for some uses we want HadCM3 to be "emissions driven" for CO<sub>2</sub>, and so will use CO<sub>2</sub> emissions ancialllries and the interactive carbon cycle. [See section xqche, xqchf, xqcht](https://github.com/Climateyousheng/cmip7/blob/main/HadCM3/expts_descriptions.md)
> - some forcing is given in very granular (H)(C)FC species - these can often be lumped together into CFC-equivalents. See, e.g., [Jones et al HadGEM2 documentation, sec 3.3](https://gmd.copernicus.org/articles/4/543/2011/gmd-4-543-2011.html)


