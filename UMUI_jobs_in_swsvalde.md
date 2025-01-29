# Introduction

When I started using the UM, I inherited a lot of different jobs from the Hadley Centre. These jobs covered the whole range of scientifically different versions of the model, from normal HadAM3-N48 (and HadAM3-N216), to HadSM3 and HadCM3-M1, and HadCM3-M2.1. However, the jobs often had lots of differences, due to different users, differences in STASH, the date when the job was created, different machines etc. etc. This made it very difficult to compare jobs and work out what was a true scientific difference, and what was just a path or machine technical difference. I also wanted to be able to submit to a range of different machines without having to make lots of changes to the job.

# umui job structure aim

I therefore decided to create a set of jobs covering all of the major variants of the model, which:

a. When taking differences between model variants, the only differences were related to science.
b. Standard modsets were all located together so path names were simple and clear.
c. Standard naming of folders, using variable names for key locations, so that moving to different folder names on different machines requires just one simple change.

Moreover, I then implemented a script, clustersubmit (an extension of the UM provided umsubmit) which will automatically make the changes required for different machines, change the job from compile to run mode (all of our standard jobs are set to compile and stop), and also allows the user to select the queue, core numbers of NS and EW, and the run time.

# Overall Structure

In the umui on puma, the user called swsvalde holds a series of experiments with different configurations of the model. Each experiment will have a number of jobs, with the highest letter representing the latest, most up-to-date version. When available, the original versions were successfully benchmarked against a “standard” from the Hadley centre. E.g., the HadCM3-M1 job tcsyb was run and output compared to a Hadley Centre equivalent. HOWEVER, subsequent versions may have made small changes to the science (and bug fixed errors) so that the latest versions may not be 100% scientifically identical to the original. If you are interested, you can go through the differences to help ascertain the changes. It is on my long to-do list, to document the changes but this will probably never happen!

Within each job, there is a standard structure. The path names etc use a standard naming convention based on some system variables, described below:

# Key "system" variables

When a job is submitted, the scripts expect a number of shell variables to be defined. This is achieved through a script called **setvars** or **setvars_4.5** or equivalent. On our BRIDGE machines, a user should include invoke this in their .profile file. Although we have also added a few extra definitions. In particular, we define a variable called DUMP2HOLD which is the folder which contains the job folder, with the input, output, and code folders (the name originates from an old national HPC machine which used this name). This folder needs to have sufficient space to handle the output from the job.

Within a umui job, go to **Sub-Model Independent -> Script Inserts and Modifications**. There will be a further number of “Defined Environment Variables”. These are rarely (never) changed for a simulation.

| Name       | Description                                                                                                                                                  | Typical Value              |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------- |
| ANCIL_ROOT | This is the root folder for most of the system wide ancil files (note that the precise location is defined below in the File and Directory naming section)   | /home/swsvalde             |
| PV_ROOT    | This is the root folder for most of the system wide modset files. (Note that the precise location is defined below in the File and Directory naming section) | /home/swsvalde             |
| UM_INPUT   | Folder for various standard input files                                                                                                                      | \$UMDIR/PUM_Input/vn4.5    |
| UM_OUTPUT  | Folder for various output files. I don’t think this is used!                                                                                                 | \$HOME/PUM_Output/vn4.5    |
| TEMP       | Temporary folder for a variety of files whilst model is running                                                                                              | \$DUMP2HOLD/um/\$RUNID/tmp |
| IN         | Temporary input file folder.                                                                                                                                 | \$TEMP                     |
