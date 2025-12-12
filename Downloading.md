[Back to HadCM3_technical_notes](HadCM3_technical_notes.md)

* There is a BRIDGE-wide crontab that cycles through users.  This needs root access. Could move to a system where all users have their own crontab.

* tidy_expt does not have the same checks as ftp_master/control, and can sometimes delete files.

* pi->pt and pg->pl is done during downloads, but not after tidy_expt.  Webpage processing will do this final step, or it can be done manually.

* precipevap folder is only used for .monthly files and for sed fless over land/ocean -> no global evap climatology field is produced.


* wetland and biome post-processing id sone on oligocene in a separate queue - see in ummodel/scripts/sed2.dat.


* search for 'ggpjv' in scripts as sometimes functionality only runs for user ggpjv.

* You can run the downloads manually by running `~swsvalde/bin/ftp_control`.  This is a wrapper script that gathers arguments to pass to `~swsvalde/bin/ftp_master`.

* ftp_master again assembles a lot of arguments, makes appropriate directories and sshfs links, checks quotas, decides which files to download, and runs remove_unwanted_files remotely.  It then loops over files to be copied.  It copies the file over via the sshfs mount.  It then removes the remote file.  It then runs `~swsvalde/bin/convert_file` with appropriate options:
```
${swsvalde_root}/bin/convert_file$suffix -file $file1 -expt $expt -type $type -list_runs $list_runs -check $check -famous_rename $famous_rename
```
`$suffix` can be set to is ggpjv for testing purposes.  
`${swsvalde_root}` is ~swsvalde.  
`$file1` is the name of the file to be converted  
`$expt` is the experiment name  
`$type` is the type, e.g. pa, pb, pc etc.  
`$list_runs` is y or n depending on whether the list_runs entry in ~swsvalde/ummodel/scripts/html_list/jobs exists.  
`$check` is y or n, usually n I think in the automatic downloads, but default is y in the convert_file script I think.  
`$famous_rename` should be y if using famous, default is "" in the convert_file script I think.







 