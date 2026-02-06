[Back to HadCM3_user_notes](HadCM3_user_notes.md)

# Getting started with HadCM3

The starting point for this document was [Paul's notes](https://www.paleo.bristol.ac.uk/UM_Docs/Bristol_Tech_Notes/old_now_on_github_do_not_use/Starting_Using_the_Hadley_Centre_Climate_Model.docx). This itself was originally written as a guide for our undergraduate students who were carrying out dissertations using HadCM3.  You may also be interested to look at [Nils's notes](Nils_notes_for_running_HadCM3B.md)

# Introduction

This document describes some of the aspects of using the Hadley Centre model HadCM3 and its variants (e.g., FAMOUS) on the BRIDGE servers and the University of Bristol’s HPC machines (bluecrystal and bluepebble). The Hadley Centre model is also known as the Unified Model (UM) which refers to the unification of the model for weather and climate forecasting (the weather forecast model normally uses much higher resolution that the climate version, but it is the same code base). HadCM3 corresponds to version 4.5.1 of the UM (FAMOUS is 4.5.3).

In practice, it takes a lot of time to build experience with all aspects of the system. This document is just a start, but the aim is to gradually expand the content until it is a relatively complete description of the complete system.

Unfortunately, computing platforms and software are always changing, and it is almost certain that some aspects of this document are out-of-date. It is also a developing document, and the aim is to gradually expand it. Therefore it is probably better to always access the online version, rather than having your own copy.

# Obtaining Accounts

We use a variety of different computers for running and processing climate model outputs and the first task is to obtain user accounts. Unfortunately, this is always changing so some of this information is out-of-date but it will give you some guidance.

(a) BRIDGE servers. These are used for most day-to-day analysis of model simulations. We have a number of machines, called after geological periods (eocene.ggy.bris.ac.uk, triassic.ggy.bris.ac.uk, silurian.ggy.bris.ac.uk, anthropocene.ggy.bris.ac.uk). To get an account on these machines, please contact your supervisor/PI.  Note that any data put on the BRIDGE servers is not personal and will be handed over to your supervisor/PI when you leave.

(b) Bluecrystal phase4 and bluepebble. These are our main high-performance computers on which we run climate model simulations. They consist of “login nodes” and many “computer nodes”. The login nodes are called: bc4login.acrc.bris.ac.uk and bp1-login04.acrc.bris.ac.uk. To get an account on these machines, [https://www.acrc.bris.ac.uk/login-area/apply.cgi](https://www.acrc.bris.ac.uk/login-area/apply.cgi) .  Under “Project details” choose “Join an existing project” and give the code (provided by supervisor/PI).  Under “preferred log-in shell” choose bash.  In the box for additional info, you can just state “HadCM3 user”. NOTE: Also specify that you want an account on bluecrystal as well as bluepebble. The default is bluepebble only.

(c) For bluepebble only, You may also need to email them because you need to ask them to create a folder: /bp1/geog-tropical/users/(your username). Also ask to be added to the s-tropical group. Cc [p.j.valdes@bristol.ac.uk](mailto:p.j.valdes@bristol.ac.uk) on your email since they need to confirm additions.

(d) Puma2.  ”puma2” is the machine that holds a database of (almost) all Met Office Unified Model (UM) climate simulations ever carried out in universities in the UK.  It is also the machine from which we set up and submit simulations.  puma2 is now part of the Archer national computing resources. To get access to puma, you need to have an account on archer2. Instructions for access the system are here: [https://cms.ncas.ac.uk/puma2/](https://cms.ncas.ac.uk/puma2/)

I would strongly recommend that you choose the same username on puma/archer as at Bristol. It makes life simpler.

In order to access the system, you need to create a ssh-key from one of our servers. The new system allows multiple such keys. I would suggest you do this on bluecrystal but also on our BRIDGE servers. To create the key, on bluecrystal and/or BRIDGE server type:

`ssh-keygen -t rsa -f ~/.ssh/id_rsa_puma2`

The resulting key needs to be sent to archer, following the instructions in the NCAS website above.

(e) You also need access to our webpage server. Go to: [https://www.paleo.bristol.ac.uk/](https://www.paleo.bristol.ac.uk/).   This gives you access to all of our model simulations. This is almost overwhelming since over the last 30 years we have performed about 50000 simulations!!!  More details about the web page can be found here: [https://www.paleo.bristol.ac.uk/ummodel/scripts/papers/Using_BRIDGE_webpages.pdf](https://www.paleo.bristol.ac.uk/ummodel/scripts/papers/Using_BRIDGE_webpages.pdf)

There are also some help pages on our BRIDGE wiki (note that you will need to be on the university network/VPN to access this). See: [https://www.paleo.bristol.ac.uk/wiki/bridge/](https://www.paleo.bristol.ac.uk/wiki/bridge/)


# The Model Description

This paper is a description of the model, HadCM3:

[https://www.geosci-model-dev.net/10/3715/2017/gmd-10-3715-2017.html](https://www.geosci-model-dev.net/10/3715/2017/gmd-10-3715-2017.html)

Read this paper!  It will help you understand the various “flavours” of model that can be used, and their strengths and weaknesses. 

The original Met Office documentation for the model is also available.  I wouldn’t expect you to read all of this (!), but it is good to know where it is:

Old location:
http://cms.ncas.ac.uk/wiki/Docs/MetOfficeDocs
New location:
https://www.paleo.bristol.ac.uk/UM_Docs/UM_Technical_Documents/

See in particular document 070 “Specification of ancillary files” which describes how the boundary conditions for the model were originally developed – this will be useful if you come to change boundary conditions yourself.


# Learning Linux

Once you have an account on the university supercomputer (which you will only be able to log in to if you are on a UoB computer, or on the UoB VPN; see Appendix A, Working from Home) you can start learning some Linux.  Linux is an “operating system”, a bit like Windows, but it less “point and click” than Windows and is much more powerful and efficient in term of automating tasks and manipulating files.  All serious computer programmers use Linux! 

First of all, you will need to log into your account on the machine you will be using.  Logging on to Linux servers is done through a text (command line) interface called SSH. You will still be able to get Gui (graphical user interface, i.e., windows-type) programs to display as well through an environment called X11. The programs ‘PuTTY’ (the SSH client) and ‘Xming’ (the X11 environment for Windows) should already be installed on your UOB PC. 

If not, you could try logging into the student remote desktop, instead of directly via your PC:

[https://www.bristol.ac.uk/it-services/advice/homeusers/remote/studentdesktop](https://www.bristol.ac.uk/it-services/advice/homeusers/remote/studentdesktop)

(See Appendix A on working from home).

However, the version of Xming on the standard UoB machines does not always work correctly.  As such, you will first need to install the free Xming package that can be found at:

[https://sourceforge.net/projects/xming/files/Xming/6.9.0.31/Xming-6-9-0-31-setup.exe/download](https://sourceforge.net/projects/xming/files/Xming/6.9.0.31/Xming-6-9-0-31-setup.exe/download)
also download and install the Xming fonts:  
  
[https://sourceforge.net/projects/xming/files/Xming-fonts/7.7.0.10/Xming-fonts-7-7-0-10-setup.exe/download](https://sourceforge.net/projects/xming/files/Xming-fonts/7.7.0.10/Xming-fonts-7-7-0-10-setup.exe/download)

First start Xming running from the version you just installed. If this is running correctly, the icon will appear on the right of the windows taskbar. Then open PuTTY (via ‘Start > All
Programs > PuTTY’). Fill in the host machine name on the first screen: bc4login.acrc.bris.ac.uk. To view windows sent from the host screen, you need to set up ‘forwarding’. On the left click the ‘+’ symbol next to SSH, then select X11. Tick the box to ’Enable X11 forwarding’.  Also on the left-hand menu, click on ‘Colours’ and put a tick in the box next to ‘Use system colours’.  Then click Open at the bottom of the window. When prompted enter your username. You will have been sent an email of these when you registered on the ACRC webpage. Remember to use the correct password for the machine you are using.

Once you have logged in, you will automatically be in your ‘home’ directory, and you should see the command-line prompt.

Linux requires commands to be typed at the command line (followed by the Return key). An example is `ls` which will bring up a listing of all the files and folders in the current directory. At the moment, you will have no files, so this command will produce no result. Before you start installing and running the UM, it is important to get used to some simple Linux commands. Work through ‘Tutorial 1’ here: [http://www.ee.surrey.ac.uk/Teaching/Unix/](http://www.ee.surrey.ac.uk/Teaching/Unix/) , and ensure that you are happy with listing, making, and moving between directories. Also try removing them (`rmdir DIRECTORY_NAME`).

There are many good online Linux courses, including some interactive ones, such as: [https://linuxsurvival.com/](https://linuxsurvival.com/) .

A particularly recommended course is:
[https://www.netacad.com/campaign/linux-unhatched3](https://www.netacad.com/campaign/linux-unhatched3)

The ACRC also provides some training courses and tutorials, including HPC, Linux, Python and R, etc. You can take a look here: [ACRC Training](https://www.bristol.ac.uk/acrc/training/)

Before going any further, try these online courses until you feel that you are confident using Linux.  In particular, make sure that you can write and edit text files using emacs, move around your directory structures, copy files, move files, and delete files.


# Setting up your Linux environment

Now that you are familiar with Linux, you can finish setting up access to your accounts. You only need to do this ONCE. It is important that you follow the instructions precisely and in the order that they are listed. If you are not using bluepebble, skip all commands related to it.

WARNING: The script setup_system overwrites a number of existing files. If you are a new user, this is correct. If you are an existing user, you may wish to avoid using the script but you might want to look at what the script does and mimic it.

One of the key things is to set up ssh keys so that we can move files around between systems without the need for a password. We do this for all machines within the University of Bristol domain. It is **very important** that you follow these instructions precisely. When you have completed the bluecrystal/bluepebble/eocene ssh key setups, test to see if it works by trying to logon from one machine to another (e.g. from eocene type: `ssh bc4`). If successful, then you will not need a password.

These are the commands for different machines, to be done in the following order:

### (a) bluecrystal

Login to bluecrystal (bc4login.acrc.bris.ac.uk). Standard folder and paths can then be created by typing:

`~ggpjv/swsvalde/etc/setup_system`

Press return (default yes) for all questions.

This sets ups all the relevant files, paths and directories that are required to run the UM. It also creates a number of default files (e.g. .profile, .bashrc) which as you become more knowledgeable, you may want to edit. It also includes setting up short machine names for transferring files between machines. Specifically, bc4login.acrc.bris.ac.uk becomes bc4, bp1-login04.acrc.bris.ac.uk becomes bp14, and all of the BRIDGE servers can be used as their short name (i.e., eocene rather than eocene.ggy.bris.ac.uk). See $HOME/.ssh/config for full list of short names.

ssh keys are setup by:
```
cd $HOME/.ssh
ssh-keygen -t rsa -b 2048 -f ~/.ssh/id_rsa
```
Press return for all questions (DO NOT ENTER A PASSPHRASE).
```
chmod 400 ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
ssh-copy-id -i ~/.ssh/id_rsa bp14
ssh-copy-id -i ~/.ssh/id_rsa eocene
```

### (b) bluepebble

Login to bluepebble (bp1-login04.acrc.bris.ac.uk ). Standard folder and paths can then be created by typing:

`~ggpjv/swsvalde/etc/setup_system`

Press return (default yes) for all questions.

The script does a similar role to that on bluecrystal, but folder locations are different.

Setting up ssh keys is similar:
```
cd $HOME/.ssh
ssh-keygen -t rsa -b 2048 -f ~/.ssh/id_rsa
```
Press return for all questions (DO NOT ENTER A PASSPHRASE).
```
chmod 400 ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
ssh-copy-id -i ~/.ssh/id_rsa bc4
ssh-copy-id -i ~/.ssh/id_rsa eocene
```

### (c) eocene

Login to Eocene (eocene.ggy.bris.ac.uk). Standard folder and paths can then be created by typing:

`~swsvalde/etc/setup_system`

Press return (default yes) for all questions.

(NOTE the different folder address above)

The script does a similar role to that on bluecrystal, but folder locations are different.

Setting up ssh keys is similar:
```
cd $HOME/.ssh
ssh-keygen -t rsa -b 2048 -f ~/.ssh/id_rsa
```
Press return for all questions (DO NOT ENTER A PASSPHRASE).
```
chmod 400 ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
ssh-copy-id -i ~/.ssh/id_rsa bc4
ssh-copy-id -i ~/.ssh/id_rsa bp14_
```

### (d) archer2/puma2

You should have already setup the ssh keys as part of the registering process for archer2/puma2. You can add further keys from different machines if you would like. There are also instructions at NCAS for making the logging on puma2 from archer2 password less.

To log into puma2, log into eocene, and then type (you only need to do this once per eocene session):

`eval $(ssh-agent); ssh-add ~/.ssh/id_rsa_puma_`

you should now be able to log into archer2/puma2 from eocene, by typing:

`ssh archer2`

On archer2, create a symbolic link:

```
cd $HOME
ln -s /home/n02/n02-puma/$USER/umui_jobs
```

then

`ssh puma2`

Once logged on to puma2, type:

`~swsvalde/etc/setup_system`

Press return (default yes) for all questions.

The script does a similar role to that on bluecrystal but folder locations are different.

This has now completed the setup of all of the machines that are required. You only need to do this once.


# Advanced Computing Research Centre

You should also make yourself familiar with the ACRC webpages:

https://www.bristol.ac.uk/acrc/high-performance-computing/hpc-documentation-support-and-training/


# Overall Summary of running and processing the Unified Model

Climate is the average (and other statistics) of weather. The World Meteorological Organisation defines climate as the 30-year statistics of weather, although there is no scientific basis for the use of 30 years. Frequently, researchers working on modern climate choose a shorter period (10 or 20 years). This allows for a more rapid updating of climate to reflect recent changes but means there is more natural variability in the signal (there is a lot of natural, unforced variability of weather and climate). Lovejoy (2013, 2018) suggests that there is a scientific rationale for using 100 years as the averaging period.

A climate model works by simulating day-to-day weather and then treating the resulting output in the same way as real weather. Climate (and other statistics) are calculated from the model simulated weather. The internal time step of the atmosphere (and land surface) model is typically about 30 minutes. The internal time step of the ocean is typically about 1 hour and, in theory, we could output simulated weather at this frequency. However, this would produce a huge amount of output.

In many cases, we do not know the initial state of the climate system, so we often must arbitrarily initialise the state of the atmosphere, ocean, and land surface and then wait until the model reaches a dynamic equilibrium. The atmosphere rapidly comes into equilibrium (within a decade or two). The land surface (especially the deep soil moisture) takes a few decades more. Vegetation can take several centuries to a millennium (boreal forests are slow to grow). The surface ocean responds within a century or two, the deep ocean can take several thousand years (as can ocean biogeochemistry). Hence, we normally run the model for a 'spinup' period to allow the model to reach a dynamic equilibrium and then perform averaging (and other statistics) on a final segment.

For a detailed description of the HadCM3 workflow following an example, see [Example_HadCM3_workflow](Example_HadCM3_workflow.md).


# Other documentation

Here is documentation for some of the key scripts/processes:

[Documentation for clustersubmit](Documentation_for_clustersubmit.md)

[Documentation for ensembles](Running_Ensembles_on_bluecrystalp4.md)

