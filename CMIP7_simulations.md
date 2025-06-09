[Back to HadCM3 for CMIP7](HadCM3_CMIP7.md)

Here we give a brief summary of our experiments. We plan to have several phases of experiments.
1. Single testing phase, where the primary goal is to test the functionality of our models (to resolve different forcings) to participate in CMIP7. And as several of us are responsible for a specified forcing, we will document them in different categories.
2. Combined testing phase, where various forcings are configured together to make sure the models are working fine.
3. CMIP7 experiments phase, where we make use of CMIP7 forcings. These will be submitted.

## Single testing phase

### 1. Historical greenhouse gas concentrations

| experiment | description                           | running length | source            |
| ---------- | ------------------------------------- | -------------- | ----------------- |
| xqcha      | test run                              | /              | <- xpuoo          |
| **xqchb**  | control run                           | 1890-2090      | <- xpzab <- xpwca |
| **xqchc**  | CMIP6 GHGs                            | 1890-2090      | <- xqchb          |
| **xqchd**  | CMIP6 GHGs + CMIP6 O<sub>2</sub> conc | 1890-2090      | <- xqchc          |


### 2. Historical CO<sub>2</sub> emissions

| experiment | description                        | running length | source   |
| ---------- | ---------------------------------- | -------------- | -------- |
| xqche      | emission test                      | 1650-1850      | <- xqchb |
| xqchf      | SRESA2 emissions, with TRIFFID bug | 1750-2100      | <- xqchb |
| **xqchh**  | SRESA2 emissions, bug fixed        | 1750-2100      | <- xqchf |
| xqcht      | CMIP6 emissions, with TRIFFID bug  | 1750-2014      | <- xqchb |
| **xqchi**  | CMIP6 emissions, bug fixed         | 1750-2014      | <- xqcht |
| **TBC**    | CMIP7 emissions                    |                | <- xqchb |

### 3. Solar forcing
xqcpa: 
This job is based on a standard HadCM3B job, tdaag, whose setup is HadCM3-MOSES2.1-TRIFFID_dyn, Pre-industrial. Job xqcpa further includes CMIP6 Total Solar Irradiation data (annual mean) and run for 450 years (1850-2299).

solar file set as `BC4:/user/home/mf22281/um_updates/varying_TSI_CMIP6.dat`  

please refer to [[CMIP7_fcg_solar | Solar forcing for HadCM3]] for more information.

To be notice, other jobs related to solar forcing need to be run later, including 
1) uses monthly CMIP6 TSI data, 
2) uses CMIP6 spectrum data (different solar irradiation value for different spectrums), 
3) combine CMIP6 monthly/annual TSI and spectrum data, 
4) use CMIP7 data (?)

### 4. Volcanic forcing

### 5. Land-use forcing

| experiment | description                                             | running length | source   |
| ---------- | --------------------------------------------------------| -------------- | -------- |
| xqcna      | test dyn TRIFFID, static Land Use  (LU)                 | 1850 - 1880    | <- xqavc |
| xqcnb      | dyn and compressed LU, BUG                              | 1850 - 1880    | <- xqcna |
| xqcnc      | dyn and uncompressed LU, BUG                            | 1850 - 1880    | <- xqcna |
| xqcng      | dyn and compressed sequencial LU, new mods, BUG FIXED   | 1850 - 1880    | <- xqcnc |
| xqcnh      | dyn and uncompressed sequencial LU, new mods, BUG FIXED | 1850 - 1880    | <- xqcng |
| xqcni      | dyn and uncompressed Hyde LU, new mods, BUG FIXED       | 1850 - 1880    | <- xqcng |


### 6. Sulphur cycle/aerosol scheme

### 7. Ozone in HadCM3 and how to include CMIP forcing

## Combined testing phase

| experiment | description                  | running length | source           |
| ---------- | ---------------------------- | -------------- | ---------------- |
| **xqchz**  | emissions + solar forcing    | 1750-2014      | <- (xqchi,xqcpa) |
| **xqchy**  | emissions + solar + land-use | 1750-2014      | <- (xqchz,xqcni) |

## CMIP7 experiments phase
