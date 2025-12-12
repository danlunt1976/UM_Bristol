
[Back to HadCM3_technical_notes](HadCM3_technical_notes.md)
# Transferring Experiments from BC4 to BluePebble

These notes were originally written by Chris Jones.  Please feel free to edit (as with all files in this repository!)
## Log on to Blue Pebble.

For me, I had an account already, so can just log on directly. Important that you use the “04” login node. So e.g.:
```
ssh -Y tw23150@bp1-login04.acrc.bris.ac.uk
```

## Set up environment

### 1. Create all the necessary directories

When you log on, you will be in your home directory. For me: `/user/home/tw23150`

Type `ls -l` to see the files and folders already there. Some of these will be links to folders on a different disk. This is to stop your home folder filling up. But for me some of these didn’t exist.

So if you see any flashing files these will need creating. It means the links don’t exist. E.g. for me I had many links like this:
```
lrwxrwxrwx.  1 tw23150 geog        42 Oct 31  2023 DUMP2HOLD -> /bp1/geog-tropical/users/tw23150/DUMP2HOLD

lrwxrwxrwx.  1 tw23150 geog        38 Oct 31  2023 ancil -> /bp1/geog-tropical/users/tw23150/ancil
```
If these are flashing, then they need to be created. Try changing to this folder: `cd /bp1/geog-tropical/users`

If you have a directory under there with your username, then great. You can change into that and create the folders you need beneath it – DUMP2HOLD, ancil etc.

If there is no entry for your username then you need to email the hpc helpdesk on: [hpc-help@bristol.ac.uk](mailto:hpc-help@bristol.ac.uk) . Explain you are moving over from BC4 to Blue Pebble and need a user directory set up under: `/bp1/geog-tropical/users`

### 2. Set up paths and environment variables

The pathnames to UM files differs here from BC4. So you will need to have some differences in your .profile and .bashrc etc files. But you might also have some entries in those files on BC4 which you would like to keep. So you will need to be selective. But a good guide will be that Paul’s versions of these files are the best place to copy. So copy the following files to your home directory:
```
cp ~ggpjv/.bashrc ~/
cp ~ggpjv/.bash_profile ~/
cp ~ggpjv/.kshrc ~/
cp ~ggpjv/.profile ~/
```
If you then have any lines from your BC4 versions that you would like to add, and you are comfortable editing these files then go ahead.

I also found I was missing a “setvars” file, and this should be linked from a central location. So type:
```
ln -s /bp1/geog-tropical/um/PUM64/setvars setvars
```
you may also need a config file for clustersubmit, so if needed create a directory in your home directory called `.um` and then in here copy:
```
cp ~ggpjv/.um/clustersubmit.conf ~/.um/
```

### 3. Copy files over from BC4

Most other things can be simply copied over from BC4. All mods, scripts, hand edits, dump and ancillary files etc. And of course any jobs set up under umui_jobs/

So to copy a file from BC4 (type this on Blue Pebble, and make sure you’re in the correct directory), e.g.:
```
cd ~
scp -r tw23150@bc4login2.acrc.bris.ac.uk:/user/home/tw23150/mods .
```

Here I am copying a directory called `mods` from my home directory on BC4. Do the same with umui_jobs for example. The `-r` after scp means you will copy the whole directory across. But of course you can copy individual files too.

### 4. Try running a UM job

The _clustersubmit_ script should work as before. If you have copied Paul’s clustersubmit.config file then it should default to using the right queue and partition etc. But you can give options for all of these. The key differences from BC4 are

* use `-q compute`, instead of `-q cpu` or `-q veryshort`
* use 24 not 28 cores because the nodes have just 24 cores per node. So `-p 6x4` instead of `-p 7x4`
* machine name is: `-r bp14` (instead of `-r bc4`)

In theory we would expect the same accounts to work on BP as on BC4. But I had a problem, so if you get errors such as “sbatch: error: Batch job submission failed: Invalid account or account/partition combination specified”, you might need to contact the help desk ([hpc-help@bristol.ac.uk](mailto:hpc-help@bristol.ac.uk)) to see if you have been set up the right accounts.

Just like BC4 you will need to run a compile job and then a run job. I encountered a strange problem on my run job due to namelists not being created properly.

If you get an immediate failure and error messages like this:
```
forrtl: severe (24): end-of-file during read, unit 5, file /user/home/tw23150/DUMP2HOLD/um/xqfsp/tmp/xqfsp.namelists, line 563, position 0
```

Then contact Paul who can implement a fix for you in clustersubmit
