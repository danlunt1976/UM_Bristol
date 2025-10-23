[Back to HadCM3_user_notes](HadCM3_user_notes.md)


# Documentation for ensembles

# Background

Very often on bluepebble/bluecrystal, we have to queue for some time before the job commences. It is then frustrating if it crashes (e.g. with negative pressure or negative theta) after a relatively short time. The crash can often be easy to sort out but your job goes to the bottom of the queue.

Another problem with the queueing system on bluepebble/bluecrystal is that there is an absolute limit on the number of jobs that can run/queue at the same time (I think it is 40) but there is a larger limit on the total number of nodes (currently 100). The normal resolution of HadCM3 does not efficiently scale beyond 1 node so we cannot make use of the maximum node count.

To solve this problem, we have created the “ensemble script” which can combine several jobs into one bigger job, or can run one job within a larger overall job that can restart the model if it crashes.

# Basic Concept

UM version 4.5 (HadCM3 and family) consists of a set of fortran subroutines with a complicated suite of korn shell scripts to support running it. In practice, the complex scripts are quite difficult to change because they all strongly interact with one another. However, ultimately when you submit a job to run there is one overall driving script which runs everything.  Hence to run multiple versions of the model, all you need to do is to create/capture this script for each ensemble member and then find a mechanism to make the set of scripts run on a set of compute nodes. Simplistically, an ensemble script would look like:
```
#
for node in list of nodes ; do
  command to run job_N on node  &
done
#
while [ some criteria ] ; do
  check to see if criteria satisfied
done
```

where the `&` gets the job to run in the background and will continue to run until some criteria is met. This structure is pretty much how the new method works.

The script that drives the running of any particular job is created when you submit a job using clustersubmit, and is held in the umui_runs folder (not umui_jobs). It is called qsubmit.bc4loginX. bc4.acrc.priv and it is this script we need to grab (where X is one of the head nodes 1-4).

## Step 1
Prepare your ensemble set of jobs, and run them for a few months. Currently the script works best for continuation runs (it will work for new runs too but it will always be less reliable because new jobs are less reliable).

Copy the relevant umui_jobs to bc4/bp14 (if not done already - with the new puma on archer you will have done this already in order to run the short jobs above).

## Step 2
On bluecrystal, create a folder \$HOME/ensembles. Also copy some files:
```
cp ~ggpjv/ensembles/run_scripts_01 $HOME/ensembles  
cp ~ggpjv/ensembles/master_script_02 $HOME/ensembles  
cp ~ggpjv/ensembles/normal_resubmit_02 $HOME/ensembles  
cp ~ggpjv/ensembles/history_script_02 $HOME/ensembles
```
I’m advocating this method currently because I am still learning how best to do this and they may change without notice. Eventually we will have a stable version and these scripts will able to be accessed from some common location. By copying then across, there is no danger that they will change.

## Step 3 (assuming that ~ggpjv/swsvalde/bin is in your PATH variable)

Use the script **create_ensemble** to prepare the required files. Details of the script are below but the simplest use is:

`create_ensemble -file xxxxx -expts list_expts`

Where xxxxx is a filename which will contain a list of the required umui_runs folders. You should typically keep this to about 6 or 7 characters.

And list_expts is a list of experiments, separated by commas or spaces.

(if you are submitting a very large ensemble, it can sometimes be beneficial to group the jobs over a range of different numbers of nodes, as the queuing system may favour different numbers of nodes at different time.  As an example, see ~ggdjl/ensembles/create_all)

The script creates a file \$HOME/ensembles/ensemble_files/xxxxx.dat which contains a list of umui_runs folders.

The script works by submitting each experiment, then deletes the submitted job, but saves the corresponding umui_runs folder by copying it into the \$HOME/ensembles/umui_runs folder. It must do this because the \$HOME/umui_runs/ folders get deleted. It also edits the qsubmit script to ensure that it correctly picks up node information, and edits the output file name to be .eleave instead of the normal .leave.

Finally it creates the batch file to run the model. This file is called:
\$HOME/ensembles/xxxxx_batch.

To submit the ensemble type:
```
\cd $HOME/ensembles
sbatch xxxxx_batch
```

## Step 4
You now need to monitor how it is running. There are a number of tools to help:

(a) **check_running xxx**   (or simply **check_running** which will do all files in \$HOME/ensembles/ensemble_files).

This creates a list of the status of each simulation within the ensemble file. If **xxx** is specified, it will do the xxx.dat file from \$HOME/ensembles/ensemble_files/ folder. The output produces a list with each row looking like this:

*tfed.dat: tfedq: compute139: compute139: 4292608 Mar 12 14:39 tfedqa#pd000006607ja+ tfedqa#pd000006590dc+ Mar 12 09:47  79.31*

where first column is ensemble file, second is experiment name, third is the expected node based on those available, fourth is the actual node based on the .eleave file, 5-9 is the size, latest modification time, and name of latest file, 10-13 is the latest file when the last time you called the script, and column 14 is the estimated model speed (years per day) based on the time difference between the two files.

Things to pay attention to are:

  (1) That the expected and actual node should be the same. If they are different, something bad has happened and you need to stop the job.

  (2) The date of the latest file should be nearly the current time (with one or two minutes). If not then that simulation has crashed. If it is more than 20 mins old, then it had also failed to restart so something more profound has gone wrong. But it may be possible to restart it. See later for solutions.

  (3) The model speed should be something appropriate (i.e. about 30-50 model years per day for HadCM3, 80-90 years per day for HadCM3L, and several hundred years per day for FAMOUS). If it is much smaller, it could be because the model is starting, running for a month or two and then crashing, and then repeating this sequence. So a file could look to be new, but overall the model is failing. See later for solutions.

If (2) or (3) show problems, the first thing you should try is to reset the start file by using the restart_manually script (below). For some reason, I have noticed that the phist/thist files are not regularly updated so sometimes the model may try and restart from a much older location and the dump file is missing. This is quite common when restarting an ensemble run. NOTE that there is a time delay when doing this and it can take 20+ minutes before everything restarts so be patient and do not assume there is a problem prematurely!

(b) **special_where**:  This is a tool I use a lot and is not especially related to ensembles but it is good check on progress of runs. It also checks that downloading is working too.   There are no arguments to this script, just type: special_where

The output is a series of columns for each simulation of the form:

*tfefr n   90,484M diiidi pc_no =  2005 pd_no =  1766 pf_no =   699 pg_no =    35 last= tfefra#pd000006631sp+ ggpjv  8266     0 Mar 12 19:25*

2nd column = is it running or not (based on looking at the queue so will not think that it is running if part of an ensemble)  
3rd column = total space used by experiment in dump2hold  
4th column = what has happened to folder since last running script. Codes are n if new, d if number files reduced, s if same, S is same but file is recently created, and i if number of files is increasing. The set of letters correspond to total files, pc, pd, pf, pg and latest pd file.  
5th-12th column = number of files of each type  
13th column= latest file  
14th column = owner  
15th column = model speed, based on average across the files in datam (in units of 100x years per day)  
16th column = model speed, based on time difference between latest file and previous one.  
17th-19th = Date of modification of latest file  

(c) **edit_phist xxx yyy zzz**: This script will reset the phist/thist files to start from a specific dump file. It assumes that the start month was Dec and will only reset to a Dec start date. **xxx** is the experiment name, **yyy** is the dump_age_name (i.e. the name after …da), and **zzz** is the year since start of run. This script (the swsvalde version) is more sophisticated than other versions of this script because it resets all of the contents of the namelist file. This seems safer than only making the minimum modifications of the contents, though it is not clear whether it makes any difference.

In theory, if you just specify the experiment name, it should work out the very latest restart. However, due to variations in the namelist structure, this is not fully reliable so there is an additional script.

(d) **restart_manually xxx**: This is an extension to the edit_phist script and resets the phist/thist files to the latest available dump file. **xxx** is the experiment name. It works by finding the most recent dump file in the datam folder. However, to make this work it needs to know what was the start year of the simulation, and the script does not assume it is correctly stored in the phist/thist files. Hence to use this script you need to create a file in $HOME/ensembles/restart_manually_input with lines of the form:

temp 1850  
tewza 2850

Where the number indicates the start year, and the 4 letter code means that all experiments starting with the 4 letter code will use this start year, whereas the 5 letter code only refers to the specific simulation.

## Solving Problems

The output from the jobs is stored in the normal location (\$HOME/um/umui_out) but in files ending .eleave. If the model goes wrong, it will rapidly generate .eleave files every 10-20 minutes.

**clean_eleave_files:** deletes all of the eleave files except for the latest one for each simulation.

The .eleave files are identical to the normal .leave files so you can hopefully diagnose the problem and correct it. The job will then automatically restart.

## Ending the job

The job will not finish automatically. You will need to kill it (or let it timeout). Also, you will find the individual jobs will run at different speeds so you may decide to kill the job before they are all finished. For instance, it is a bit anti-social to be using 10 nodes but only one node is used. But there is no hard and fast rule. It is up to the individual to decide when to kill it.

## Bit more ambition

It is possible to start a new simulation when an ensemble member finishes and when there is still time left for the overall ensemble. To do this you must first run create_ensemble:

```create_ensemble -file temp1 -expt abcde```

Then edit the running ensemble_files/xxxxx.dat file and replace the job that has finished with the job that you want to start which is listed in temp1.dat. HOWEVER, you must be very careful to ensure that you keep the order the same. i.e if job 5 out of 8 has finished, you must replace line 5 and not add the job to the end. Similarly, you must keep the same number (actually you can increase the number of simulations listed but it is pointless. You must not decrease the number).

However, there is an experimental facility (which so far seems to work) where you can create a list of jobs in the file \$HOME/ensembles/new_runs_list.dat  then it will work through these when a job finishes.

## A little more details of the scripts

### run_scripts_01
This script starts the jobs running. The first argument is the umui_runs folder name, and the second is the node to run it on. It copies the relevant \$HOME/ensembles/umui_runs folder to \$HOME/umui_runs and then starts the job by simply executing the relevant qsubmit script as a background job (this allows the system to move on to the next command).

NOTE that there is a 120 sec time delay in the batch file after starting each job. This was added because there was a weird problem that I could not understand. Sometimes, if the jobs were started too rapidly, the output files (i.e. those in datam) would end up in the wrong simulation folder. I could not work out why but adding the time delay seems to largely cure the problem.

### master_script_02
This script loops over the nodes, decides whether it is still running and then resubmits the job if it has crashed. It calls:

(a) **normal_resubmit_02:** this works out whether the running job has stopped, and if so why has it failed. This script calls quite a few other scripts.

(b) **history_script_02:** this work out the status of the run at the time of resubmission. In theory it can be used to help get the script to do different things depending on whether it has been resubmitted from this point before. But not very reliable.

If these scripts work out it needs resubmitting then master_script will resubmit.

### create_ensemble
This creates the required files, specifically:

(a) creates the umui_runs folder for each experiment within the ensemble by submitting the job using clustersubmit and then copying the umui_runs folder to the ensembles folder.

(b) creates the .dat file for the ensemble which is the last of umui_runs folders

(c) creates the batch file for the job.

A full set of arguments are:

-e\|-expts\|-expt )    - this is a list of expts. No default.

-d\|-delete\|-new )    - by default, the script will add to an existing .dat file. If -d y, then the .dat file is created from scratch.

-c )    - continuation run (default).If -c n, then will treat then as new runs.

-f\|-file )    - outfile name for .dat file, and also for the batch file.

-p )    - processor usage. Default is 7x4. (but will default to 6x4 for bluepebble)

-P ) - account. e.g. ```-P PGEO001321```.  You can set this with the -P option, or in $HOME/.um/clustersubmit.conf .  If using a .conf file, this file should contain a line of text of the form e.g.  ```account="PGEO001321"```

-q )    - the queue to submit to. Default=cpu, but could be e.g. bridge or paleo.

-g)    - groups the experiments into batches of N jobs



# EXTRA USEFUL INFORMATION FROM RUNNING MY FIRST ENSEMBLE:
  
The jobs should just restart when any problem is corrected so failing to restart indicates a more serious problem. For these more serious problems, restarting the ensemble is not that trivial, and the fact that it has not automatically started suggests a deeper problem than the year (NOTE that restarting can take up to 10mins x the number of jobs in ensemble so could take an hour). Steps are as follows:

(1) Use the ```restart_manually``` and wait for up to an hour  (you've done this)

(2) Look at the very latest .eleave file. See if you can find out what the problem is.  .eleave files replace the normal .leave file but contain the same information. It might be worth running the ```clean_eleave_files``` which removes all but the latest version. If a job is failing, the ensemble script will produce a new .eleave file every time it tries to restart and it won't take long to result in >100 in the ~/um/umui_out folder.

I just took a look at this for tfgx_01 and found that tfgxb has not produced a .leave file for more than a day. So it is not restarting. Why?

By contrast, tfgxf has produced zillion of files. The output is:
```
mpiopts = -np 28 -host compute350 -hosts compute350
srun: Job step creation temporarily disabled, retrying
srun: error: slurm_receive_msg: Socket timed out on send/recv operation
srun: error: slurm_receive_msg: Socket timed out on send/recv operation
srun: error: slurm_receive_msg: Socket timed out on send/recv operation
srun: error: slurm_receive_msg: Socket timed out on send/recv operation
srun: error: slurm_receive_msg: Socket timed out on send/recv operation
```
This indicates that something with the ensemble has gone run (srun is a slurm program that controls what job runs on what node).

I also noted that you had managed to add tfgxd twice!!!  The good news is that it has not damaged the run that is working but one node has been idle. I think you must  have done create_ensemble.... -expt tfgdb,tfgdc,tfgdd,tfgdd,....With these big jobs it is important to be careful. 

(3) If looking at the .eleave file does not help, look at the ~/ensembles/*.out file corresponding to the ensemble you are running.  Go to the end of that file. The output for your run is complicated and is consistent with a problem with slurm and tfgxf. I think that what has happened is that this is "freezing" the restarts of all jobs, not just tfgxf.  

I have not yet sorted a simple method for solving this but you may be able to do the following:

(a) logon to the node that is running the simulation (```ssh compute350```, shown when running check_running). Type ```ps -wef | grep glxaf```. Kill all the executables. Also any srun jobs.

(b) logon to the lead node (shown by the first listed from ```check_running```, in your case compute142). Again do a ```ps -wef | grep glxaf```.  Kill most jobs referring to tfgxf. This is the bit I have not perfected. Killing too much will kill the overall job. Initially kill just the lines that repeat themselves.

(c) If this does not work, then the job is probably unrecoverable and you have to make a decision about whether to kill the ensemble job or let it run, knowing that not all nodes are being used. There is no hard-and-fast rule about when to do this. It is for you to decide depending on the importance of the runs and queue times etc. 

(4) At any point, you can repair broken runs by commenting out the simulation in the ```~/ensembles/ensembles_file/xxxxx``` (just add a C to beginning of line) and then working normally. Once you have it working, remove the comment and the ensemble will restart it (assuming that it is not a slum problem). HOWEVER, remember to remove the .leave file since otherwise the automatic resubmission script will submit the job to the normal queue as well as running as an ensemble.

The overall ensemble jobs will not automatically restart. However, all you need to do is go into the ~/ensembles folder and type ```sbatch batch_job_name```.

Given that your ensemble job has almost used the max time, I would suggest you do the following:

(1) Try steps 3a and 3b. It will be a learning curve for you and it doesn't matter if you delete too many jobs and hence cause the ensemble to finish a few hours early.

(2) Also do step (4) to get the faulty jobs running.

(4)when ready, kill your existing job and either resubmit (but then you are wasting one node because of the duplication of tfgxd), OR prepare a new ensemble (e.g. ```create_ensembles -file tfgx_01 -expts ......-new y```).


**Xin's note**:
In my situation that simulations did not restart automatically and some of these nodes became zoombie nodes, I've tried to restart the simulations on my own as follow:
1) ```ssh computexxx```
   computexxx is the zoombie node.
3) restart manually
```
module load slurm
echo $PATH
export PATH=/opt/slurm/bin:$PATH
cat $HOME/ensembles/run_scripts_01 | grep mpirun
export ensemble_file=$HOME/ensembles/ensemble_files/XXX.dat
export nodes="computeXXX computeXXX computeXXX computeXXX"
$HOME/ensembles/master_script_02 $HOME/ensembles/normal_resubmit_02
```
XXX.dat is the ensemble contains your zoombie nodes, computexxx are the nodes in this ensemble runs, make sure it's the same order as your runs.


# Further updates to the script (Paul – 27/06/2022)

(a) it deletes any core.* files each time it checks on the simulations. This prevents the build-up of these files that can occasionally happen if the job is misbehaving.
(b) I have an updated version of the script that diagnoses errors with the leave file. leave_file_errors_02 is functionally similar to the original but is much more straightforward to maintain. The output is slightly different, and the input can be more varied. The script is used in the ensembles system to decide what to do if the job is no longer running. 
**IMPORTANT** - (c) I have added a new feature. If you put newjob in an ensembles/ensembles_file/ it forces the script to select a new job from the $HOME/ensembles/new_runs_list.dat. I added this because I am about to do a tuning ensemble (to merge the Eocene and Green Sahara parameter sets) and wanted to have this ability since a single tuning run is not 14 days. I want to be able to use one ensemble script to run many jobs.


## If you need to change where the downloads are happening

Firstly kill the ftp_master jobs currently running on silurian and delete the corresponding ~/umdata/expt/downloading file. 
Secondly, modify the ftp_sh.bc4.params so that simulations you wish to download have the syntax expt::triassic.

Wait a few hours and check that you have ftp_master scripts running on triassic but not on silurian.

### Freeing up space:

Try not to leave files on the dump2hold space. If a run has finished, remove it. Don't leave it. The small files add up! 

Check that the files are not building up. I use ```special_where``` to find out the status of bc4 filestore. Sort out when some experiments are not downloading.

On BC4 - If they are building up, use ```remove_unwanted_files```  Can be even more severe if jobs are nowhere near finishing (```remove_unwanted_files -expt xxx -delete_papb 2``` will remove most of the pa/pb files before downloading). But only do this if you are in the middle of spinup.

Run ```check_running``` and repair any jobs that have stopped. This could be particularly important now (after the disk space problem). Don't assume that the simulations are running.

On BRIDGE servers, run ```remove_unwanted_files -expt``` to make sure they do not build up too much. This removes unwanted dump files.

## If you have a large set of Step 1 jobs – loop clustersubmit them:

 didn't mean one by one. You can loop over simulations using:
```
for job in ${job_names[@]}; do

   clustersubmit -c n -s y -a y -q veryshort -r bc42 -g 1x1 $job

done
```
If this works, on the timescale of 6 hours it will progress about 3 months and run out of time. At that point, you can repeat the submission but try more processors. i.e.
```
for job in ${job_names[@]}; do
   clustersubmit -c y-s y -a y -q veryshort -r bc42 -g 6x1 $job
done
```
(Note that there are two difference to the second clustersubmit command which I have highlighted in bold). I found that this helped with a lot of my runs. It seems that there is a "shock" to the model when starting and that this requires you to use 1x1 but, if it survives a few months, then you can continue the run with more cores.

Note that the list of simulations that get  resubmitted may be smaller than in the first list. Use monitor to find out which jobs finished cleanly or not.

### Step 1 continued – once run:

I've taken a look and there are a mixture of things going on. To diagnose these, I did:
```
special_where
```
and
```
monitor
```
I then did
```
cat ~/logs/monitor.out | grep "ran out of time" 
```
This showed me which jobs had run out of time and quite a lot of jobs (57) got to the time limit (6 hours). However, we know that in some cases, this may be because the job got stuck at the first month. To find out which made real progress I did:
```
expts=`cat ~/logs/monitor.out | grep "ran out of time" | awk '{print $3}'`
for expt in $expts ; do cat ~/logs/special_where.dat | grep $expt;done
```
This showed to me that most had got to 3 months which is what we expected when they were only using 1x1 cores. Indeed if I then did:

for expt in $expts ; do cat ~/logs/special_where.dat | grep $expt;done | grep -v "pc_no=     3 pd_no=     3 pf_no=     3"

This showed me only two of the 57 did not have 3 months of files, and one of them (xpxnc) actually had 4 months! Hence only one of these time limit jobs failed to run: xpXnn.

So for the remaining time limited jobs, we should try resubmiiting with 6x1. I would do this by:
```
expts=`cat ~/logs/monitor.out | grep "ran out of time" | awk '{print $3}' | grep -v xpXnn`
for expt in $expts ; do clustersubmit -c y -s y -a y -q veryshort -r bc4 -g 6x1 $expt;done
```
In theory this might progress things, in practice there are some strange things going on and my analysis is not perfect but lets try these (the slightly strange thing is that most of the experiments that had 3 months are showing that 2850dc was the latest file which is wierd).

I'll email separately about the other runs but try this first.

