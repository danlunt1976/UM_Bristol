[Back to HadCM3_user_notes](HadCM3_user_notes.md)

# Running Paleo simulations with HadCM3

This page provides a guide to running paleo simulations with HadCM3

## Overview

In general, paleo simulations with HadCM3 will either be equilibrium simulations (in which the boundary conditions do not change with time (unless they repeat monthly, such as ozone, or SST for an atmosphere-only simulation), or transient simulations (in which the boundary conditions do change with time).  This page focusses for now on equilibrium simulations (although this may change later).  We do carry out some transient paleo simulations (e.g. of the Last Millennium), but more often we carry out equilibrium simulations.

For paleo simulations, usually we will change one or more of 5 types of boundary conditions compared with their standard preindustrial state.  The 5 types of boundary condition that we usually change are (1) solar constant, (2) orbital configuration, (3) greenhouse gas concentrations, (4) land-surface conditions, and (5) paleogeography.  (5) and (4) are connected, because if we change paleogeography (in particular land-sea mask) then we will have to also modify the land-surface conditions.  If we change (4) then we will also need to create a new atmospheric restart file, although this done automatically by the code.  If we change (5) then we will also need to create a new ocean restart file.  

## Changing solar constant


## Changing orbital configuration


## Changing greenhouse gas concentrations

The atmospheric CO$_2$ concentration is stored in the umui in Model Selection / Atmosphere / Scientific Parameters and Sections / General Physics Constants.  The CO$_2$ is given in units of kg/kg, not ppm (4.25418e-04 kg/kg = 280 ppmv).  Create a new job (by copying your control simulation), edit this value, and run.  Note that you do not need to recompile your code because CO$_2$ is stored as a runtime namelist.  
## Changing land-surface conditions  


## Changing paleogeography


## Changing restart files







