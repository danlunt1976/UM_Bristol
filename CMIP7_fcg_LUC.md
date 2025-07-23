[back to CMIP7 ancillaries](CMIP7_ancillaries.md)

## Land-use/land-use change forcing for HadCM3

### Where to access data

<add info here where to find CMIP LU data>

### How to process data
The land-use should be an ancillary file, in the pp format, containing fraction of vegetation (values between 0 and 1) on each point of the land area of the model grid. If the initial land-use file is on a netcdf4 format, convert in on pp format by: 
1) Open xancil
2) Load nc file of interest
3) Choose start date, time depth and time step
4) Click on "create ancillary file"

### How to implement the forcing into HadCM3
From umui (access from PUMA2, from archer2)
1) Copy a standard HadCM3B job.
2) To define the path where the ancillary is : 
   Model Selection -> Sub - Model Independant -> File & Directory Naming
   In the table called "Defined Environment Variables for Directories", add in the column "Variable Name" MY_VEG_DIST, and the path corresponding in the other column. For example : $HOME/ancil/ancil_landuse
3) Choose the right ancillaryvfile:
   Model Selection -> Atmosphere -> Ancillary and input data files -> Climatologies & potential climatologies -> Vegetation Distribution : Disturbance
   In directory or Environment Variable, write path where ancillary is (or let  MY_VEG_DIST, if step 2) already completed). Enter file name.
   a) If ancillary is static : choose "Disturbed fraction of vegetation to be" : "Configured"
   b) If ancillary is a varying land-use : choose "Disturbed fraction of vegetation to be" : "Updated from ancil" and specify the time step corresponding to the land-use update.
4) Especially for varying land-use, do not forget to add these mods:
   Model Selection -> Sub - Model Independant -> Compilation and Modifications -> Modifications for the model
   In the Fortran mods table, add /user/home/tw23150/mods/gath_fld_co2.mf77 and /user/home/tw23150/mods/disturb_grid_fix.mf77 (Include Y).


