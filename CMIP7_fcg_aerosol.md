[back to CMIP7 ancillaries](CMIP7_ancillaries.md)

## (Sulphate) aerosol forcings for HadCM3

Aerosol forcing has many aspects. In HadCM3 we only implement sulphates (i.e. no nitrates etc). The atmospheric chemsitry scheme takes SO2 as an emission (at surface and high level) and converts it to SO4 aerosol. These can be in various size modes.

The model may then represents how these interact with:
- radiation. the so-called "direct effect" or ARI: Aerosol-radiation interaction. This is where aerosols directly intercept/absorb/scatter incoming solar radiaiton
- clouds. the so-called "indirect effect" or ACI: Aerosol-cloud interaction. This is where aerosols affect clouds and both increase their lifetime and albedo.

The sulphate scheme requires a handful of mods to make work. This is documented below. The two effects (direct/indirect) can then be turned on with logical switches:
- L_USE_SULPC_DIRECT=.TRUE.

- L_USE_SULPC_INDIRECT_SW=.TRUE.
- L_USE_SULPC_INDIRECT_LW=.TRUE.
(so the indirect can be switched on/off indiivdiually for SW/LW radiative effects)

NOTE - CURRENTLY (FEB 2026) THE INDIRECT EFFECT DOES NOT WORK - CHRIS TO WRITE UP NOTES, BUT IT SYSTEMATICALLY CAUSEES NEGATIVE THETA/PRESSURE CRASHES EVERY YEAR OR TWO DESPITE COMPILING OK.


### Where to access data

<add info here where to find CMIP aerosol data>
for now still being processed (as of 16 Feb 2026). Use the following ancils to test:
SO2 emissions (both surface and high-level):
 /user/home/tw23150/dumps/ancil/Sulphur/SO2_1850_1980

oxidants:
 $ANCIL_ROOT/ancil/preind2/sulphur/sulpc_oxidants_19_A2_1990
(where ANCIL_ROOT = /user/home/ggpjv/swsvalde)
this is a repeating file, with 12 monthly values cycled through as a climatology, so can be used for any scenario/year

### How to process data

<add info here how to process the CMIP data into the right format - whether it needs to be ancillary files, text files etc, which categroies to use, units required etc>

### How to implement the forcing into HadCM3

1. Turn on SO2 tracer - the model needs this to be able to include SO2 as a variable. Go to:
 -> Model Selection
   -> Atmosphere
     -> Model Configuration
       -> Tracers

turn on the Check box: Do you want to include tracers in the atmosphere?

then next to line 79 in the table, put a "1" next to SO2

2. turn on the treacer advection if not already. Go to:
-> Model Selection
   -> Atmosphere
     -> Scientific Parameters and Sections
       -> Section by section choices
         -> Atmospheric tracer advection
- select '<1A> Atmospheric tracer advection included'
- but keep turned off in Check box: "Run with tracer advection scheme for thetal and qt (experimental)"

3. turn on the chemsitry scheme. Go to:
-> Model Selection
   -> Atmosphere
     -> Scientific Parameters and Sections
       -> Section by section choices
         -> Chemistry
Select: Entry is set to '<1A> Chemistry included.'
then turn ON: Check box: With the Sulphur Cycle
but turn OFF: Check box: Soot modelling

ignore an error box that says it can only be used with the right boundary layer scheme - the mods below fix this.

from that panel click "SULP" to go to the next panel for sulphur cycle choices. On here select (or make sure already selected):
- Sulphur cycle included - turn on
- including surface emissions - turn on
- including high-level emissions - turn on a nd set to level 3 in the "specify level" box
- TURN OFF: natural 3D emissions, DMS and ozone
  
- DIRECT effect - turn on
- INDIRECT effect - turn OFF - this doesn't (yet) work. 

click SUR to go to ancillayr files for SO2 emissions. Enter a path and filename. Consistent with science choices you now need to set:
- surface SO2 emissions. Set to "updated", can choose a frequency. Daily or monthly is fine
- DMS emissions. Set to "not used"
- high-level SO2 emissions. Set to "updated", can choose a frequency. Daily or monthly is fine
- Ammonia emissions. Set to "not used"

back in the SULPHUR panel click on OXID to specify the oxidant ancillaries:
add a path and filename for oxidants and then select ALL the options to be updated. Again monthly is fine


--
I HAVE NOT YET LOOKED AT STASH OPTIONS OR DIAGNOSTICS - WE WILL LIKELY WANT TO TURN ON SOME MORE DIAGOSNTOCS. NEED TO REVISIT


In mods for the model, check the following are included

set environment variable: MODS_SULPC = /user/home/tw23150/mods/Sulphur
then include mods:
$MODS_SULPC/gbccf406_co2        - make sure to use this instead of $MODS_SOURCE/vn4.5/hadam3/gbccf406 - needed for inetractive CO2
$MODS_SULPC/bl_7a_fix.mod       - simple mod to set RHOKH variable
$MODS_SULPC/SUL_dens_fix.mf77   - bug fix to calculation of density
$MODS_SULPC/SO4_indirect        - technically only needed for indirect effect but can be added anyway in case indirect later turned on
$MODS_SULPC/are4f406.mf77       - makes the sulphur cycle deposition work with the tiled land surface scheme
$MODS_SULPC/sulpc_re4_5to4_4    - fix for H2O2 calcs
$MODS_SULPC/rnout3d_4.5         - fix to scavenging/rain out. don't scavenge above rainy layers

