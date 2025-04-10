[Back to HadCM3 for CMIP7](HadCM3_CMIP7.md)

# This page documents bug fixes and/or model modifications for CMIP7.

## 1. land use bug


## 2. Terrestrial carbon uptake

Emission-driven runs use emission historical data rather than CO<sub>2</sub> concentrations. Primary producers are important contributors to uptake CO<sub>2</sub> and export O<sub>2</sub>. It seems that when terrestrial PFTs absorbs atmospheric CO<sub>2</sub>, they mistakenly absorb Carbon rather than Carbon Dioxide (molar mass of 12 relative to 44 g/mol). This resulted potentially too much uptake for the tertestrial system.

A module could be added to fix this:
`/user/home/tw23150/mods/acn1f406`