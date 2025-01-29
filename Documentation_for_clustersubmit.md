[Back to HadCM3_user_notes](HadCM3_user_notes.md)
# Introduction

**clustersubmit** is the main script that we use to submit UM4.5 (HadCM3, FAMOUS etc.) jobs to our HPC machines. It has evolved from a script called umsubmit which is distributed with the original code from the Met Office. It has been modified and extended frequently and is now a complex code. It has occasionally had major clean-ups, but further additions end up making it a rather untidy and only semi-structured script.

The **umui** database stores all of the information about a simulation. When the process button is pressed, the **umui** creates a series of files in the $HOME/umui_jobs/expt_name folder which contains all of the information needed to run the model. These files need to be copied to the HPC.  **clustersubmit** then takes these files, makes a unique copy in the umui_runs folder (changing some parameters), and submits the UM main script to run on the machine. **clustersubmit** has gradually become linked to the BRIDGE setup and is not especially transferrable to other machines and setups.

One of the key roles of **clustersubmit** is to allow the job in the umui to be independent of the target HPC machine. This is achieved by keeping to some common naming conventions within the umui. In the umui, folder and file locations are referred to using standard location names (such as /home/swsvalde or /home/username). These are then converted by **clustersubmit** to the appropriate local folder name on the relevant HPC machine  

A second role of **clustersubmit** is to swap between compile jobs, new run jobs, and continuation runs without the need to make any changes in the umui itself. In general, it makes life a lot simpler and that the copy of the job within the umui is always the compile option.

A third role of **clustersubmit** is to change the run time and number of processors, depending on the machine and queue being used. Again, this avoids the need to change these within the umui itself.

**clustersubmit** has also evolved to do a few other things too.

# Example usage

(a)    Compile job:

`clustersubmit -c y -s y -q cpu -r bc4 -P abcdef expt_name`

(b)    New simulation:

`clustersubmit -c n -s y -a y -q veryshort -r bc4 -P abcdef -p 7x4 expt_name`

(c)     Continuation simulation on bluepebble:

`clustersubmit -c y -s y -a y -q compute -r bp14 -P abcdef -p 6x4 expt_name`

# Configuration File

It is sometimes useful to set some standard defaults for the machine being used. This can be done by creating a file called: $HOME/.um/clustersubmit.conf.

Typical options are shown for a typical bluepebble configuration:

cores_ns="6"  
cores_ew="4"  
nomail="y"  
notransfer="y"  
rhost="bp14"  
queue="compute"  
account="GEOG015942"

Typical options are shown for a typical bluecrystal configuration:

cores_ns="7"  
cores_ew="4"  
nomail="y"  
notransfer="y"  
rhost="bc4"  
queue="cpu"  
account="GEOG015942"

# Argument List

| **Name**        | **Description**                                                                                                                     | **Valid Options**                                                                                               | **Default**                                                                                                               |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| -expt           | Experiment name                                                                                                                     | Any                                                                                                             | None. Compulsory                                                                                                          |
| -r              | The remote machine that will run the simulation                                                                                     | A number of short names for clusters. See note 1 for full list.                                                 | None Compulsory                                                                                                           |
| -q              | The queue to submit the job to. The name will depend on the machine. The queue name will also often impact on the default run time. | See note 2 for a list of available queues                                                                       | None. Compulsory                                                                                                          |
| -P              | Account name                                                                                                                        | Adds user account for job                                                                                       | Currently needed for bluecrystal and bluepebble. Can be set as a default using the file \$HOME/.um/clustersubmit.conf     |
| -p              | Number of cores, in the format NSxEW                                                                                                | Any but total core number must equal size of node (currently 28 cores on bluecrystalp4, 24 cores on bluepebble) | Optional. If not specified, will take value from umui job. Defaults can be set in file \$HOME/.um/clustersubmit.conf file |
| -g              | As -p but without any check on total core number.                                                                                   |                                                                                                                 |                                                                                                                           |
| -w              | Wall time                                                                                                                           | Format is: 24:0:0 (ie. 24 hrs, 0 min, 0 secs) or 14-0:0:0 (i.e. 14 days)                                        | Optional. If not specified, then maximum for the queue specified.                                                         |
| -u              | Username                                                                                                                            | Any                                                                                                             | Optional: default is the same user as submitter                                                                           |
| -F              | Force submission                                                                                                                    | Clustersubmit will check to see if there is already a job running with same name                                | Optional: Default = n, Option=y                                                                                           |
| -n              | Email output                                                                                                                        | Umui jobs can email outputs to user. This can override options                                                  | Optional: Default: same as in umui, option=y                                                                              |
| -e              | Create ensemble                                                                                                                     | It is possible to merge a number of umui jobs into a single multnode job. This can sometimes be more            | Optional: Default=n, option=y                                                                                             |
| -S              | Short hand for the best continuation run                                                                                            | Should be used for a continuation run, after compilation                                                        | Optional: Default=n, option=y<br><br>If y, then the same as:<br><br>-c y -s y -a y                                        |
| -C              | Short hand for the best settings for a compile job                                                                                  | Should be used for compile job only                                                                             | Optional: Default=n, option=y<br><br>If y, then the same as:<br><br>-c y -s y                                             |
| -A              | Short hand for new run, after compilation                                                                                           | Should be used for a new run, after compilation                                                                 | Optional: Default=n, option=y<br><br>If y, then the same as:<br><br>-c n -s y -a y                                        |
| -a              | Change compilation                                                                                                                  | This changes the job from a compile job to non-compile or vice versa.                                           | Optional: Default=n (no change) option=y (change setting)                                                                 |
| -c              | New or continuation run                                                                                                             | Changes settings to make it a new run, or continuation run                                                      | Optional: Default=n (new run)<br><br>option=y (continuation run)                                                          |
| -l              | Write data to local disk                                                                                                            | On some machines, the nodes had local disks which are a lot faster than networked disks.                        | Optional: Default=n<br><br>The option=y is currently not used because none of the machines have local disk.               |
| -m              | Rerun the reconfiguration                                                                                                           | This is an unusual option. See Note 3 for full explanation                                                      | Optional: Default=n, option=y                                                                                             |
| -s              | Submit job to queue                                                                                                                 | This is the normal option but could just create the umui_runs folder                                            | Optional: Default=y, option=n                                                                                             |
| -f              | Copy umui_job files to HPC machine                                                                                                  | We used to submit jobs from puma and it was useful to copy the umui_job.                                        | NO longer used. We can no longer submit jobs from puma due to security issues.                                            |
| -d              | Debug                                                                                                                               | This print additional information to help debugging                                                             | Optional: Default=n, option=y                                                                                             |
| -v              | Verbose                                                                                                                             | More output                                                                                                     | Optional: Default=n, option=y                                                                                             |
| -V or -h -or -? | Version                                                                                                                             | Prints some information about the script                                                                        | Optional: No inputs                                                                                                       |

## Note 1: HPC Machine Names

| **Clustersubmit name**                                       | **Full Machine Name**                                                                                                        | **Description**                                                                                                                                                                  |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CURRENT MACHINES                                             |                                                                                                                              |                                                                                                                                                                                  |
| bc4                                                          | bc4login.acrc.bris.ac.uk                                                                                                     | Latest, fourth bluecrystal machine                                                                                                                                               |
| bc4login1<br><br>bc4login2<br><br>bc4login3<br><br>bc4login4 | bc4login1.acrc.bris.ac.uk<br><br>bc4login2.acrc.bris.ac.uk<br><br>bc4login3.acrc.bris.ac.uk<br><br>bc4login4.acrc.bris.ac.uk | Submitting to bc4 would submit to a general pool of 4 machines. Occasionally, there are problems with this system so it is useful to be able to submit to specific machine.      |
| bp1                                                          | bp1-login01.acrc.bris.ac.uk                                                                                                  | Bluepebble HPC machine, using the generic head node                                                                                                                              |
| bp14                                                         | bp1-login04.acrc.bris.ac.uk                                                                                                  | Bluepebble HPC machine, using the BRIDGE head node                                                                                                                               |
|                                                              |                                                                                                                              |                                                                                                                                                                                  |
| LEGACY MACHINES                                              |                                                                                                                              |                                                                                                                                                                                  |
| quest-hpc<br><br>quest                                       | quest-hpc.bris.ac.uk                                                                                                         | Old quest machine which was a small clusters machine                                                                                                                             |
| Ormen                                                        | ormen.ggy.bris.ac.uk                                                                                                         | Small predecessor of quest machine                                                                                                                                               |
| babyblue<br><br>bc<br><br>bluecrystal<br><br>bluecrystalp1   | bluecrystalp1.bris.ac.uk                                                                                                     | The first bluecrystal machine                                                                                                                                                    |
| bigblue<br><br>bigbluecrystal<br><br>bluecrystalp2           | bluecrystalp2.bris.ac.uk                                                                                                     | The second bluecrystal machine                                                                                                                                                   |
| newblue<br><br>bluecrystalp3                                 | bluecrystalp2.acrc.bris.ac.uk                                                                                                | The third bluecrsytal machine                                                                                                                                                    |
| newblue1<br><br>newblue2<br><br>newblue3<br><br>newblue4     | newblue1.acrc.bris.ac.uk<br><br>newblue2.acrc.bris.ac.uk<br><br>newblue3.acrc.bris.ac.uk<br><br>newblue4.acrc.bris.ac.uk     | Submitting to newblue would submit to a general pool of 4 machines. Occasionall, there were problems with this system so it was useful to be able to submit to specific machine. |

## Note 2: Queue Names

On bluecrystalp4:

| **Queue Name** | **Characteristics**                                                                            |
| -------------- | ---------------------------------------------------------------------------------------------- |
| cpu            | Maximum 14 days run time                                                                       |
| test           | Maximum 1 hour run time                                                                        |
| veryshort      | Maximum 6 hour run time                                                                        |
| bridge         | Maximum 14 days run time. Limited number of nodes available. Available to selected users only. |
| paleo          | Maximum 14 days run time. Limited number of nodes available. Available to selected users only. |

On bluepebble:

| **Queue Name** | **Characteristics**                                                                            |
| -------------- | ---------------------------------------------------------------------------------------------- |
| compute        | Maximum 14 days run time                                                                       |
| test           | Maximum 1 hour run time                                                                        |
| short          | Maximum 3 days run time                                                                        |
| djl            | Maximum 14 days run time. Limited number of nodes available. Available to selected users only. |
| dmm            | Maximum 14 days run time. Limited number of nodes available. Available to selected users only. |

## Note 3: The -m option

When starting a new model simulation, before the model starts we need to reconfigure the input dump files. This step takes the input dump files, and writes out new dump files typically called \$DATAW/\$RUNID.astart and \$DATAW/\$RUNID.ostart. On some occasions, the atmosphere dump reconfiguration crashes. This mostly happens when changing land sea mask but will happen on other occasions too. The output dump file (\$RUNDIR.astart) is created but not complete. Sometimes, reconfiguration will work if you re-run the reconfiguration, but starting from the incomplete output dump file (\$RUNDIR.astart) and writing out a new dump file (e.g. \$RUNDIR.astart1). If you select the (-m y) option, this will all be done automatically.

## Note 4: Path translation

Clustersubmit will take folder names from the umui job, and translate a few standard folder names to the specific locations on the relevant machines. This allows you to use universal folder names in the umui and these do not have to be changed depending on the target machine. Currently the folders which are automatically translated are:

| Folder in umui       | Folder on bluecrystal                | Folder on bluepebble              |
| -------------------- | ------------------------------------ | --------------------------------- |
| /home/swsvalde       | /mnt/storage/private/bridge/swsvalde | /bp1/geog-tropical/users/swsvalde |
| /home/username  $^*$ | /user/name/username                  | /user/home/username               |
| ~username1 $^*$      | /user/name/username1                 | /user/name/username1              |

$^*$ Where username is the name of the user running the simulation and username1 is the name of the owner of the folder

