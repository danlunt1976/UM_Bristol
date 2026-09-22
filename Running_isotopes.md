
[Back to HadCM3_user_notes](HadCM3_user_notes.md)

# Running with isotopes

# Running HadCM3 with Isotopes


# HadCM3 Stable Water Isotope Experiment — Example Workflow

> **Example experiment:** `xqmxa → xqmxb`
> **Purpose:** Run a complete stable water isotope experiment and obtain the isotope output.
> **Core configuration:** `4x1`


## Step 0 — Copy the example experiments on puma2

Before starting the experiment, first log in to puma2 and copy the two example experiments:

xqmxa

xqmxb

These are the example experiments containing the stable water isotope configuration.

Copy them to your own experiment names, for example:

xqmxa → YOUR_EXP1

xqmxb → YOUR_EXP2

From this point onward, use your own experiment names when compiling, running, checking output, and restarting the experiments.

---

## Step 1 — Compile the first experiment

Compile the first experiment:

```bash
~ggpjv/swsvalde/bin/clustersubmit -q short -r bp14 -P GEOG030184 xqmxa
```

Wait about 10–20 minutes.

On `bp1`, check:

```text
/dump2hold/xqmxa/dataw
```

If the following executable exists:

```text
HadCM3BL-CNNP_M2.1Da.exec
```

the compilation is successful.

---

## Step 2 — Run the first experiment

Submit the first experiment:

```bash
~ggpjv/swsvalde/bin/clustersubmit -s y -c n -a y -r bp1 -q djl -g 4x1 -M 40 -m y -t y -P GEOG030184 xqmxa
```

After the experiment starts, check the output on `bp1`:

```text
/dump2hold/xqmxa/datam
```

Check the generated `pd` files and confirm that **STASH code 338** is present.

If STASH 338 is present, **Step 1 is successful**.

---

## Step 3 — Save the output of Step 1

Copy the two Step-1 restart files from `datam` to:

```text
/dump2hold/dumps_deeptime_djl
```

For example:

```text
xqmaxo#da000000001c1+
xqmaxa#da000000001c1+
```

These files are used as the starting dumps for the second experiment.

---

## Step 4 — Compile the second experiment

Compile the second experiment:

```bash
~ggpjv/swsvalde/bin/clustersubmit -q short -r bp14 -P GEOG030184 xqmxb
```

Wait about 10–20 minutes.

On `bp1`, check:

```text
/dump2hold/xqmxb/dataw
```

If the following executable exists:

```text
HadCM3BL-CNNP_M2.1Da.exec
```

the compilation is successful.

---

## Step 5 — Run the second experiment

Submit the second experiment:

```bash
~ggpjv/swsvalde/bin/clustersubmit -s y -c n -a y -r bp1 -q djl -g 4x1 -M 40 -m y -t y -P GEOG030184 xqmxb
```

## Step 6 — If the experiment stops unexpectedly

The experiment may stop during the later run.

If this happens, restart the experiment using:

```bash
~ggpjv/swsvalde/bin/clustersubmit -s y -c y -a y -r bp1 -q djl -g 4x1 -M 40 -m y -t y -P GEOG030184 xqmxb
```

The important difference is:

```text
-c y
```

instead of:

```text
-c n
```

This allows the experiment to continue from the previous state.

---

## Step 7 — If a theta / pressure error occurs

If the experiment encounters a **theta / pressure error**, manually move the experiment back to an earlier year using:

```bash
~ggpjv/swsvalde/bin/restart_manually xqmxb:0000:1
```

The format is:

```text
restart_manually EXPERIMENT:START_YEAR:YEARS_TO_ROLL_BACK
```

For example:

```bash
~ggpjv/swsvalde/bin/restart_manually xqkla:0000:1
```

means:

* `xqkla` = experiment name
* `0000` = starting/current year
* `1` = roll back 1 year

Only modify the experiment name and the final number according to the experiment and the number of years you want to roll back.

After manually restarting from the earlier year, resubmit:

```bash
~ggpjv/swsvalde/bin/clustersubmit -s y -c y -a y -r bp1 -q djl -g 4x1 -M 40 -m y -t y -P GEOG030184 xqmxb
```

Continue monitoring the experiment until it finishes.

---

## Step 8 — Complete the experiment

Continue the experiment until it finishes successfully.

The stable water isotope experiment is successful when the model runs to completion and the isotope output is generated.

---

# Step 9 — Isotope output and STASH codes

## 9.1 Atmospheric STASH code 338

**STASH code 338** is a 19-level `pd` field. The precipitation isotope information is stored in levels 1–12 as follows.

| Level | IDL | Field                      |
| ----: | --: | -------------------------- |
|     1 |   0 | Large-scale rain 16O       |
|     2 |   1 | Large-scale rain 18O       |
|     3 |   2 | Large-scale rain deuterium |
|     4 |   3 | Large-scale snow 16O       |
|     5 |   4 | Large-scale snow 18O       |
|     6 |   5 | Large-scale snow deuterium |
|     7 |   6 | Convective rain 16O        |
|     8 |   7 | Convective rain 18O        |
|     9 |   8 | Convective rain deuterium  |
|    10 |   9 | Convective snow 16O        |
|    11 |  10 | Convective snow 18O        |
|    12 |  11 | Convective snow deuterium  |

The remaining levels of STASH 338 are not used for the precipitation fields listed above.

---

## 9.2 Calculate δ18O, δD and d-excess

The fields in STASH 338 represent the **absolute amounts** of 16O, 18O and deuterium. Calculate the isotope composition using the corresponding 16O field.

### δ18O

```text
δ18O = ((18O / 16O) − 2005.2E−6) / 2005.2E−9
```

Example for large-scale rain:

```python
d18o_in_large_scale_rain = (
    (stash_code_338(lev2) / stash_code_338(lev1))
    - 2005.2E-6
) / 2005.2E-9
```

### δD

```text
δD = ((D / 16O) − 155.76E−6) / 155.76E−9
```

### d-excess

```text
d-excess = δD − 8 × δ18O
```

Example for total convective precipitation:

```python
dD_in_convective_precipitation = (
    (
        (stash_code_338(lev11) + stash_code_338(lev8))
        / (stash_code_338(lev10) + stash_code_338(lev7))
    )
    - 155.76E-6
) / 155.76E-9
```

> **Important:** When combining different precipitation components, combine the isotope amounts first and then calculate the isotope ratio. Do not directly average δ18O or δD values from different components.

---

## 9.3 Other isotope-related STASH codes

| STASH | Field                                                  |
| ----: | ------------------------------------------------------ |
|   499 | Sea surface deuterium after timestep                   |
|   500 | Soil 18O content in a layer                            |
|   501 | Canopy 18O on non-ice tiles                            |
|   502 | Soil frozen 18O content in a layer                     |
|   504 | Soil moisture 18O content after timestep               |
|   480 | Soil deuterium content in a layer                      |
|   481 | Canopy deuterium on non-ice tiles                      |
|   482 | Soil frozen deuterium in a layer                       |
|   483 | Deuterium snow amount after timestep                   |
|   484 | Soil moisture deuterium content after timestep         |
|   485 | Sea ice depth deuterium                                |
|   322 | 18O in cloud liquid water, 19 levels                   |
|   323 | 18O in cloud frozen water, 19 levels                   |
|   325 | Deuterium in cloud liquid water, 19 levels             |
|   326 | Deuterium in cloud frozen water, 19 levels             |
|   339 | 16O in cloud liquid water, 19 levels                   |
|   340 | 18O in cloud frozen water, 19 levels                   |
|  8240 | Subsurface runoff 18O                                  |
|  8241 | Subsurface runoff deuterium                            |
|  8242 | Surface runoff 18O                                     |
|  8243 | Surface runoff deuterium                               |
| 4231* | Large-scale rain 18O rate                              |
| 4232* | Large-scale snow 18O rate                              |
| 4233* | Large-scale rain deuterium rate                        |
| 4234* | Large-scale snow deuterium rate                        |
| 5258* | Atmospheric 18O increment from convection scheme       |
| 5259* | Atmospheric deuterium increment from convection scheme |
| 5260* | Convective 18O rainfall rate                           |
| 5261* | Convective 18O snowfall rate                           |
| 5262* | Convective deuterium rainfall rate                     |
| 5263* | Convective deuterium snowfall rate                     |

* These fields should work according to the isotope configuration, but they have not been systematically checked and may contain errors.

## Step 10 — Change the experiment to another geological age

Once the stable water isotope experiment has been successfully established, the same experiment can be adapted to another geological age.

---

### 10.1 `SOLAR_AGE`

**Find the geological age on `puma2`:**

```bash
~ggdjl/scotese/co2_all_04_nt.dat
```

The **second column** gives the geological age.

For example:

```text
136.4
```

**Modify in the copied experiment on `puma2`:**

```text
Model Selection
→ Sub-Model Independent
→ Script Inserts and Modifications
```

Change:

```text
SOLAR_AGE 154.7 Ma
```

to:

```text
SOLAR_AGE 136.4 Ma
```

---

### 10.2 `MY_ANCIL`

**Find on `bp1`:**

```bash
~ggpjv/ancil/scotese/
```

Select the directory corresponding to the target age.

Example:

```text
136.4 Ma → 136_4_1deg
```

**Modify in the copied experiment on `puma2`:**

```text
Model Selection
→ Sub-Model Independent
→ File & Directory Naming. Time Convention & Envirmnt Vars.
```

Change:

```text
MY_ANCIL ~ggpjv/ancil/scotese/000_0_1deg
```

to:

```text
MY_ANCIL ~ggpjv/ancil/scotese/136_4_1deg
```


### 10.3 Number of Land Points

**Find on `puma2`:**

```bash
~ggdjl/scotese/landfrac_nt.dat
```

For the target geological age, use the **final column**.

For example, for **136.4 Ma**:

```text
2515
```

**Modify in the copied experiment on `puma2`:**

```text
Model Selection
→ Atmosphere
→ Model Resolution and Domain
→ Horizontal
```

Change:

```text
Number of Land Points = 2014
```

to:

```text
Number of Land Points = 2515
```


### 10.4 CO2

**Find on `puma2`:**

```bash
~ggdjl/scotese/co2_all_04_nt.dat
```

For the selected geological age, use the **final column**.

For the 136.4 Ma example:

```text
CO2 = 1.07774e-03
```

**Modify in the copied experiment on `puma2`:**

```text
Model Selection
→ Atmosphere
→ Scientific Parameters and Sections
→ General physics Constants
```

Change:

```text
CO2 Mass Mixing Ratio for whole run
= 1.61929e-03
```

to:

```text
CO2 Mass Mixing Ratio for whole run
= 1.07774e-03
```

---

### 10.5 Atmosphere and Ocean Start Dumps

The restart simulations are arranged at approximately 5 Ma intervals, starting from the youngest simulation. The simulation names follow this sequence:

| Geological age | Name        |
| -------------- | ----------- |
| 0–125 Ma       | `tfks[a–z]` |
| 130–255 Ma     | `tfkS[a–z]` |
| 260–385 Ma     | `tfKs[a–z]` |
| 390–515 Ma     | `tfKS[a–z]` |
| 520–540 Ma     | `tFks[a–e]` |

For example:

```text
102.6 Ma → 100 Ma simulation → tfksu
541.0 Ma → outside this sequence
```

The corresponding restart files are located on **`bp1`**:

```bash
~ggdjl/dump2hold/dumps_deeptime_djl/tfks
```

For the **136.4 Ma** example, the corresponding restart files are:

```text
tfkSba#da000003000c1+
tfkSbo#da000003000c1+
```

Copy these files to your own:

```bash
~userid/dump2hold/dumps_deeptime_djl/
```

Then use them as the **Atmosphere Start Dump** and **Ocean Start Dump** in the copied experiment

**Modify in the copied experiment on `puma2`:**

Atmosphere:

```text
Model Selection
→ Atmosphere
→ Ancillary and input data files
→ Start dump
```

Set:

```text
tfkSba#da000003000c1+
```

Ocean:

```text
Model Selection
→ Ocean GCM
→ Input Files
→ Start dump
```

Set:

```text
tfkSbo#da000003000c1+
```


### 10.6 Number of Islands

**Find on `puma2`:**

```bash
~ggdjl/scotese/islands
```

The `teye*` files contain the island information.

The relevant values are:

| Value       | Meaning                                 |
| ----------- | --------------------------------------- |
| 1st         | Number of islands                       |
| 2nd         | Maximum number of segments in an island |
| 3rd         | Total number of island segments         |
| 4th / final | Ignore                                  |

For the 136.4 Ma example:

```text
Number of Islands = 2
Total number of island segments = 3
```

**Modify in the copied experiment on `bp1`:**

```text
Model Selection
→ Ocean GCM
→ Model Resolution and Domain
→ Vertical
```

Change:

```text
Total number of island segments = 11
Number of Islands = 9
```

to:

```text
Total number of island segments = 3
Number of Islands = 2
```

---



### 10.7 `GLOBAL_SALINITY`

Set `GLOBAL_SALINITY` according to the number of permanent ice sheets:

| Ice-sheet condition  | `GLOBAL_SALINITY` |
| -------------------- | ----------------: |
| No ice sheet         |           `34.23` |
| One polar ice sheet  |           `34.63` |
| Two polar ice sheets |           `34.84` |

Modify `GLOBAL_SALINITY` in the copied experiment according to the ice-sheet condition of the selected geological age.

---


