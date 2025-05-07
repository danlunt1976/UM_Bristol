[Back to HadCM3 for CMIP7](HadCM3_CMIP7.md)

In order to run CMIP7 simulations, HadCM3 must be able to ingest various forcings from greenhouse gases to aerosols and natural changes. These pages document where to get CMIP forcing from and how to process it for use in HadCM3.

### Contents
- [Contents](#contents)
- [Background](#background)
- [CMIP7 forcings](#cmip7-forcings)
- [HadCM3 implementation of forcings](#hadcm3-implementation-of-forcings)
- [Forcings backup on Bridge machines](#forcings-backup-on-bridge-machines)


### Background

CMIP forcing data is kept centrally in an activity called "inputs4mips".

There is a (long) document here with details from CMIP6: [CMIP6 Forcing Datasets Summary](https://docs.google.com/document/d/1pU9IiJvPJwRvIgVaSDdJ4O0Jeorv_2ekEtted34K9cA/)
and the database itself is here: [Inputs4MIPs](https://aims2.llnl.gov/search/input4MIPs)

It takes a bit of getting used to: you can search for example for a variable under "Classificaitons" tab, then "variable ID". It's probably best to know in advance exactly what you want rather than to browse. It's not very user friendly for random exploring...

As an example, if you want GHG concentrations don't look for "CH4" but for "mole_fraction_of_CH4_in_air". Though note for **CMIP7 data**, some changes are made – they've simplified the variable names, e.g., for 'mole_fraction_of_methane_in_air', 'ch4' is the new variable. A full list variable name mapping could be found here [CMIP7 GHG concs](https://input4mips-cvs.readthedocs.io/en/latest/dataset-overviews/greenhouse-gas-concentrations/).

It is strongly recommended to read the document before accessing any data. Some datasets are also available elsewhere which can provide more friendly download options. 

### CMIP7 forcings

[CMIP7 forcings home page](https://wcrp-cmip.org/cmip-phases/cmip7/cmip7-forcing-datasets/), and you can have an overview [here](https://input4mips-cvs.readthedocs.io/en/latest/dataset-overviews/).

Currently greenhouse gases are available, guide to use is [here](https://input4mips-cvs.readthedocs.io/en/latest/dataset-overviews/greenhouse-gas-concentrations/).

Forcings availability (last updated: 14th Apr 2025):
- [x] Anthropogenic short-lived climate forcer (SLCF) and CO<sub>2</sub> emissions
- [x] Open biomass burning emissions
- [x] Land use
- [x] Greenhouse gas concentrations
- [x] Stratospheric volcanic SO<sub>2</sub> emissions and aerosol optical properties
- [ ] Ozone concentrations
- [ ] Nitrogen deposition
- [x] Solar
- [ ] AMIP sst and sea-ice boundary forcing
- [ ] Population density

> [!NOTE]
> There are two categories of data for CMIP7, the `mip_era` metadata value being 'CMIP7' and 'CMIP6Plus'. 'CMIP6Plus' is used for testing, while 'CMIP7' is used in CMIP7 production simulations.


### HadCM3 implementation of forcings

The following pages provide details of how to access CMIP forcings, process them into the correct format for HadCM3, and use them in a model run.

- [Greenhosue gas concentrations](CMIP7_fcg_GHG_CO2.md)
- [CO<sub>2</sub> emissions](CMIP7_fcg_GHG_CO2.md)
- [land-use change](CMIP7_fcg_LUC.md)
- [aerosols](CMIP7_fcg_aerosol.md)
- [ozone](CMIP7_fcg_ozone.md)
- [solar](CMIP7_fcg_solar.md)
- [volcanic](CMIP7_fcg_volc.md)

As mentioned in [CMIP7_simulations](CMIP7_simulations.md), there are 3 phases we implement these forcings. Phase 1 (Single Testing Phase), we test the availability to add a single forcing; Phase 2 (Combined Testing Phase), we gradually merge various forcings; Phase 3 (CMIP7 experiments Phase), standard runs for CMIP7.

For **Phase 2**, we document the processes in [CO<sub>2</sub> emissions](CMIP7_fcg_GHG_CO2.md).


### Forcings backup on Bridge machines

As CMIP7 forcing data are provided at monthly resolution, and high spatial resolution (e.g., 0.5 degree for emissions), they are quite large and could be messy. We plan to backup these forcings (rawdata, ready-to-use ancillary files) on our machines. For long-term management, we would like to create a linux user group (i.e., for CMIP7), and everyone in the group have write permission (sometimes this could be dangerous). But this needs to be properly figured out as new machines or new systems are being updated.

Currently, members responsible for forcings are suggested to have a copy of the data in their work directory. If they need to be backup up, please email either Paul, Dan or Alex to make a copy of them. FYI, the directory sits under `oligocene:~swsvalde/public_html/CMIP7`, which could be accessed on web at [www.paleo.bristol.ac.uk/CMIP7](https://www.paleo.bristol.ac.uk/CMIP7).



