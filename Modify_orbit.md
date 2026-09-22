
[Back to HadCM3_user_notes](HadCM3_user_notes.md)

# Orbit Setup in HadCM3

This document describes **three methods** for modifying Earth’s orbital parameters in the HadCM3 / UM framework.

These methods range from predefined orbital forcing files to fully manual orbital reconstruction.

---

## Method 1 — Predefined Orbital Files (`orbit_???k`)

This method uses precompiled orbital parameter files for specific time slices, such as 6 ka and 21 ka BP.

### File Location

Typical location on `puma2`:

```text
~swsvalde/um_updates/orbit_???k
```

These files directly modify the orbital parameters in the model source code.

### Add the Orbital Mod

To include an orbital file, add the corresponding Fortran modification in UMUI.

1. Open UMUI.
2. Navigate to:

```text
Model Selection
→ Sub-Model Independent
→ Compilation and Modifications
→ Modifications for the Model
```

3. Add the Fortran mod file:

```text
~swsvalde/um_updates/orbit_???k
```

4. In the **final column** of the modification table, set:

```text
Y
```

5. Compile the model and run the experiment.

---

## Method 2 — Orbital Parameter Mod for Past/Future Time Periods

This method allows orbital parameters to be specified for a particular past or future time period.

It requires both a Fortran modification and a post-processing script.

### Required Mod and Script

Add the Fortran mod:

```text
~ggdjl/um_updates/orbital_parameters-6.1_real1950o.mod
```

Add the local post-processing script:

```text
~ggdjl/um_updates/orbit_update
```

### Set Orbital Parameters

After adding the mod, the solar constant and orbital configuration can be controlled through:

```text
Sub-Model Independent
→ Script Inserts and Modifications
```

The main parameters are:

| Parameter    | Description                             |
| ------------ | --------------------------------------- |
| `SOLAR`      | Solar constant                          |
| `YEAR_ORBIT` | Year defining the orbital configuration |

### Example

For an orbital configuration corresponding to 6000 years BP:

```text
YEAR_ORBIT = 6000
```

The model will then use orbital parameters corresponding to approximately **6000 years BP**.

### Default Values

If not specified:

```text
SOLAR = 1365
YEAR_ORBIT = 0
```

`YEAR_ORBIT = 0` corresponds to the **1950 orbit**.

### Common Mod Variants

| Mod                                     | Description                                                                                           |
| --------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `orbital_parameters-6.1_1950.mod`       | Pre-industrial orbit set to 1950; offset = 50000; dump year 50000 represents the pre-industrial orbit |
| `orbital_parameters-6.1_50k.mod`        | Offset = 50000; pre-industrial orbit = dump year + 51950                                              |
| `orbital_parameters-6.1_real1950.mod`   | Pre-industrial year = 1950; dump year 0 corresponds to the 1950 orbit                                 |
| `orbital_parameters-6.1_real1950o.mod`  | Same as `real1950.mod`, with additional `solarorbit.dat` output                                       |
| `orbital_params-6.1_real1950_100k.mod`  | Like `orbital_parameters-6.1_1950.mod`, but with offset = 100000                                      |
| `orbital_params-6.1_real1950_100ko.mod` | Same as the 100k version, with output enabled                                                         |
| `orbital_params-6.1_real1950_99k.mod`   | Like the 1950 version, but with offset = 99000                                                        |
| `solar_orbit_real1950.mod`              | Combines the earlier orbital update variants into one framework                                       |
| `solar_orbit_real1950_ver02.mod`        | Adds variable solar constant support                                                                  |
| `solar_orbit_real1950_ver03.mod`        | Latest version; includes an orbital bug fix                                                           |

### `solar_orbit_real1950_ver03.mod`

The original insolation equation was:

```text
S(t) = S₀ * [ (1 + e²/2)(1 + e·cos(v)) / (1 - e²) ]²
```

The corrected equation is:

```text
S(t) = S₀ * [ (1 + e·cos(v)) / (1 - e²) ]²
```

---

## Method 3 — Orbital Parameter Calculation

This method calculates the HadCM3 orbital inputs from astronomical parameters:

* Eccentricity (`E`)
* Obliquity (`ε`, degrees)
* Perihelion − 180°
* Vernal equinox

The resulting HadCM3 inputs are:

| HadCM3 parameter | Meaning                               |
| ---------------- | ------------------------------------- |
| `GAMMA` (`γ`)    | Supplement of longitude of perihelion |
| `E`              | Eccentricity                          |
| `TAU0` (`τ₀`)    | Perihelion passage time               |
| `SINOBL`         | Sine of obliquity                     |

### Reference

[UM Technical Documentation — Radiation](https://www.paleo.bristol.ac.uk/~swsvalde/UM_Docs/UM_Technical_Documents/Radiation_p023.pdf)

### 3.1 Basic Definitions

#### `SINOBL`

```text
SINOBL = sin(obliquity)
```

#### Eccentricity

`E` is the orbital eccentricity, either directly specified or interpolated from Laskar (2004).

#### `GAMMA`

`GAMMA` is the supplement of the longitude of perihelion:

```text
GAMMA = π − LPH
```

or equivalently:

```text
GAMMA = PI - atan2(esinw, ecosw)
```

#### `TAU0`

`TAU0` represents the time of perihelion passage:

```text
τ₀ = DATE_VE − MEAN_ANOMALY(VE) × TropYear / (2π)
```

---

### 3.2 Laskar-style Calculation

#### Step 1 — Auxiliary Variables

```text
β  = sqrt(1 − E²)

EE1 = (0.5E + 0.125E³)(1 + β)

EE2 = −0.25E²(0.5 + β)

EE3 = 0.125E³(1/3 + β)
```

#### Step 2 — Mean Anomaly at Vernal Equinox

```text
MEAN_ANOM_VE =
GAMMA − 2 × [
    EE1 sin(GAMMA)
    + EE2 sin(2GAMMA)
    + EE3 sin(3GAMMA)
]
```

#### Step 3 — Perihelion Timing

```text
TAU0 = DATE_VE − MEAN_ANOM_VE × TropYear / (2π)
```

---

### 3.3 Normalisation

#### `TAU0` — Days

```text
while tau0 < 0:
    tau0 += DINY

while tau0 > DINY:
    tau0 -= DINY
```

#### `GAMMA` — Radians

```text
while gamma < 0:
    gamma += 2π

while gamma > 2π:
    gamma -= 2π
```

---

### 3.4 HadCM3 / UMUI Workflow

#### Step 1 — Pre-process on `puma2`

Calculate the required:

```text
GAMMA
E
TAU0
SINOBL
```

before modifying the UM configuration.

#### Step 2 — Edit `CNTLATM`

In `umui_jobs`, remove the last 8 lines:

```bash
head -n -8 CNTLATM > temp_CNTLATM.dat
mv temp_CNTLATM.dat CNTLATM
```

#### Step 3 — Add Fixed Switches

Add:

```text
L_SEC_VAR=.FALSE.,
SEC_VAR_FACTOR=1.0,
L_SEC_VAR_ONLINE=.FALSE.,
SEC_VAR_FILE=.FALSE.,
SEC_VAR_YEAR=0,
```

#### Step 4 — Add Orbital Parameters

Append:

```bash
echo "GAMMA_IN=${gamma_in},"   >> CNTLATM
echo "E_IN=${e_in},"           >> CNTLATM
echo "TAU0_IN=${tau0_in},"     >> CNTLATM
echo "SINOBL_IN=${sinobl_in}," >> CNTLATM
```

#### Step 5 — Add Final Block

Append:

```bash
echo "NOUTPUT_ORB=1," >> CNTLATM
echo "&END" >> CNTLATM
```

---

### 3.5 Final `CNTLATM` Example

A complete final block should look like:

```text
L_SEC_VAR=.FALSE.,

SEC_VAR_FACTOR=1.0,

L_SEC_VAR_ONLINE=.FALSE.,

SEC_VAR_FILE=.FALSE.,

SEC_VAR_YEAR=0,

GAMMA_IN=0.256314,

E_IN=0.043182,

TAU0_IN=0.875921,

SINOBL_IN=0.394615,

NOUTPUT_ORB=1,

&END
```

After completing the `CNTLATM` modification, compile the model and run the experiment.
