[Back to HadCM3 for CMIP7](HadCM3_CMIP7.md)

# This page documents bug fixes and/or model modifications for CMIP7.

1. This fixes the abilityto read in time-varying land ancillary files without double-expanding them to land points.
   
   The module for this bug:
   `/user/home/tw23150/mods/disturb_grid_fix.mf77`

2. Emission-driven runs use emission historical data rather than CO<sub>2</sub> concentrations. Primary producers are important contributors to uptake CO<sub>2</sub> and export O<sub>2</sub>. It seems that when terrestrial PFTs absorbs atmospheric CO<sub>2</sub>, they mistakenly absorb Carbon rather than Carbon Dioxide (molar mass of 12 relative to 44 g/mol). This resulted potentially too much uptake for the tertestrial system.
   
   This is a fix for emissions runs to pass the land flux to the atmosphere CO2 in the correct units:
   `/user/home/tw23150/mods/acn1f406`
   
3. Replace any mod called "mod1702" with `/user/home/tw23150/mods/mod1702_cdj_2024.mf77`. This ensures proper treatment of the land-use/disturbance field as a disturbed area and not a disturbance rate.

