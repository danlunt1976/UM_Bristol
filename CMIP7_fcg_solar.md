[back to CMIP7 ancillaries](CMIP7_ancillaries.md)

## Solar forcing for HadCM3

### Where to access data
You can find introduction of solar forcing from [Homepage of SOLARIS-HEPPA](https://www.solarisheppa.kit.edu/index.php), the [CMIP7 Solar forcing](https://www.solarisheppa.kit.edu/75.php), and the paper [Funke et al., 2024](https://gmd.copernicus.org/articles/17/1217/2024/).

Data can be access from links [monthly resolution reference solar forcing](https://cloud.iaa.es/index.php/s/n7cacmRBjk5Gb8f), and [daily resolution reference solar forcing](https://cloud.iaa.es/index.php/s/nJFTPcnFwZ3smTo).


To be noticed, the CMIP7 solar forcing provides data ranging from 1850-2023 (1850-1873 for pre-industrial control; version 4.6). While CMIP6 provides data from 1850-2299 (version 3.2).

However, the link for downloading CMIP6 solar forcing data are now overwritten by the CMIP7 one. But you can access data from my previous saved file: [[solarforcing-ref-mon_input4MIPs_solar_CMIP_SOLARIS-HEPPA-3-2_gn_18500101-22991231.nc]]

### How to process data

#### Total Solar Irradiation (TSI)
The HadCM3B model requires time-varying Total Solar Irradiation (TSI) file in annual mean resolution, saving as a .dat file with two columns (`year value`), without column name.

You can get the converted annual mean **varying_TSI_CMIP6.dat** file from [[local path]] (can open with Notepad), or in `BC4:/user/home/mf22281/um_updates/`.

The file looks like this:
![[head of varying_TSI_CMIP6 file.png]]

The TSI data for CMIP6:
![[TSI_CMIP6.png]]

#### Spectrum

### How to implement the forcing into HadCM3

#### Setup a transient TSI job
Tutorial: [[Tutorial of Solar Orbit Setup_202503.docx]]

Key process:
- copy a standard HadCM3B job. 
- setup a module in PUMA2, UMUI window:
	Model Selection 
		-> sub-model independent 
			-> compilation and modification 
				-> modifications for the model 
					-> Fortran Mods table
	`$PV_UPDATES/solar_orbit_real1950.mod` | Y

> $PV_UPDATAES: `BC4:/mnt/storage/private/bridge/swsvalde/um_updates/`

- Include time-varying TSI file and turn on related options in PUMA2, UMUI window:
	Model Selection ->
		-> sub-model independent 
			-> Script inserts and modifications
				-> Defined Environment Variable
	- `L_SEC_VAR: .TRUE.`
		set orbit changing through time
	- `L_SOLAR_SPEC: .TRUE.`
		set solar spectrum changing through time
	- `ORB_REAL_YEAR: 0`
	- `ORB_OFFSET_YEAR: 0`
	- `SOLAR_FILE: /home/mf22281/um_updates/varying_TSI_CMIP6.dat` (change file path and name as you want)
![[PUMA3_set_time_varying_TSI.png]]

- save
- process
- copy job from PUMA2 to `BC4:~/umui_jobs/`

You can further check or modify the setting in
`BC4:~/umui_jobs/jobid/MODS_UM`:
![[BC4_umui_jobs_jobid_MODS_UM.png]]

`BC4:~/umui_jobs/jobid/CNTLATM`:
![[BC4_umui_jobs_jobid_CNTLATM.png]]

`BC4:~/umui_jobs/jobid/SCRIPT` :
![[BC4_umui_jobs_jobid_SCRIPT.png]]

## Test with CMIP6 TSI
### Setting
- xqcpz
	A copy of the standard HadCM3B job, tdaag, which is HadCM3-MOSES2.1-TRIFFID_dyn, Pre-industrial.
	re-run from year 1850 to 2299.
- xqcpa
	solar file set as `BC4:/user/home/mf22281/um_updates/varying_TSI_CMIP6.dat`
	running from year 1850 to 2299.
- xqcpb
	solar file set as `BC4:/user/home/mf22281/um_updates/shift_TSI.dat`
	This solar file set the TSI values start from 1361 $W/m^{2}$ for 20 years, then suddenly shift to a larger value (1391 $W/m^{2}$) for 10 years, then shifts back to 1361 $W/m^{2}$ for the remaining years. 
	Set running from year 1850 to 2299. 
	![[shift_TSI.png]]



### Result
#### compare TSI_CMIP6 with standard PI job (xqcpa - xqcpz)

Anomaly of Surface air temperature (ANN)
![[xqcpa-xqcpz_temp2m_all_months_fsy_pjxy-time-series_tfann.png]]

Anomaly of Surface air temperature (JJAS)
![[xqcpa-xqcpz_temp2m_all_months_fsy_pjxy-time-series_tfjjs.png]]

Anomaly of Surface air temperature (DJF)
![[xqcpa-xqcpz_temp2m_all_months_fsy_pjxy-time-series_tfdjf.png]]


Anomaly of Precipitation (annual)
![[xqcpa-xqcpz_precip_all_months_fsy_pjxy-time-series_tfann.png]]

Anomaly of Precipitation (monthly)
![[xqcpa-xqcpz_precip_all_months_fsy_pjxy-time-series_tfmonth.png]]

Anomaly of Precipitation (JJAS)
![[xqcpa-xqcpz_precip_all_months_fsy_pjxy-time-series_tfjjs.png]]

Anomaly of Precipitation (DJF)
![[xqcpa-xqcpz_precip_all_months_fsy_pjxy-time-series_tfdjf.png]]

Anomaly of Evaporation
![[xqcpa-xqcpz_evap_all_months_fsy_pjxy-time-series_tfann.png]]


Anomaly of Precipitation - Evaporation
![[xqcpa-xqcpz_precipevap_all_months_fsy_pjxy-time-series_tfann.png]]

Anomaly of Mean sea level pressure
![[xqcpa-xqcpz_mslp_all_months_fsy_pjxy-time-series_tfann.png]]

Anomaly of Downward solar radiation at TOA
![[xqcpa-xqcpz_downsolartoa_all_months_fsy_pjxy-time-series_tfann.png]]

Anomaly of Downward solar radiation at surface
![[xqcpa-xqcpz_downsolarsurf_all_months_fsy_pjxy-time-series_tfann.png]]

Anomaly of Net Solar radiation at TOA
![[xqcpa-xqcpz_netsolartoa_all_months_fsy_pjxy-time-series_tfann.png]]

Anomaly of Net solar radiation at surface
![[xqcpa-xqcpz_netsolarsurf_all_months_fsy_pjxy-time-series_tfann.png]]



Anomaly of Downward longwave radiation at surface
![[xqcpa-xqcpz_downlongsurf_all_months_fsy_pjxy-time-series_tfann.png]]

Anomaly of Net upward longwave radiation at surface
![[xqcpa-xqcpz_netlongsurf_all_months_fsy_pjxy-time-series_tfann.png]]

Anomaly of Net radiation at surface
![[xqcpa-xqcpz_netradiationsurf_all_months_fsy_pjxy-time-series_tfann.png]]

Anomaly of Outgoing longwave radiation at TOA
![[xqcpa-xqcpz_olr_all_months_fsy_pjxy-time-series_tfann.png]]

Anomaly of Sensible heat flux
![[xqcpa-xqcpz_sensible_heat_all_months_fsy_pjxy-time-series_tfann.png]]

Anomaly of Latent heat flux
![[xqcpa-xqcpz_latent_heat_all_months_fsy_pjxy-time-series_tfann.png]]

Anomaly of Total cloud cover (random overlap)
![[xqcpa-xqcpz_totalcloud_all_months_fsy_pjxy-time-series_tfann.png]]
