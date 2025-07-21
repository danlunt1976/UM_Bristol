[Back to HadCM3_technical_notes](HadCM3_technical_notes.md)

# Conversion to New Operating System (Rocky8)

See also notes on [Local Hardware](Local_hardware)

The BRIDGE servers have been using a very old operating system (CentOS6) which is no longer maintained, and hence we no longer get up-to-date security patches. This is a serious security risk for the university and ourselves. The age of the operating system was also impacting on software, where some python codes did not work on our old system.

We have therefore got to transition to a more modern operating system (called Rocky 8.10, or Rocky8 for short). We are also transitioning to IT support for our systems which has resulted in some further changes.

In addition  to these changes, our home disk server (eocene) is very old and needed replacing (to eocene2). Similarly, the webserver (where all of the HadCM3 output is stored) needed more disk space and we got a new machine to support this.

We have converted a number of machines to the new operating system. These machines are:

(a)   **eocene2**:  new machine holding our home server (you are no longer able to logon to the home server)

(b)   **miocene**: general purpose server

(c)   **paleocene**: new machine holding webdata. Ultimately it will also run the web software but transition has not been completed.

(d)   **triassic**: old machine, mainly used for downloading and processing of HadCM3 simulations

(e)   **holocene4**: old and currently general purpose but likely to become another download/processing machine because triassic is very old and may be turned off at some point.

There are two machines which have not been converted:

(a)   **silurian**: another server download/processing of HadCM3

(b)    **anthropocene**: server mainly used by the climate group

The final machine, **eocene,** our current home server, will be soon turned off (once the transition has been completed).

Users now need to transition to the new machines. Unfortunately, we cannot do this automatically and users will have to do a fair amount of work. The following summarises the changes to the new system and some of the steps required. Please NOTE that it is strongly suggested that after making the transition, you do NOT use the old system again (unless you are really an expert). The final machines (silurian and anthropocene) will be converted, and eocene turned off, soon after everyone has converted.

## Changes for the New system

(1)   eocene2 is our new /home server. It holds all the home directories. HOWEVER, we cannot logon to this machine. All other machines access the eocene2 disk.

(2)   Our home directory names have changed. It used to be /home/bridge and is now /home (i.e. for the swsvalde user, /home/bridge/swsvalde becomes /home/swsvalde).

(3)   Most software is now installed using the module command (as used on bluecrystal and bluepebble). To see what is available type: module avail. To load a chosen module: module load xxx.

(4)   Our large disks are now automounted and in a different location to the old system. e.g previously /export/triassic/array-01  is now /scratch/triassic and similarly for the other disks.   The automounting means that the mount will timeout if not used BUT will be automatically remounted when the disk is accessed.

(5)   Similarly the RDSF disks are now mounted on /projects

(6)   We have transitioned to the new intel fortran compiler, which is called ifx rather than ifort.


## Transferring to the New Machines

Because of the above changes, it was decided NOT to automatically migrate users onto the new system. Instead, you must do this yourselves. Here are the required steps:

(1)   Tidy up your home folders on eocene.  This is a good opportunity to get rid of unwanted data, and this will speed up the process of moving.  Make sure you check the 'hidden' directories that start with a '.', as these can contain a lot of files.

(2)   Logon to a converted machine (e.g. miocene). (NOTE that you cannot logon to any of the new machines from the old machines. You must open a new terminal window).

(3)   Copy your files from eocene to eocene2. There are multiple ways of doing this but the simplest (and strongly recommended method) is using rsync. To use this, logon to miocene and then type:  
`rsync -vrltp eocene:/home/bridge/$USER/. $HOME` 

(4)   You need to create new .bash_profile and .bashrc files. I add the more common module load commands into the bash_profile file. If you feel expert, feel free to make your own changes. However, you might want to use the 'setup_system' command (this creates a reasonable bash_profile and bashrc file, as well as a few standard links etc.) Simply type:  
`~swsvalde/etc/setup_system`

(5)   You need to create new ssh keys, if you need them, and especially if you use the download system to run HadCM3.  These are the commands (make sure you are precise about this, it is easy to make a typo error that invalidates whole process):  
`cd $HOME/.ssh`  
`ssh-keygen -t rsa -b 2048 -f ~/.ssh/id_rsa`  
Press return for all questions (DO NOT ENTER A PASSPHRASE).  
`chmod 400 ~/.ssh/id_rsa`  
`cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys`  
`ssh-copy-id -i ~/.ssh/id_rsa bc4login.acrc.bris.ac.uk`  
`ssh-copy-id -i ~/.ssh/id_rsa bp1-login04.acrc.bris.ac.uk`  
Note that you may need to edit your ~/.ssh/known_hosts file on the new BRIDGE machine, by removing reference to the remote machine, if prompted 

(6)   Change any broken symlinks to reflect the changes from /home/bridge to /home

(7)   Similarly, change any scripts/code which use /home/bridge.

(8)   If usign github, you will need to reset your config files, e.g. I used
`git config user.name "Dan J. Lunt"`  
`git config user.email d.j.lunt@bristol.ac.uk`


## Download System (for HadCM3 users of bc4/bp14)

There are a few changes to the download system. These will be notified shortly.

