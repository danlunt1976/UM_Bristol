# Model Install

[Back to HadCM3_technical_notes](HadCM3_technical_notes.md)

# Modifying the original Portable Unified Model (PUM) Distribution

## Introduction

The Portable Unified Model was released in about 2000. It was sent out on 2 CDs with a formal license agreement that required signing before installation. One CD contained the source code, and the second had the documentation including a website.

The Met Office gave instructions on how to install the model and a configuration file that helped automate the build. The configuration script was NOT universal. It included installation options for 7 different hardware configurations which the Met Office had used, but none of these were still valid in 2026. Moreover, there were additional changes which were required. For instance, the original scripts required a particular flavour of the korn shell (called pdksh). The code was also full of copyright statements.

## Steps in Creating Github version

All of this meant that the source code needed updating. To do this, I did the following:
1) Created a home folder for the UM code. `$HOME/UM_HOME`
2) `\cd $HOME/UM_HOME`
3) `tar xvf ~swsvalde/UM/UM_DISC1/UM_SYSTEM.TAR`

I then edited the file `$HOME/UM_HOME/um/vn4.5/scripts/Install/mach_defaults` so that option 7 was for suitable for bluepebble (using intel ifx command), and option 8 became fill in all of the blanks yourself. Also added option a for archer2. There is a script `unpackmodel` which uses the mach_defaults, and I updated this to include the extra options.

Also added a script update to remove the need for pdksh, although we still need ksh. Subsequently, I discovered that the removal was not “perfect”. Specifically, the build of the scripts and the build of the standard object files did not work correctly. The core of the problem was the `echo` command, and the function `gen_sed_string`. The latter is used to create the list of objects in the makefile. It splits lines with n objects per line, followed by a backslash and a newline. This is done with one of the following lines, depending on whether you are using pdksh or normal ksh (but with echo aliased to echo -e).
```
bigstring=$bigstring'\\\\\n'$smallstring(file://n'$smallstring)
bigstring=$bigstring'\\\\\\\n'$smallstring(file://n'$smallstring)
```
For some reason, the build scripts behaved differently to the normal compile job scripts. After a lot of work (requiring a deeper dive into the scripts than I have ever done), I decided to replace the whole `gen_sed_script` function but this interacted with some of the other standard mods to the scripts. I have therefore created a new mod script called `merged_scripts`  which includes the `pdksh_remove` mod, the `remove_warnings` mod, and the `script_fix.mod`. This will work on all machines.

I then ran `unpackmodel` which created all of the files.

Inspection showed a lot of copyright statements so I wrote a script to remove these (`remove_copyright`). This was done for both the met office version of update (editing plain text files) and the cray version (had to use `nupdate` command, `create_new_update_lib`). This included modifying the source file viewer but this was a one-off (i.e. not repeated).

Also had to hand edit for the timer problem (the second command had an argument). This allowed it to compile BUT the timer code will not work currently (we rarely use it).

Also copied the gcom3.8 library from the FAMOUS github release, and removed all copyright statements (manually). Discovered small buglet in code (`2**62` needed to be `2.0**62`).

There was also a problem with a subroutine that used Holleriths in the format statement. Replaced with up-to-date character string version.

Another major problem was using the met office nupdate command. It turns out that some of our modsets would not work with this version. Again, after some investigation I found two issues (a) the met office nupdate did not like long ID names and the length varied depending on whether it was changing a COMDECK or normal DECK. (b) it also did not like a modest where there was structure such as add some code before a line (`*B xxxxx.30`) and then add some more code after the line (`*I xxxxx.30`). With the Cray nupdate, this is fine and does not even count as overlapping mods. The met office nupdate crashed. Unfortunately, one of the standard mods (gbccf406) made extensive use of such a construct and it was a tedious process to sort out. Especially since there were two versions!

Alex has already got qsub-um working, and had done the heavy lifting for the clustersubmit command. I had revamped this command and so I simply had to merge in the archer specific changes.

## Webpage work

The webpage on the PUM CD still worked but had some “features” that needed updating. All the documentation files were in postscript format. In theory, this could be easily converted to pdf format. However, some of the postscript files had bugs in them which meant that few of them would process correctly. Fortunately, postscript files are plain text and I had experience creating them from scratch (my old qplot program can produce postscript!). It was therefore possible to edit the files and get them converted to pdf format, unfortunately this had to be done manually for about 40 files!

The second job was to remove all references to the original copyright agreement and also add the new version of the copyright.

Also remove all links that referred to PUM support centre, and other links to Met Office.

Then modify the source code viewer (see above).

Finally, I did not change the Met Office logo. We will need to talk to them about whether they wish to retain this. The final webpage is here:

[http://paleo2-test.ggy.bris.ac.uk/~swsvalde/PUM_vn4.5/](http://paleo2-test.ggy.bris.ac.uk/~swsvalde/PUM_vn4.5/)
## Old notes

gcom is the hardest part of the install.  Gethin does this part.

nupdate is also a challenge.

Gethin has a cut-down version of the install.

Once the cut-down version is running, Paul modifies to make changes associated with running on different machines etc. invisible to the user, via clustersubmit.

Could put the model on github (Richard at BRICS also suggested this).

On bc4, the model code etc is here:
~ggpjv/UM_HOME , which is a link to: /mnt/storage/private/bridge/um/PUM64 , which is a link to PUM64_rocky8 .

The key code is here: /mnt/storage/private/bridge/um/PUM64_rocky8/um/vn4.5

----
18/2/2026

Gethin found the CD at home.
Plan:
1) Upload raw CD to github, once unpacked.
2) Upload Paul's changes:
	* whitsepace end of line
	* comments over lin length
	* automated makefiles (alphabetical order changed)
	* new configure file
	* get rid of pdksh
3) upload stripped copyright (keep line numbers)
4) upload new licence file
5) get rid of compiler-specific section
6) GCOM (3.1, 3.8, 2.8 ?) new version
7) Met Office nupdate , or CRAY, or Mike Blackburn
8) upload again officially and make available
9) Longer term:
	* xconv, xancil
	* Bristol scripts/infrastrucutre/libancil etc.








