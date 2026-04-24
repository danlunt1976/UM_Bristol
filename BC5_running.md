[Back to HadCM3_user_notes](HadCM3_user_notes.md)

# Running on BC5

This is a step-by-step guide to getting set up on BC5, and running simulations.
There is a [dedicated page for BC5](https://docs.isambard.ac.uk/user-documentation/faqs/bc5-launch/) on the BriCS pages.

## Creating a project

I initially set up a new project called "BC5 HadCM3" following the instructions [here](https://apply.isambard.ac.uk/bristol/) .
However, mostly you would be joining an existing project via an invitation from a PI, that arrived by email. 

## Creating an account

There are instructions on how to get an account [here](https://docs.isambard.ac.uk/user-documentation/tutorials/setup/).
In brief, login at the [BriCS portal](https://portal.isambard.ac.uk/) via "University Login (MyAccessID)".
If this is your first time, choose the same linux username as you have on the BRIDGE machines, i.e. your UoB username, and accept the terms and conditions.
Note that on BC5, your username will actually be in the form USER.PROJECT . For example, mine is ggdjl.b55

## Logging in

There are some notes on logging in [here](https://docs.isambard.ac.uk/user-documentation/guides/login/).
In brief, only once, the first time you log in, you will need to [generate an SSH key pair](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
To do this, on miocene, I did:  
```
ssh-keygen -t ed25519
```
and renamed the file to /home/ggdjl/.ssh/id_ed25519_bc5
and set a passphrase (cd6).
Again, only once, I installed clifton in a clifton directory in my home directory:
```
mkdir clifton ; cd clifton
curl -L https://github.com/isambard-sc/clifton/releases/latest/download/clifton-linux-musl-x86_64 -o clifton 
chmod u+x clifton
```
The default is for you to be logged out every minute or so of not typing.  To avoid this, in .ssh/config, add these 3 lines after the Include line:
```
Include "/home/ggdjl/.ssh/config_clifton"
TCPKeepALive yes
ServerAliveInterval 10
ServerAliveCountMax 100
```

Every time you log in, to authenticate your ssh link:
```
cd clifton
./clifton auth --identity /home/ggdjl/.ssh/id_ed25519_bc5
```
This popped up a QR code (there was no default web browser set on miocene), which I read into my mobile phone, and logged in via the webpages that popped up on my phone.
Back on miocene I then did: (you only need to do this once, the very first time you log in)
```
cd clifton
./clifton ssh-config write
```
and then
```
ssh -X -Y b55a.bc5.digital-labs
```
and you should be logged in!


## Setting up to run the UM

In your home directory, once only, set up these folders/links:
```
mkdir /projects/public/b55a/ggdjl
mkdir /projects/public/b55a/ggdjl/um
mkdir /projects/public/b55a/ggdjl/tmp

ln -s /projects/public/b55a/ggdjl/um /projects/public/b55a/ggdjl/DUMP2HOLD
ln -s /projects/public/b55a/ggdjl/DUMP2HOLD
ln -s /projects/public/b55a/ggdjl/um dump2hold
ln -s /projects/public/b55a/ggdjl work

ln -s /projects/public/b55a/swsvalde
ln -s /projects/public/b55a/um/PUM64_intel PUM64
ln -s /projects/public/b55a/ggdjl/tmp
ln -s /projects/public/b55a project

ln -s swsvalde/ancil
ln -s swsvalde/dumps

ln -s ln -s PUM64/setvars

mkdir umui_jobs

cp /home/b55a/ggdagw.b55a/.profile .
cp  /home/b55a/ggdagw.b55a/met.kshrc .

```

## Compile and Run:

### compile:
```
clustersubmit -s y -q general -r bc5 -P " " xqhgf
```
Now `cd` to ~/`umui_runs` .  Normally you would just type `ksh SUBMIT`, but for now you will either have to do some hand-edits first, or submit as above but using /home/b55a/ggdjl.b55a/clustersubmit_ggdjl in place of clustersubmit.

If you used the usual clustersubmit then will need to hand-edit the SCRIPT and SUBMIT files in the latest umui_runs folder.
In SUBMIT:
```
echo "#!/usr/bin/env ksh">/tmp/qsubmit.$thisHost.$$
```

```
qsubCmd1="/projects/public/b55a/um/bin/qsub-um -o $OUTPUT_FILE -s ksh
qsubCmd2="/projects/public/b55a/um/bin/qsub-um -o $OUTPUT_FILE -s ksh 
qsubCmd1="/projects/public/b55a/um/bin/qsub-um -o $OUTPUT_FILE -r $CJOBN -s ksh qsubCmd2="/projects/public/b55a/um/bin/qsub-um -o $OUTPUT_FILE -r $CJOBN -s ksh 
```

In SCRIPT:
```
MODSCRIPT=false         # set true to use test versions of scripts
```

You can then submit with 
```
ksh SUBMIT
```

You can check on the progress of the compile job with:
```
squeue --me
```

### run:

```
clustersubmit -s y -q general -r bc5 -P " " -a y -p 8x4 -c n xqhgf
```

And then do the same hand-edits as for compile (or use clustersubmit_ggdjl), and run in the same way.

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



