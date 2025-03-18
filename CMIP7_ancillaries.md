[Back to HadCM3 for CMIP](HadCM3_CMIP7.md)

In order to run CMIP7 simulations, HadCM3 must be able to ingest various forcings from greenhouse gases to aerosols and natural changes. These pages document where to get CMIP forcing from and how to process it for use in HadCM3.

### Background

CMIP forcing data is kept centrally in an activity called "inputs4mips".

There is a (long) document here with details from CMIP6: [CMIP6 Forcing Datasets Summary](https://docs.google.com/document/d/1pU9IiJvPJwRvIgVaSDdJ4O0Jeorv_2ekEtted34K9cA/)
and the database itself is here: [Inputs4MIPs](https://aims2.llnl.gov/search/input4MIPs)

It takes a bit of getting used to: you can search for example for a variable under "Classificaitons" tab, then "variable ID". It's probably best to know in advance exactly what you want rather than to browse. It's not very user friendly for random exploring...

As an example, if you want GHG concentrations don't look for "CH4" but for "mole_fraction_of_CH4_in_air".

It is strongly recommended to read the document before accessing any data. Some datasets are also available elsewhere which can provide more friendly download options. 

### CMIP7 forcings

[CMIP7 forcings home page](https://wcrp-cmip.org/cmip-phases/cmip7/cmip7-forcing-datasets/)

## HadCM3 implementation of forcings

The following pages provide details of how to access CMIP forcings, process them into the correct format for HadCM3, and use them in a model run.

- [Greenhosue gas concentrations](CMIP7_fcg_GHG.md)
- [CO2 emissions](CMIP7_fcg_CO2.md)
- [land-use change](CMIP7_fcg_LUC.md)
- [aerosols](CMIP7_fcg_aerosol.md)
- [ozone](CMIP7_fcg_ozone.md)
- [solar](CMIP7_fcg_solar.md)
- [volcanic](CMIP7_fcg_volc.md)



