[back to CMIP7 ancillaries](CMIP7_ancillaries.md)

## Solar forcing for HadCM3

### Where to access data
You can find introduction of solar forcing from [Homepage of SOLARIS-HEPPA](https://www.solarisheppa.kit.edu/index.php), the [CMIP7 Solar forcing](https://www.solarisheppa.kit.edu/75.php), and the paper [Funke et al., 2024](https://gmd.copernicus.org/articles/17/1217/2024/).

Data can be access from links 
[CMIP7 reference solar forcing dataset (1850-2023; monthly](https://cloud.iaa.es/index.php/s/n7cacmRBjk5Gb8f), 
[CMIP7 reference solar forcing dataset (1850-2023; daily)](https://cloud.iaa.es/index.php/s/nJFTPcnFwZ3smTo), 
and [CMIP7 future solar forcing dataset (2022-2299; monthly)](https://cloud.iaa.es/index.php/s/QWorEALDriYabgN); [CMIP7 future solar forcing dataset (2022-2299; daily)](https://cloud.iaa.es/index.php/s/j7ncYwoHXCtRwRE); 
and [metadata](https://www.solarisheppa.kit.edu/img/CMIP7_metadata_description_4.6.pdf).



To be noticed, the CMIP7 solar forcing provides reference data ranging from 1850-2023 (174 years in total. 1850-1873 for pre-industrial control; version 4.6) and future data ranging from 2022-2299 (version 4.6-a002). 
CMIP6 provides data from 1850-2299 (450 years in total; version 3.2).

However, the link for downloading CMIP6 solar forcing data are now overwritten by the CMIP7 one. But you can access data from my previous saved file: [monthly resolution reference solar forcing for CMIP6](Attachments/CMIP7_fcg_solar/solarforcing-ref-mon_input4MIPs_solar_CMIP_SOLARIS-HEPPA-3-2_gn_18500101-22991231.nc).

### How to process data

#### Total Solar Irradiation (TSI)
The HadCM3B model requires time-varying Total Solar Irradiation (TSI) file in annual mean resolution, saving as a `.dat` file with two columns (`year value`), without column name. So we need to convert the original monthly data into annual mean format. You can use this python script to convert and plot data: [Convert_TSI_data.ipynb](Attachments/CMIP7_fcg_solar/Convert_TSI_data.ipynb)

You can get the converted annual mean **varying_TSI_CMIP6.dat** file, for example, from [local path](Attachments/CMIP7_fcg_solar/varying_TSI_CMIP6.dat) (can be opened with Notepad), or in `BC4:/user/home/mf22281/um_updates/`.

The file looks like this:  
![head of varying_TSI_CMIP6 file.png](<Attachments/CMIP7_fcg_solar/head of varying_TSI_CMIP6 file.png>)

TSI data for CMIP6:  
![TSI_CMIP6.png](Attachments/CMIP7_fcg_solar/TSI_CMIP6.png)

TSI data for CMIP7_reference:
![TSI_CMIP7.png](Attachments/CMIP7_fcg_solar/TSI_CMIP7.png)

Comparisons of CMIP6 and CMIP7_reference TSI data:
![TSI_CMIP6&7_1.png](Attachments/CMIP7_fcg_solar/TSI_CMIP6&7_1.png)

![TSI_CMIP6&7_2.png](Attachments/CMIP7_fcg_solar/TSI_CMIP6&7_2.png)

### How to implement the forcing into HadCM3

#### Setup a transient TSI job
Tutorial: [Tutorial of Solar Orbit Setup_202503.docx](<Attachments/CMIP7_fcg_solar/Tutorial of Solar Orbit Setup_202503.docx>)


Key process:
- copy a standard HadCM3B job. 
- setup a module in PUMA2, UMUI window:



> Model Selection  
-> sub-model independent  
-> compilation and modification  
-> modifications for the model  
-> Fortran Mods table
> |Fortran modes | Include Y/N |
> |--------------|-------------|
> |$PV_UPDATES/solar_orbit_real1950.mod|Y|


Where $PV_UPDATAES: `BC4:/mnt/storage/private/bridge/swsvalde/um_updates/`

- Include time-varying TSI file and turn on related options in PUMA2, UMUI window:
> Model Selection  
-> sub-model independent  
-> Script inserts and modifications  
-> Defined Environment Variable  
>> `L_SEC_VAR: .TRUE.`: set orbit changing through time  
>> `L_SOLAR_SPEC: .TRUE.`: set solar spectrum changing through time  
>> `ORB_REAL_YEAR: 0`  
>> `ORB_OFFSET_YEAR: 0`  
>> `SOLAR_FILE: /home/mf22281/um_updates/varying_TSI_CMIP6.dat` (change file path and name as you want)

![PUMA3_set_time_varying_TSI.png](Attachments/CMIP7_fcg_solar/PUMA3_set_time_varying_TSI.png)

- save
- process
- copy job from PUMA2 to `BC4:~/umui_jobs/`

You can further check or modify the setting in
`BC4:~/umui_jobs/jobid/MODS_UM`:  
![BC4_umui_jobs_jobid_MODS_UM.png](Attachments/CMIP7_fcg_solar/BC4_umui_jobs_jobid_MODS_UM.png)

`BC4:~/umui_jobs/jobid/CNTLATM`:  
![BC4_umui_jobs_jobid_CNTLATM.png](Attachments/CMIP7_fcg_solar/BC4_umui_jobs_jobid_CNTLATM.png)

`BC4:~/umui_jobs/jobid/SCRIPT`:  
![BC4_umui_jobs_jobid_SCRIPT.png](Attachments/CMIP7_fcg_solar/BC4_umui_jobs_jobid_SCRIPT.png)

## Setting
### Control run: xqcpz
A copy of the standard HadCM3B job, tdaag, which is HadCM3-MOSES2.1-TRIFFID_dyn, Pre-industrial.  
Solar constant = 1361.0 $W/m^2$.  
re-run from year 1850 to 2299.  
check setting and results of xqcpz and xqcpz-tdaag [here](https://www.paleo.bristol.ac.uk/ummodel/data/xqcpz/standard_new_html/xqcpz.html)
### Test effectivess of solar setting: xqcpb
solar file set as `BC4:/user/home/mf22281/um_updates/shift_TSI.dat`.  
This job is used to test the effectiveness of the solar setting.    
This solar file set the TSI values start from 1361 $W/m^{2}$ for 20 years, then suddenly shift to a larger value (1391 $W/m^{2}$) for 10 years, then shifts back to 1361 $W/m^{2}$ for the remaining years.  
Set running from year 1850 to 2299.  
check setting and results of xqcpb and xqcpb-xqcpz [here](https://www.paleo.bristol.ac.uk/ummodel/data/xqcpb/standard_new_html/xqcpb.html)  
![shift_TSI.png](Attachments/CMIP7_fcg_solar/shift_TSI.png)
### Test with CMIP6_TSI: xqcpa
solar file set as `BC4:/user/home/mf22281/um_updates/varying_TSI_CMIP6.dat`  
running from year 1850 to 2299.  
check setting and results of xqcpa and xqcpa-xqcpz [here](https://www.paleo.bristol.ac.uk/ummodel/data/xqcpa/standard_new_html/xqcpa.html)  
### Test with CMIP7_TSI_ref: xqcpc
solar file set as `BC4:/user/home/mf22281/um_updates/varying_TSI_CMIP7.dat`
running from year 1850 to 2023.
check setting and results of xqcpc and xqcpc-xqcpz [here](https://www.paleo.bristol.ac.uk/ummodel/data/xqcpc/standard_new_html/xqcpc.html)

### Test with CMIP7_TSI (reference + future): xqcpd
solar file set as `BC4:/user/home/mf22281/um_updates/xxx?`
running from year 1850 to 2299.
check setting and results of xqcpd and xqcpd-xqcpz here.
(To be update...)
## Result
### compare shift_TSI job with standard_PI job (xqcpb - xqcpz)  
![xqpcb-xqcpz_surface_air_temperature_ann](Attachments/CMIP7_fcg_solar/xqcpb-xqcpz_temp2m_all_months_fsy_pjxy-time-series_tfann.gif)   

![xqcpb-xqcpz_downward_solar_radiation_at_TOA](Attachments/CMIP7_fcg_solar/xqcpb-xqcpz_downsolartoa_all_months_fsy_pjxy-time-series_tfann.gif  )

### compare TSI_CMIP6 with standard PI job (xqcpa - xqcpz)
![xqcpa-xqcpz_surface_air_temperature_ann](Attachments/CMIP7_fcg_solar/xqcpa-xqcpz_temp2m_all_months_fsy_pjxy-time-series_tfann.png)  

![xqcpa-xqcpz_downward_solar_radiation_at_toa_ann](Attachments/CMIP7_fcg_solar/xqcpa-xqcpz_downsolartoa_all_months_fsy_pjxy-time-series_tfann.png)  

### compare TSI_CMIP7_ref with standard PI job (xqcpc - xqcpz)
![xqcpc-xqcpz_surface_air_temperature_ann](Attachments/CMIP7_fcg_solar/xqcpc-xqcpz_temp2m_all_months_fsy_pjxy-time-series_tfann.gif)

![xqcpc-xqcpz_downward_solar_radiation_at_toa_ann](Attachments/CMIP7_fcg_solar/xqcpc-xqcpz_downsolartoa_all_months_fsy_pjxy-time-series_tfann.gif)
### compare TSI_CMIP7_ref with TSI_CMIP6 (xqcpc - xqcpa)
![xqcpc-xqcpa_surface_air_temperature_ann](Attachments/CMIP7_fcg_solar/xqcpc-xqcpa_temp2m_all_months_fsy_pjxy-time-series_tfann.gif)

![xqcpc-xqcpa_downward_solar_radiation_at_toa_ann](Attachments/CMIP7_fcg_solar/xqcpc-xqcpa_downsolartoa_all_months_fsy_pjxy-time-series_tfann.gif)