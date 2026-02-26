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

| experiment | description                             | running length | source   |
| ---------- | --------------------------------------- | -------------- | -------- |
| xqche      | emission test                           | 1650-1850      | <- xqchb |
| xqchf      | SRESA2 emissions, with TRIFFID bug      | 1750-2100      | <- xqchb |
| **xqchh**  | SRESA2 emissions, bug fixed             | 1750-2100      | <- xqchf |
| xqcht      | CMIP6 emissions, with TRIFFID bug       | 1750-2014      | <- xqchb |
| **xqchi**  | CMIP6 emissions, bug fixed              | 1750-2014      | <- xqcht |
| **TBC**    | CMIP7 emissions                         |                | <- xqchb |
| xqchk      | CMIP6 emissions, veg timestep bug fixed | 1750-2014      | <- xqchi |

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
| ---------- | ------------------------------------------------------- | -------------- | -------- |
| xqcna      | test dyn TRIFFID, static Land Use  (LU)                 | 1850 - 1880    | <- xqavc |
| xqcnb      | dyn and compressed LU, BUG                              | 1850 - 1880    | <- xqcna |
| xqcnc      | dyn and uncompressed LU, BUG                            | 1850 - 1880    | <- xqcna |
| xqcng      | dyn and compressed sequencial LU, new mods, BUG FIXED   | 1850 - 1880    | <- xqcnc |
| xqcnh      | dyn and uncompressed sequencial LU, new mods, BUG FIXED | 1850 - 1880    | <- xqcng |
| xqcni      | dyn and uncompressed Hyde LU, new mods, BUG FIXED       | 1850 - 1880    | <- xqcng |


### 6. Sulphur cycle/aerosol scheme

### 7. Ozone in HadCM3 and how to include CMIP forcing

## Combined testing phase

| experiment | description                                | running length | source           |
| ---------- | ------------------------------------------ | -------------- | ---------------- |
| **xqchz**  | emissions + solar forcing                  | 1750-2014      | <- (xqchi,xqcpa) |
| **xqchy**  | emissions + solar + land-use               | 1750-2014      | <- (xqchz,xqcni) |
| **xqchx**  | emissions + solar + land-use + GHGs        | 1850–2022      | <- (xqchy,xqchd) |
| **xqhug**  | aerosol run (sulphate direct effect)       | TBC            | <- xqhuc         |

### xqhug

Aerosol (sulphate) run based on the updated-mods spin-up `xqhuc`. Only the direct effect (ARI) is enabled; the indirect effect (ACI) is switched off.

- **Aerosol indirect effect crashes**

  `L_USE_SULPC_INDIRECT_SW` and `L_USE_SULPC_INDIRECT_LW` cause systematic negative theta/pressure crashes every year or two despite compiling correctly. Root cause not yet identified.

  Solution: keep indirect effect switched off for now. Only direct effect (`L_USE_SULPC_DIRECT=.TRUE.`) is used.

- **RECONA hand-edits required**

  Turning on the SO2 tracer (item 79) via the UMUI panel may not propagate correctly to the RECONA file, and the SO4 mode prognostics are absent from the start dump entirely. The correct entries are:

  ```
  ### Tracer fields ###
  &ITEMS ITEM=79,  DOMAIN=1, SOURCE=6, USER_PROG_RCONST=0.0 &END
  ### Atmos user-prognostic fields ###
  &ITEMS ITEM=101, DOMAIN=1, SOURCE=3 &END
  &ITEMS ITEM=103, DOMAIN=1, SOURCE=3 &END
  &ITEMS ITEM=104, DOMAIN=1, SOURCE=3 &END
  &ITEMS ITEM=105, DOMAIN=1, SOURCE=3 &END
  &ITEMS ITEM=106, DOMAIN=1, SOURCE=3 &END
  ```

  `ITEM=79` must use `SOURCE=6` (initialise to constant 0.0), not `SOURCE=3` — the field does not exist in the original dump and RECON will abort with `Stash code 79 not found on input file`. Items 101 and 103–106 use `SOURCE=3` (read from ancil) and must be inserted after `ITEM=222`. Use the `aero_recon` post-script to apply both fixes automatically: `~/um_updates/post_scripts_puma2/aero_recon <jobid>`.

## CMIP7 experiments phase

### Test on HadCM3

| experiment | description                                                                    | running length | source |
| ---------- | ------------------------------------------------------------------------------ | -------------- | ------ |
| **xqgtz**  | copy from xqgra, Tuning HadCM3                                                 | /              | xqgra  |
| **xqgta**  | Equilibrium TRIFFID, under preind                                              | 40             | xqgtz  |
| **xqgtb**  | Spin-up, Dynamic TRIFFID, under preind (varying solar, volcanic, and land-use) | 200            | xqgta  |
| **xqgtc**  | Spin-up, Dynamic TRIFFID, under preind (fixed solar, volcanic, and land-use)   | 165            | xqgtd  |
| **xqgtd**  | Emission-driven test, without emissions                                        | 173            | xqgtz  |
| **xqgte**  | Emission-driven test, cmip7                                                    | 173            | xqgtd  |
| **xqgth**  | copy from xqgtb, add GHGs                                                      | 173            | xqgtb  |

However, spun-up results for the carbon cycle are not satisfying. We modified some mods (mainly carbon cycle mods) and redo the spin-up.


| experiment | description                                                         | running length | source         |
| ---------- | ------------------------------------------------------------------- | -------------- | -------------- |
| **xqhua**  | updated mods, preindustrial Equilibrium TRIFFID spin-up             | 40             | xqgta          |
| **xqhuc**  | updated mods, preindustrial Dynamic TRIFFID spin-up (fixed forcing) | 200            | xqgtc          |
| xqhud      | updated mods, Emission + GHGs                                       | 5              | xqhue          |
| xqhue      | updated mods, CMIP7 Emission (calibrated based CEDS obs)            | 5              | /              |
| xqhuf      | updated mods, Emission + Vol                                        | 5              | xqhue          |
| xqhuh      | updated mods, GHGs                                                  | 5              | xqhuc          |
| xqhui      | updated mods, Test soil params to UM default, V crit off            | 5              | xqhuc          |
| xqhuj      | Eqbm run, test plant stress (off)                                   | 40             | xqhua          |
| xqhuk      | Eqbm run, test plant stress (off) and CCN (on)                      | 40             | xqhua          |
| xqhul      | CMIP7 Emission + GHGs + LU + Solar + Vol                            | 173            | xqhud          |
| xqhum      | CMIP7 all forcings (+ aerosol), debugging                           | TBC            | <- (xqhul, xqhug) |
| xqhuu      | check stash                                                         | /              | xqbtn <- xqbmg |
| xqhuz      | Tuning version of HadCM3C                                           | /              | xqhra          |

### xqhum

All-forcings run combining `xqhul` (Emission + GHGs + LU + Solar + Vol) with the sulphate aerosol scheme from `xqhug`. Currently being debugged.

> [!NOTE]
> Document bugs and fixes here as they are identified.