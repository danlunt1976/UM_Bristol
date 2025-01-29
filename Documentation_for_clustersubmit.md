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

