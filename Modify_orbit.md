# Modifying the Earth’s Orbit in HadCM3 / UM System

This document describes the **three official methods** for modifying Earth’s orbital parameters in the HadCM3 / UM framework.

These methods range from simple predefined forcing files to fully manual orbital reconstruction.

---

# 1. Method 1 — Predefined Orbital Files (orbit_???k)

This method uses precompiled orbital parameter files for specific time slices (e.g., 6k, 21k BP).

Typical file location in puma2:

~swsvalde/um_updates/orbit_???k

These files directly modify orbital parameters in the model source code.

To include these files, you will need to add a “mod” to the model in the UMUI. Follow the steps below:

1. Open UMUI.
2. Navigate to the following menu path:

&nbsp;Model Selection  
&nbsp;&nbsp;→ Sub-Model Independent  
&nbsp;&nbsp;&nbsp;&nbsp;→ Compilation and Modifications  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;→ Modifications for the Model

3. Add the FORTRAN mod file: ~swsvalde/um_updates/orbit_???k

4. In the **final column of the modification table**, make sure to set:**Y**

5. After completing the configuration，compile the model, and then run.

# 2. Method 2 — Using Orbital Parameter Mod for Past/Future Time Periods

You can choose a particular time period in the past or the future. To do this, you will need to add the following model modification and post-processing script.

## Required Mod and Script

Add the FORTRAN mod:

~ggdjl/um_updates/orbital_parameters-6.1_real1950o.mod


Add the local post-processing script:


~ggdjl/um_updates/orbit_update

After adding the mod, you can control the solar constant and orbital configuration via:


Sub-model Independent -> Script Inserts and Modifications


### Parameters

- `SOLAR`  
  Sets the solar constant.

- `YEAR_ORBIT`  
  Defines the orbital configuration year.

### Example

If you set:


YEAR_ORBIT = 6000

Then the model will use orbital parameters corresponding to:


6000 years BP

### Default Values

If not specified:


SOLAR = 1365
YEAR_ORBIT = 0

Note:
- `YEAR_ORBIT = 0` corresponds to **1950 orbit**.

### Common Mod Variants

1. **orbital_parameters-6.1_1950.mod**  
   - Pre-industrial orbit set to year 1950  
   - Offset: 50000  
   - Dump year 50000 represents pre-industrial orbit  

2. **orbital_parameters-6.1_50k.mod**  
   - Offset: 50000  
   - Pre-industrial orbit = dump year + 51950  

3. **orbital_parameters-6.1_real1950.mod**  
   - Pre-industrial year = 1950  
   - Dump year = 0 corresponds to 1950 orbit  

4. **orbital_parameters-6.1_real1950o.mod**  
   - Same as real1950.mod  
   - Additionally outputs `solarorbit.dat` file  

5. **orbital_params-6.1_real1950_100k.mod**  
   - Like (1) but offset = 100000  

6. **orbital_params-6.1_real1950_100ko.mod**  
   - Same as (5) but with output enabled  

7. **orbital_params-6.1_real1950_99k.mod**  
   - Like (1) but offset = 99000  

8. **solar_orbit_real1950.mod**  
   - Combines earlier orbital update variants into one framework  

9. **solar_orbit_real1950_ver02.mod**
   - adds variable solar constant support

10. **solar_orbit_real1950_ver03.mod** (recommended latest)
   - includes orbital bug fix
   - Original insolation equation was incorrect:

     ```
     S(t) = S₀ * [ (1 + e²/2)(1 + e·cos(v)) / (1 - e²) ]²
     ```

   - Correct equation is:

     ```
     S(t) = S₀ * [ (1 + e·cos(v)) / (1 - e²) ]²
     ```
# Method 3: Orbital Parameters Calculation (HadCM3)

This method derives HadCM3 orbital inputs from:

- Eccentricity (E)
- Obliquity (ε, degrees)
- Perihelion − 180°
- Vernal equinox

Target model inputs:
GAMMA (γ)
E (eccentricity)
TAU0 (τ₀)
SINOBL (sin ε)

Reference:
https://www.paleo.bristol.ac.uk/~swsvalde/UM_Docs/UM_Technical_Documents/Radiation_p023.pdf

---

## 1. Basic Definitions

### SINOBL

SINOBL = sin(obliquity)

### Eccentricity

E = eccentricity (direct input or interpolated from Laskar 2004)


---

### GAMMA (γ)
Supplement of longitude of perihelion:


GAMMA = π − LPH


or equivalently:


GAMMA = PI - atan2(esinw, ecosw)


---

### TAU0 (τ₀) — perihelion passage time

Core idea:


τ₀ = DATE_VE − MEAN_ANOMALY(VE) × TropYear / (2π)


---

## 2. Practical Laskar-style Computation

### Step 1: Auxiliary variables


β = sqrt(1 − E²)

EE1 = (0.5E + 0.125E³)(1 + β)
EE2 = −0.25E²(0.5 + β)
EE3 = 0.125E³(1/3 + β)


---

### Step 2: Mean anomaly at vernal equinox


MEAN_ANOM_VE =
GAMMA − 2 × [EE1 sin(GAMMA)
+ EE2 sin(2GAMMA)
+ EE3 sin(3GAMMA)]


---

### Step 3: Perihelion timing


TAU0 = DATE_VE − MEAN_ANOM_VE × TropYear / (2π)


---

## 3. Normalisation

### TAU0 (days)


while tau0 < 0: tau0 += DINY
while tau0 > DINY: tau0 -= DINY


### GAMMA (radians)


while gamma < 0: gamma += 2π
while gamma > 2π: gamma -= 2π

## 4. Workflow (HadCM3 / UMUI)

### Step 1: Pre-process (PUMA2)

### Step 2: Edit CNTLATM in `umui_jobs`

Remove last 8 lines:

head -n -8 CNTLATM > temp_CNTLATM.dat

mv temp_CNTLATM.dat CNTLATM

### Step 3: Add fixed switches

L_SEC_VAR=.FALSE.,

SEC_VAR_FACTOR=1.0,

L_SEC_VAR_ONLINE=.FALSE.,

SEC_VAR_FILE=.FALSE.,
SEC_VAR_YEAR=0,

### Step 4: Append orbital parameters

echo "GAMMA_IN=${gamma_in},"   >> CNTLATM

echo "E_IN=${e_in},"           >> CNTLATM

echo "TAU0_IN=${tau0_in},"     >> CNTLATM

echo "SINOBL_IN=${sinobl_in}," >> CNTLATM

### Step 5: Final block

echo "NOUTPUT_ORB=1," >> CNTLATM

echo "&END" >> CNTLATM

### 5. Final CNTLATM Example，compile the model, and then run

L_SEC_VAR=.FALSE.,

SEC_VAR_FACTOR=1.0,

L_SEC_VAR_ONLINE=.FALSE.,

L_SEC_VAR_FILE=.FALSE.,

SEC_VAR_YEAR=0,

GAMMA_IN=0.256314,

E_IN=0.043182,

TAU0_IN=0.875921,

SINOBL_IN=0.394615,

NOUTPUT_ORB=1,

&END













