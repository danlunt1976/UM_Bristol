[Back to HadCM3_user_notes](HadCM3_user_notes.md)

# Running on BC5

This is a step-by-step guide to getting set up on BC5, and running simulations.
There is a [dedicated page for BC5](https://docs.isambard.ac.uk/user-documentation/faqs/bc5-launch/) on the BriCS pages.

## Creating a project

I initially set up a new project called "BC5 HadCM3" following the instructions [here](https://apply.isambard.ac.uk/bristol/) .
However, in the end I joined via an invite from SH to the 'BC5 Testing' project, and mostly you would be joining an existing project via an invitation from a PI, that arrived by email. 

## Creating an account

There are instructions on how to get an account [here](https://docs.isambard.ac.uk/user-documentation/tutorials/setup/).
In brief, go to the [BriCS portal](https://portal.isambard.ac.uk/) and choose the identify provider "University Login (MyAccessID)".
If this is your first time, choose the same linux username as you have on the BRIDGE machines, i.e. your UoB username, and accept the terms and conditions.
Note that on BC5, your username will actually be in the form USER.PROJECT . For example, mine is ggdjl.b55  . As such, ~ggdjl will not work, it has to be ~ggdjl.b55

## Logging in

There are some notes on logging in [here](https://docs.isambard.ac.uk/user-documentation/guides/login/).
In brief, only once, the first time you log in, you will need to [generate an SSH key pair](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
To do this, on miocene, I did:  
```
ssh-keygen -t ed25519
```
and renamed the file to /home/ggdjl/.ssh/id_ed25519_bc5
and set a passphrase (cd6).

bc5 uses a program called clifton to authorize usage. It generates a certificate that lasts for 12 hours before requiring renewal (you can also renew earlier if preferred). We have installed clifton in ~swsvalde/bin on our newer machines (triassic/miocene/holocene4). On our older machines, we have not done this so you will need to do the following.

Again, only once, I installed clifton in a clifton directory in my home directory:
```
mkdir clifton ; cd clifton
curl -L https://github.com/isambard-sc/clifton/releases/latest/download/clifton-linux-musl-x86_64 -o clifton 
chmod u+x clifton
```

Every time you log in to BC5, to authenticate your ssh link:
```
clifton auth --identity /home/ggdjl/.ssh/id_ed25519_bc5
```
This pops up a QR code (there was no default web browser set on miocene), which you read into your mobile phone, and log in via the webpages that pop up on your phone.
Back on miocene you then do: (you only need to do this once, the very first time you log in)
```
cd clifton
./clifton ssh-config write
```
and then
```
ssh -X -Y b55a.bc5.digital-labs
```
and you should be logged in!

The default is for you to be logged out every minute or so of not typing.  To avoid this, in .ssh/config, add these 3 lines after the Include line:
```
Include "/home/ggdjl/.ssh/config_clifton"
TCPKeepALive yes
ServerAliveInterval 10
ServerAliveCountMax 100
```

On our newer machines, there is also a script that tells you how long your certificate has before it expires:

check_certificate

## Setting up to run the UM

The home directory is relatively small (as it is on many HPC machines) so the recomendation is to have most of your folders in the bigger projects space, and then use sym links. In your home directory, once only, do the following:
```
mkdir /projects/public/b55a/ggdjl
for folder in DUMP2HOLD ancils dumps work umui_jobs umui_runs tmp ; do
   mkdir /projects/public/b55a/ggdjl/$folder
   ln -s /projects/public/b55a/ggdjl/$folder
done

mkdir DUMP2HOLD/um
ln -s /projects/public/b55a/ggdjl/DUMP2HOLD/um dump2hold

ln -s /projects/public/b56i/swsvalde
ln -s /projects/public/b56i/ggpjv/UM_HOME

ln -s UM_HOME/setvars
cp /home/b56i/ggpjv.b56i/.profile .
mkdir $HOME/.um
cp /home/b56i/ggpjv.b56i/.um/clustersubmit.conf $HOME/.um

```
Then, in the clustersubmit.conf file, change the final line to your home location. i.e.
```
home='/home/b55a'
```

ALSO, there is a line in clustersubmit which converts usernames from our normal format on triassic etc, to the more unusual format of bc5. Add your username to the existing list:
```
username_convert=("ggpjv:ggpjv.b56i" "glxaf:glxaf.b56r" "ggdjl:ggdjl.b55i")
```

## Compile and Run:

If the above changes are done correctly, then the rest should be simple. Moreover, the defaults for clustersubmit have been set so the usage can be very simple.
### compile:

```
clustersubmit -C y xqhgf
```

### run:

```
clustersubmit -c n -a y xqhgf
```



## Paul's notes from CMIP7 meeting:

### Progress with BC5 (and other machines)

* We have been given permission from the Met Office to make HadCM3 public domain software, and will be uploading it to github
* We also have access to a number of new machines (bc5, Isambard 3, Archer2) which require some changes/restructuring of the model setup
* Our CMIP7 prototype job has exceeded 100 modifications to the code
* HENCE this seems like a good opportunity to have a major refresh of the code.

### Change to the Install

* The portable unified model (PUM) was released almost 30 years ago.
* When I moved to Bristol (in 2003) I installed it on our local servers
* Shortly after we got the first bluecrystal (and our own HPC machine quest)
* All subsequent installs copied this install
* For BC5 etc, we have gone back to basics and installed from the original release (on CD’s)
* We also needed to install korn shell which is no longer standard
* On bc5, we had to do our own install of the intel compiler
* On Isambard, there is no native fortran compiler so we need to use gfortran (which converts fortran to C).
* This latter issue means that we have to use a different version of nupdate, which we have decided to use for all machines.
* On bluepebble, we will have the old and new installs.

### Changes to the umui

* Changes to the default variables name (e.g. PV_ROOT becomes BRIDGE ROOT)
* Merger of many modsets that are always used together. The original mods list:
```
$MODS/clim/vn4.4/hadam3/AMIPII/rssafehs4.4
$MODS/general/gdr1f406
$MODS/general/model_fix.mod
$MODS/general/ofilter_mpp.mod
$MODS/general/port_conv_f.mod
$MODS/general/port_end_f.mod
$MODS/general/timerupd_new.mod
$MODS_SOURCE/vn4.5/hadam3/AMIPII/diag_cld
$MODS_SOURCE/vn4.5/hadam3/asm1f406
$MODS_SOURCE/vn4.5/hadam3/ftj1f405
$MODS_SOURCE/vn4.5/hadam3/gbccf406
$MODS_SOURCE/vn4.5/hadam3/gsm1f406
$MODS_SOURCE/vn4.5/hadam3/gsm4f406.PUM
$MODS_SOURCE/vn4.5/hadam3/h3dbqlim
$MODS_SOURCE/vn4.5/hadam3/nomsrest
$MODS_SOURCE/vn4.5/hadam3/tjnowrit
$MODS_SOURCE/vn4.5/hadcm3/gdr2f406
$MODS_SOURCE/vn4.5/hadcm3/gdr3f406
$MODS_SOURCE/vn4.5/hadcm3/gsm2f406
$MODS_SOURCE/vn4.5/hadom3/osy1f405_change
$PV_UPDATES/BL_IC7A_TRANS.mod
$PV_UPDATES/abortfix.mod
$PV_UPDATES/ask1f406
$PV_UPDATES/ask6f406
$PV_UPDATES/atmstep_flush.mod
$PV_UPDATES/blkdata_buglet
$PV_UPDATES/bottom_friction_quadc_1.0e
$PV_UPDATES/boundsfix_famous.mod_xcpsa
$PV_UPDATES/boundsfix_nonmpp.mod
$PV_UPDATES/boundsfix_vn4.5.mod
$PV_UPDATES/bugfix_timer
$PV_UPDATES/buglet_cntl_io_fix.mod
$PV_UPDATES/change_dark_respiration_ver02
$PV_UPDATES/coupled/gancf407.mf77.pjv
$PV_UPDATES/dummy.mod
$PV_UPDATES/extendSTASH_SETDIR.mod
$PV_UPDATES/fix_rad.txt
$PV_UPDATES/fixfill3a.mod
$PV_UPDATES/fixmeanctl.mf77
$PV_UPDATES/fixsolang.mod
$PV_UPDATES/fixspin3a.mod
$PV_UPDATES/fixstdia.mod
$PV_UPDATES/gsm9f406_nowarning
$PV_UPDATES/gwave_varlim_001_N048.mod
$PV_UPDATES/inittime_info
$PV_UPDATES/leaf_co2
$PV_UPDATES/linuxf_mpp.mod
$PV_UPDATES/long_output_names02.mod
$PV_UPDATES/lux_open.mod
$PV_UPDATES/meadlengths.mod
$PV_UPDATES/mods/vn4.5/extras/abx0f406
$PV_UPDATES/mods/vn4.5/extras/abx1f406
$PV_UPDATES/mods/vn4.5/extras/abx2f406
$PV_UPDATES/mods/vn4.5/extras/abx3f406
$PV_UPDATES/mods/vn4.5/extras/abx4f406
$PV_UPDATES/mods/vn4.5/extras/abx5f406
$PV_UPDATES/mods/vn4.5/extras/abx6f406
$PV_UPDATES/mods/vn4.5/general/coupledfix_new.mod
$PV_UPDATES/mods/vn4.5/hadam3/mod0209
$PV_UPDATES/mods/vn4.5/hadam3/mod1702
$PV_UPDATES/mods/vn4.5/hadam3/moses2_ice
$PV_UPDATES/mods/vn4.5/hadcm3/alk_2.mod
$PV_UPDATES/mods/vn4.5/hadcm3/gbc0f406
$PV_UPDATES/mods/vn4.5/hadcm3/gps0f406.pjv
$PV_UPDATES/mods/vn4.5/hadcm3/gsm3f406.notag
$PV_UPDATES/mods/vn4.5/hadcm3/medout44.mod
$PV_UPDATES/mods/vn4.5/hadom3/gbcgf406
$PV_UPDATES/ocean/ganbf407.mf77
$PV_UPDATES/oceantracerstash.mod
$PV_UPDATES/ocn_filt.mf77.pjv
$PV_UPDATES/ocnstep_print.mod
$PV_UPDATES/pot_evap_chn_nooutput
$PV_UPDATES/pstar_smooth08_N048
$PV_UPDATES/smooth_stream_006.mod
$PV_UPDATES/solar_orbit_real1950.mod
```
has become:
```
$BRISTOL_MODS/bottom_friction_quadc_standard01
$BRISTOL_MODS/gwave_varlim_001_N048.mod
$BRISTOL_MODS/long_output_names02.mod
$BRISTOL_MODS/merge_BUGFIXES_01
$BRISTOL_MODS/merge_GENERIC_01
$BRISTOL_MODS/merge_MOSES2.1_01
$BRISTOL_MODS/pstar_smooth08_N048
$BRISTOL_MODS/smooth_stream_006.mod
$BRISTOL_MODS/solar_orbit_real1950_ver04.mod
$STANDARD_MODS/merge_STANDARD_MODS_clim_01
$STANDARD_MODS/merge_STANDARD_MODS_general_01
```

### Current Status

* Installed on bc5 and benchmarked
* Hint that terrestrial GPP failing benchmark tests but need to investigate further
* CMIP7 is prepared but crashing!
* Computer time currently available
* Probably need to ask Dann Mitchell to apply for CMIP7 project and get everyone added to project.
* Also installed on archer but no allocation given
* New version on bluepebble but currently difficult to swap between new and old system
* Aiming to install on Isambard tomorrow!

## Help etc.

BriCS Helpdesk : [https://support.isambard.ac.uk/](https://support.isambard.ac.uk/ "https://support.isambard.ac.uk/")

BriCS Documentation : [https://docs.isambard.ac.uk](https://docs.isambard.ac.uk "https://docs.isambard.ac.uk/")


## Notes from meetings with Gethin

Local linux SSH key.  Send public key to BriCS.  Run Clifton with SSH key.  Pops up webpage.  Uni account.  Webpage signs certificate.  SSH to BC5 as a group.  On a login node.  b55a project is SH's BC5 testing project.

/projects/public/b55a is install.  intel, fcm, um, swsvalde.

.profile has setvars so that correct mpi is picked up.

Project space is 20TB.  Not deleted.

current um has come from bc4.  current swsvalde has come from bc4.

On iB3 and archer, /bin/ksh installed, but not on BC5
qsmaster has been hand-edited for ksh.
In SUBMIT script, first /bin/ksh ignired as submit via 'ksh SUBMIT'
Line 193, /bin/ksh hand-edited.

account is set to empty string in clustersubmit

Permissions changed in:
/projects/public/b55a/um/pdksh/5.2.1.4 g+x
/projects/public/b55a/swsvalde/bin
/projects/public/b55a/um/PUM64/um/vn4.5/scripts
/projects/public/b55a/um/extracted_code



