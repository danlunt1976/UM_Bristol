[Back to HadCM3_user_notes](HadCM3_user_notes.md)

The starting point for this document was [Paul's notes](https://www.paleo.bristol.ac.uk/UM_Docs/Bristol_Tech_Notes/Starting_Using_the_Hadley_Centre_Climate_Model.docx)

# Introduction

This document describes some of the aspects of using the Hadley Centre model HadCM3 and its variants (e.g., FAMOUS) on the BRIDGE servers and the University of Bristol’s HPC machines (bluecrystal and bluepebble). The Hadley Centre model is also known as the Unified Model (UM) which refers to the unification of the model for weather and climate forecasting (the weather forecast model normally uses much higher resolution that the climate version, but it is the same code base). HadCM3 corresponds to version 4.5.1 of the UM (FAMOUS is 4.5.3).

In practice, it takes a lot of time to build experience with all aspects of the system. This document is just a start, but the aim is to gradually expand the content until it is a relatively complete description of the complete system.

Unfortunately, computing platforms and software are always changing, and it is almost certain that some aspects of this document are out-of-date. It is also a developing document, and the aim is to gradually expand it. Therefore it is probably better to always access the online version, rather than having your own copy.

# Obtaining Accounts

We use a variety of different computers for running and processing climate model outputs and the first task is to obtain user accounts. Unfortunately, this is always changing so some of this information is out-of-date but it will give you some guidance.

(a) BRIDGE servers. These are used for most day-to-day analysis of model simulations. We have a number of machines, called after geological periods (eocene.ggy.bris.ac.uk, triassic.ggy.bris.ac.uk, silurian.ggy.bris.ac.uk, anthropocene.ggy.bris.ac.uk). To get an account on these machines, please contact your supervisor/PI.

(b) Bluecrystal phase4 and bluepebble. These are our main high-performance computers on which we run climate model simulations. They consist of “login nodes” and many “computer nodes”. The login nodes are called: bc4login.acrc.bris.ac.uk and bp1-login04.acrc.bris.ac.uk. To get an account on these machines, [https://www.acrc.bris.ac.uk/login-area/apply.cgi](https://www.acrc.bris.ac.uk/login-area/apply.cgi) .  Under “Project details” choose “Join an existing project” and give the code (provided by supervisor/PI).  Under “preferred log-in shell” choose bash.  In the box for additional info, you can just state “HadCM3 user”. NOTE: Also specify that you want an account on bluecrystal as well as bluepebble. The default is bluepebble only.

(c) For bluepebble only, You may also need to email them because you need to ask them to create a folder: /bp1store/geog-tropical/users/(your username). Also ask to be added to the s-tropical group. Cc [p.j.valdes@bristol.ac.uk](mailto:p.j.valdes@bristol.ac.uk) on your email since they need to confirm additions.

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

First start Xming running from the version you just installed. If this is running correctly, the
icon will appear on the right of the windows taskbar. Then open PuTTY (via ‘Start > All
Programs > PuTTY’). Fill in the host machine name on the first screen: bc4login.acrc.bris.ac.uk. To view windows sent from the host screen, you need to set up ‘forwarding’. On the left click the ‘+’ symbol next to SSH, then select X11. Tick the box to ’Enable X11 forwarding’.  Also on the left-hand menu, click on ‘Colours’ and put a tick in the box next to ‘Use system colours’.  Then click Open at the bottom of the window. When prompted enter your username. You will have been sent an email of these when you registered on the ACRC webpage. Remember to use the correct password for the machine you are using.

Once you have logged in, you will automatically be in your ‘home’ directory, and you should see the command-line prompt.

Linux requires commands to be typed at the command line (followed by the Return key). An example is `ls` which will bring up a listing of all the files and folders in the current directory. At the moment, you will have no files, so this command will produce no result. Before you start installing and running the UM, it is important to get used to some simple Linux commands. Work through ‘Tutorial 1’ here: [http://www.ee.surrey.ac.uk/Teaching/Unix/](http://www.ee.surrey.ac.uk/Teaching/Unix/) , and ensure that you are happy with listing, making, and moving between directories. Also try removing them (`rmdir DIRECTORY_NAME`).

There are many good online Linux courses, including some interactive ones, such as: [https://linuxsurvival.com/](https://linuxsurvival.com/) .

A particularly recommended course is:
[https://www.netacad.com/campaign/linux-unhatched3](https://www.netacad.com/campaign/linux-unhatched3)

Before going any further, try these online courses until you feel that you are confident using Linux.  In particular, make sure that you can write and edit text files using emacs, move around your directory structures, copy files, move files, and delete files.
