[Back to HadCM3_technical_notes](HadCM3_technical_notes.md)

* There is a BRIDGE-wide crontab that cycles through users.  This needs root access. Could move to a system wher all users have their own crontab.
* tidy_expt does not have the same checks as ftp_master/control, and can sometimes delete files.
* pi->pt and pg->pl is done during downloads, but not after tidy_expt.  Webpage processing will do this final step, or it can be done manually.
* precipevap folder is only used for .monthly files and for sed fless over land/ocean -> no global evap climatology field is produced.
* wetland and biome post-processing id sone on oligocene in a separate queue - see in ummodel/scripts/sed2.dat.  
* search for 'ggpjv' in scripts as sometimes functionality only runs for user ggpjv.
