# Averaging

[Back to HadCM3_technical_notes](HadCM3_technical_notes.md)

The stated total length is actually ignored.
The code uses the stated spinup length and averaging period.  
If the stated spinup period is longer than the actual files, the code will instead ignore this and start at the end of the simulations and work back to give the correct stated averaging period.
If the stated spinup period is shorter than the actual files, the code will use the stated spinup period and then the stated averaging period, leaving some files at the end unprocesed in terms of means.

