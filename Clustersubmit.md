[Back to HadCM3_technical_notes](HadCM3_technical_notes.md)

Clustersubmit edits the submit scripts on the fly for a specific machine.

Streamlined as possible.

Still has weird pdksh.

Some user-specific bits.

Paul has documented this - see webpages.  Need to shift this onto github/markdown at some pont.


See copy from [webpages](http://paleo-wikis.ggy.bris.ac.uk/wiki/bridge/Computing/ClustersubmitOptions2013?from=Computing.ClustersubmitOptions) as below: 

# Clustersubmit options

clustersubmit [-a y|N] [-c y|N] -d [-f y|N] -h [-l y|N] [-m y|N] [-p NSxEW] [-q queue_name] [-r remote_host] [-s y|N] [-u user-name] [-v] [-V] [-w walltime] experimentname

## OPTIONS

-a y|N

In the normal process of running a job, the first submission is to compile the job, and the second turns off compilation and runs the model. This can be done in the umui but the -a option allows you to turn off compilation simply by setting -a y. Thus there is no need to modify the umui settings.

-c y|N

If y set the job to start as a continuation run. Setting this to n will start the job as a new run. The default, if this flag is not set, is to start a new run.

-d

Display some debugging informations. Use only if the script is not behaving properly or exits with an error.

-f y|N

If -f y, then the umui_jobs/exptname folder will be copied to the remote machine. This will then allow you to resubmit the job from the remote machine.

-h

Prints usage information and exits. All other options will be ignored.

-l y|N

On bluecrystalp2, the disks can be very slow and it is better to get the job to write output to the local disks on the actual compute nodes and then copy the resulting files back to the main disk. -l y turns this on. Note that you also have to establish a crontab to copy the files back. See
http://www.paleo.bris.ac.uk/wiki/bridge/Computing/UMretrievelocaldata

-m y|N

When using FAMOUS, there is a strange problem when you change land sea masks in that the first attempt at reconfiguration fails but, if you then set the start dump to be the output from the first incomplete attempt (often called exptname.astart) and set the output for the reconfiguration to be exptname.astart1, then it all works. Rather than change this in the umui, you can also do this by setting -m y.

-p mxn

Sometimes you want to change the total number of cores to be used. This is often useful if you are testing something and can use only a few cores (which will queue for shorter time). Hence the -p option overrides the settings from the umui. So if you run with -p 4×2 then the job will divide the NS direction into 4, and the EW direction into 2. Thus requiring 8 cores in total.

-q queuename

Specifies the queue to which your run will be added to on the remote host. Typical names are veryshort, short, medium, and long (quest-long for quest machine). If not specified, the default queue is long.

-r remote_host

Specifies the remote host to which the job should be sent. It can currently be one of:
quest (alternative name quest-hpc)
bigblue (alternative names bluecrystalp2 or bigbluecrystalp2)
newblue (alternative name bluecrystalp3).
babyblue (alternative names bc or bluecrystal)
In addition, if there are technical problems it is sometimes useful to be able to submit to specific head nodes on the machines. Currently quest1, quest2, bigblue1, bigblue2, bigblue3, bigblue4, newblue1, newblue2, newblue3, newblue4 are allowed.
If this option is omitted, the default will be set to quest-hpc

-s y|N

If y the script will automatically submit the SCRIPT script on the remote_host. This will, depending on your settings, either compile your job or send it to the queueing system

-u username

Specifies the username on the remote host. Only required of the username is different to that on the machine running clustersubmit. Therefore default is the current username.

-v

Verbose output. Explains what is being done step by step.

-V

Prints version and usage information and exits. All other options will be ignored.

-w walltime

Sets the job walltime. It should be in the format [Days:][Hours:][Minutes:]Seconds. Be aware that the entered time must be allowed by the queueing system for the specified queue. The default is the longest time allowed for the chosen queue.

experiment_name


Name of the UM experiment you want to run. This is mandatory. The script will exit with an error if not provided or if the name is invalid.
In addition, you can set the default behaviour of many of these switches by creating a file called ~/.um/clustersubmit.conf, and change the preferred defaults for each machine by creating a file called ~/.um/quest-hpc.conf etc. However, these options are rarely used. Probably the most useful is if you have COPY=1 in the clustersubmit.conf file, then this is equivalent to -f y, i.e. all jobs get copied to the remote machine so that subsequent re-submissions can be done on these machines.
