[Back to HadCM3 for CMIP7](HadCM3_CMIP7.md)

Here we give a brief summary of our experiments. We plan to have several phases of experiments.
1. Single testing phase, where the primary goal is to test the functionality of our models (to resolve different forcings) to participate in CMIP7. And as several of us are responsible for a specified forcing, we will document them in different categories.
2. Combined testing phase, where various forcings are configured together to make sure the models are working fine.
3. CMIP7 experiments phase, where we make use of CMIP7 forcings. These will be submitted.

## Single testing phase

### 1. Historical greenhouse gas concentrations

| experiment | description                           | source            |
| ---------- | ------------------------------------- | ----------------- |
| xqcha      | test run                              | <- xpuoo          |
| **xqchb**  | control run                           | <- xpzab <- xpwca |
| **xqchc**  | CMIP6 GHGs                            | <- xqchb          |
| **xqchd**  | CMIP6 GHGs + CMIP6 O<sub>2</sub> conc | <- xqchc          |


### 2. Historical CO<sub>2</sub> emissions

| experiment | description                        | source   |
| ---------- | ---------------------------------- | -------- |
| xqche      | emission test                      | <- xqchb |
| xqchf      | SRESA2 emissions, with TRIFFID bug | <- xqchb |
| **xqchh**  | SRESA2 emissions, bug fixed        | <- xqchf |
| xqcht      | CMIP6 emissions, with TRIFFID bug  | <- xqchb |
| **xqchi**  | CMIP6 emissions, bug fixed         | <- xqcht |
| **TBC**    | CMIP7 emissions                    | <- xqchb |

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

### 6. Sulphur cycle/aerosol scheme

### 7. Ozone in HadCM3 and how to include CMIP forcing

## Combined testing phase

| experiment | description                  | source           |
| ---------- | ---------------------------- | ---------------- |
| **xqchz**  | emissions + solar forcing    | <- (xqchi,xqcpa) |
| **tbc**    | emissions + solar + land-use | <- (xqchz,xqcni) |

## CMIP7 experiments phase