[Back to HadCM3_user_notes](HadCM3_user_notes.md)

# Introduction
Below is a full description of the HadCM3 workflow from start to finish, following an example experiment. Before going through this example, make sure that you have completed all of the setup steps listed in [Getting_started_with_HadCM3](Getting_started_with_HadCM3.md).

# Overall Process

The HadCM3 workflow described through the remainder of this page can be summarised in the following steps:

1. **Prepare experiment**
Prepare an experiment job, using the umui (on puma). The umui is a data base which contains all the information about a particular simulation. The umui creates a 5 letter code which becomes the job name and is used in all following work. In UM terminology, the 5 letter is called the RUNID.

2. **Copy to HPC**
Once the job is prepared, there is a button on the umui which processes the job. This creates a folder (in $HOME/umui_jobs/RUNID on puma) with a set of files that will control the running of the model, based on the information in the umui database. We must transfer this folder onto the HPC machine where we run the job.

3. **Compile executable**
On the HPC machine, we first must create an 'executable' file for the model itself. We do this be submitting the job to 'compile' the code (which is mainly in Fortran) into an executable. It is this executable that we will run. Creating the executable can take between an hour and 12 hours to complete.

4. **Submit simulation**
Once the executable is created, we can then submit the job to run the model itself. All HPC machines are shared and jobs can be submitted to a number of different queues, depending on the length of the simulation and whether it is a test or full run. Most machines have time limits varying from an hour of cpu time up to 14 days. However, the run may take a long time (up to several months) and will often therefore multiple continuation submissions.

5. **Transfer Data**
Whilst the model is running, it is outputting the “weather” data and this can rapidly grow to very large quantity of data. Most HPC machines do not have large data storage areas so we need to transfer the data back to our BRIDGE servers.   This is done automatically, following a few setup steps. A script will download all “old” output files (i.e. those no longer needed by the simulation) and will also convert them from UM format to netcdf format. To do this you need to:

- Create an entry in our BRIDGE database of UM simulations, and create a copy of the ancillary files (these are files used to setup land sea mask, orography). These two steps are controlled by webpages.
- Add the RUNID to a file called $HOME/bin/ftp_sh.bc4.params (or equivalent)

6. **Tidy Experiment and Output**
When the simulation is finished, you need to download the remaining files, using a script called tidy_expt. You may also want to run another script (fill_gaps_new01) to check that no file is missing.

7. **Create Climate Files**
Finally, you need to process the files to produce the climate means and other diagnostics. This is also controlled by a webpage.


# Detailed workflow
## 1. Prepare experiment

### (a). The UMUI
Log on to puma. Note that you must have Xming running for the following to work – Xming allows a remote machine to send windows to your desktop.

Type (the & sign puts the user interface in the background, so you can continue to type at the command line):

`umui &` 

A grey Gui should pop up. If it doesn’t then check that Xming and putty are correctly set up.

First, we will find some of the models described in the [GMD paper](https://www.geosci-model-dev.net/10/3715/2017/gmd-10-3715-2017.html). They are all owned by user swsvalde.

Click on: Search –> Filter, and set Owner = swsvalde,\[USER\] 

Where \[USER\] is your username on puma.  This will show your experiments, and those owned by swsvalde.  In 'umui language', an 'Experiment' is a folder that contains a number of 'Jobs'.  A Job is the same as a model simulation. To view the jobs in an experiment, click on the folder symbol. 

To view a job, click: File --> Open read only
*Note: Make sure that only the job you want to view is highlighted!*

You can now explore different sections to see how the job has been set up (e.g. to see which gravity wave drag scheme is used, look under: Model Selection --> Atmosphere --> Scientific Parameters and Sections --> Section by section choices --> Gravity wave drag. Click on the green square to open a new window with containing information about the gravity wave drag scheme.)

### (b). Setting up a simulation
In this example, I will be using the 'tdaag' job (i.e. job 'g' from the experiment 'tdaa') as a starting point. It is very rare to create a new job from scratch, you will always copy an existing job and then make changes from there.

To first create an empty experiment folder, click on: Experiment –> New
Enter an experiment description (remember that an experiment is a folder of jobs), and you will automatically be given a unique code for your folder. In my case, I created a new experiment with ID xqgf.

To copy an existing job into your experiment folder, highlight the destination experiment folder, also highlight the job to copy from. Then click on: Job –> Copy. Choose an identifier (i.e. last character of the job name) for the new Job. 
I have now created a new job called xqgfa which is a direct copy of tdaag.

*Note: you may also wish to make a second copy to edit, keeping your first copy as an identical replica of the standard run, but that is up to you. In my case, I created a fresh copy - xqgfb*

You can now make changes to your job - In this example I will be changing the length of the run.

Highlight your job and click: File --> open read write

Now I go to: Model Selection --> Sub-Model Independent --> Start Date and Run Length Options.
In this window the Target run length is set to 100y 1m (*Note: the extra month ensures a complete final year*). I now change this to 10y 1m to bring the end date up to 2025.

Click on Close at the bottom of the window, and then Save at the bottom of the Job window. Your job is now saved in the umui system. To output the model scripts, click on Process at the bottom of the window.

You can use the “Difference” function to explore the difference between to simulations. Try this to check the changes that you have just made. Highlight both jobs you want to compare, and then go to:
Job --> Difference --> Long --> No
*Note: This is also a useful way to compare other jobs and double check that they are doing what you think they are doing!!*

Close the umui, and return to your puma2 terminal. If you now look in your umui_jobs directory (i.e. `ls ~/umui_jobs`) you will see a new directory with the same name as your new job (in my case `~/umui_jobs/xqgfb`). If you look within this new directory, you will find the Bash scripts that run the model.

You've now set up your first model run!!

## 2. Copy to HPC

The folder created by umui needs to be transferred to the HPC machine. To do this, you need to do one or two copies depending on which machine your id_rsa.puma was created. From this machine, type:
	`scp -rp archer2:umui_jobs/[JOB_ID] ~/umui_jobs`

So, in my case:
	`scp -rp archer2:umui_jobs/xqgfb ~/umui_jobs`

If this machine is not the HPC, then do
	`scp -rp ~/umui_jobs/[JOB_ID] bc4:umui_jobs`

*Note: Use bc4 for BlueCrystal, use bp14 for BluePebble.*

You should now have the Job folder on the HPC machine.

## 3.  Compile executable

The model code itself is written in language FORTRAN. This has to be “compiled” before it can be run. To compile, on BlueCrystal, type:
	`~ggpjv/swsvalde/bin/clustersubmit -s y -q veryshort -r bc4 -P [PROJECT_CODE] [JOB_ID]`
	...where \[PROJECT_CODE\] is the code you used when you applied for BlueCrystal.

Whilst the code is compiling type `cd ~/dump2hold/[JOB_ID]/code`, and then try `ls -lrt`a few times and you will see the compilation progressing. After a few minutes the compilation will finish, and the contents of the code directory will be zipped up and moved. When this happens: `ls ~/dump2hold/[JOB_ID]/dataw`...
...if you have a file in that directory called “Hadley4.5.exec”, then all is good!!!

## 4. Submit simulation

To submit the actual job, on BlueCrystal:
`~ggpjv/swsvalde/bin/clustersubmit -s y -c n -a y -r bc4 -q veryshort -p 7x4 -P [PROJECT_CODE] [JOB_ID]`

You can check the status of your job in the queue of the supercomputer by typing:
`myqs1`

You may see your job near the bottom of the list. The “Q” means it is queuing (unless you are lucky and it has started already, in which case it will be “R”). Once your job starts running (this could take anything from a few seconds to a few days, depending on the queues on the machine), the output will appear in your `~/dump2hold/[JOB_ID]/datam` directory on BlueCrystal.

The files that appear have the following naming convention: `[JOB_ID][s]@[t][d]` where \[s\] can be “a” or “o” depending on if this is an atmospheric or ocean variable respectively, \[t\] can be da, pc, pd, pf, or pg depending on whether this is a restart, atmospheric dynamics, atmospheric physics, ocean surface, or ocean depth variable respectively. \[d\] is a date stamp with a format that depends on the file type, but note that the year has an odd convention: it will be of the form e.g. i49, where the initial letter (i in this case) represents the century, and 49 the year.

All files are produced once every month, except for pg files that are produced once every year. So, for my 10 year simulation I have 120 da,pc,pd,pf,pg files, and 10 pg files (total = 610 files); check by going to `~/dump2hold/[JOB_ID]/datam` and running:
`ls -1 | wc -l`

Once you have the correct number of files, your job will disappear from the queue, and your job is finished.

**For more information about the clustersubmit script, see [Documentation for clustersubmit](Documentation_for_clustersubmit.md)**

## 5. Transfer Data


## 6. Tidy Experiment and Output


## 7. Create Climate Files


