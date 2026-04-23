[Back to HadCM3_user_notes](HadCM3_user_notes.md)

# Running on BC5

This is a step-by-step guide to getting set up on BC5, and running simulations.

## Creating an account/project

I initially set up a project called "BC5 HadCM3" following the instructions [here](https://apply.isambard.ac.uk/bristol/) .
However , mostly you would be joining an existing project via an invitation that arrived by email. 

There are instructions on how to get an account [here](https://docs.isambard.ac.uk/user-documentation/tutorials/setup/).

Login at the [BriCS portal](https://portal.isambard.ac.uk/) via "University Login (MyAccessID)".
If this is your first time, choose the same linux username as you have on the BRIDGE machines, i.e. your UoB username, and accept the terms and conditions.

There is a [dedicated page for BC5](https://docs.isambard.ac.uk/user-documentation/faqs/bc5-launch/) on the BriCS pages.


## Gethin's notes

Local linux SSH key.  Send public key to BriCS.  Run Clifton with SSH key.  Pops up webpage.  Uni account.  Webpage signs certificate.  SSH to BC5 as a group.  On a login node.  b55a project is SH's BC5 testing project.
/projects/public/b55a is install.  intel, fcm, um, swsvalde.
.profile has setvars so that correct mpi is picked up.
Project space is 20TB.  Not deleted.
current um has come from bc4.
current swsvalde has come from bc4.
On iB3 and archer, /bin/ksh installed, but not on BC5

In SUBMIT script, first /bin/ksh ignired as submit via 'ksh SUBMIT'
account is set to empty string
Line 193, /bin/ksh hand-edited.
hand-edit /bin/ksh becomes ksh

In SCRIPT, MOSCRIPT=TRUE normally.  Gets scripts out of script library via nupdate.
MODSCRIPT=false gets scripts from hard copy. 
qsmaster has been hand-edited for ksh.

When project comes in, I will make sure i can log in and see Gethin's project, then we meet for me to set up a simulation.


## Logging in

There are some notes on logging in [here](https://docs.isambard.ac.uk/user-documentation/guides/login/).
You will need to [generate an SSH key pair](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
To do this, on miocene, I did:  
```
ssh-keygen -t ed25519
```
and renamed the file to /home/ggdjl/.ssh/id_ed25519_bc5
and set a passphrase (cd6).
I installed clifton in a clifton directory in my home directory:
```
curl -L https://github.com/isambard-sc/clifton/releases/latest/download/clifton-linux-musl-x86_64 -o clifton 
chmod u+x clifton
```
To authenticate my ssh key:
```
clifton auth --identity /home/ggdjl/.ssh/id_ed25519_bc5
```
This popped up a QR code, which I read into my mobile phone, and logging in.
Back on miocene I then did: (I probably only need to do this once)
```
./clifton ssh-config write
```
and then
```
ssh b55a.bc5.digital-labs
```
and I was in!

## Setting up to run the UM

In my home directory:
```
ln -s /projects/public/b55a/swsvalde
mkdir /projects/public/b55a/ggdjl
mkdir /projects/public/b55a/ggdjl/um
mkdir /projects/public/b55a/ggdjl/tmp
ln -s /projects/public/b55a/ggdjl/um /projects/public/b55a/ggdjl/DUMP2HOLD
ln -s /projects/public/b55a/ggdjl/DUMP2HOLD
ln -s swsvalde/ancil
ln -s swsvalde/dumps
ln -s /projects/public/b55a/um/PUM64_intel PUM64
ln -s ln -s PUM64/setvars
ln -s /projects/public/b55a/ggdjl/tmp
ln -s /projects/public/b55a project
```


## Help etc.

BriCS Helpdesk : [https://support.isambard.ac.uk/](https://support.isambard.ac.uk/ "https://support.isambard.ac.uk/")

BriCS Documentation : [https://docs.isambard.ac.uk](https://docs.isambard.ac.uk "https://docs.isambard.ac.uk/")









