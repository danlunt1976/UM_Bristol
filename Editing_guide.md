# Editing Guide

## Introduction

Our aim is to generate documentation that is useful, and remains useful in the future.  As such, it 
needs to be in a format which (a) all users can easily contribute to, and (b) is future-proof.

We have decided to use a combination of 'markdown' (the file format) and 'github' (the version control system).  This combination is standard for large code documentation.  

Markdown files are raw ascii text files, with some very basic formatting.  The idea is that it is easy to write, updates/changes are easily viewable, and should be relatively future-proof.  Here is a guide to some basic markdown syntax: [https://www.markdownguide.org/basic-syntax/](https://www.markdownguide.org/basic-syntax/ "https://www.markdownguide.org/basic-syntax/") . 

Github is a version control system which is very popular for maintaining code and documentation.  You can read more about github [here](https://github.com/about).    

## Reading the documentation

The documentation files are automatically pushed to a webpage, which is here:
[https://danlunt1976.github.io/UM_Bristol](https://danlunt1976.github.io/UM_Bristol "https://danlunt1976.github.io/UM_Bristol")

You can also read the pages directly on github, here: https://github.com/danlunt1976/UM_Bristol . Start by clicking on the "README.md" file, which is the entry point: https://github.com/danlunt1976/UM_Bristol/blob/main/README.md


## Writing the documentation

The documentation will be most useful if everyone can contribute to writing and maintaining it.  

In order to contribute, you will need an account on github. Apply here for a (currently!) free account:  https://github.com/signup .  Once you have an account on github (see above), email Dan Lunt <d.j.lunt@bristol.ac.uk> with your github username, and he will invite you to be a collaborator.  You will then have edit-rights. 

### Easiest entry-point for writing documentation

(1) Once logged into your github account, go to the web interface for the documentation repository:
https://github.com/danlunt1976/UM_Bristol 

(2) Click on one of the .md files

(3) Click on the pencil icon above the file text ('Edit this file').

(4) Make some edits.

(5) Click on the green button "Commit changes..."

(6) Write a "Commit message" in the upper box, and leaving "Commit directly to the main branch" selected.

(7) Click on "Commit changes"

(8) Have a beer.


### More advanced writing (from a Windows machine)

Instead of editing the wiki directly as above, you can download a 'clone' of the repository to your local machine, and edit it there, and then 'push' back to the main repository.  Before 'pushing' you should 'pull' form the main repository, to ensure that you do not overwrite or clash with anyone else's changes.  You can do this pushing and pulling using the 'Github Desktop' app.  The main benefit of editing locally is that you can take advantage of some nice tools for writing and viewing markdown files and sites.  One such editing tool is 'Obsidian'.  Here are some instructions:

(1) Download the 'GitHub Desktop' app for Windows: https://desktop.github.com/download/

(2) Clone a copy of the repository, following these instructions: https://docs.github.com/en/desktop/adding-and-cloning-repositories/cloning-a-repository-from-github-to-github-desktop .  You can choose anywhere on your local filesystem to hold your local copy.

(3) You can edit the .md files in your local copy using whatever editing sofware you wish (e.g. Wordpad).  However, to have access to some useful tools, you can use a specific markdown file editor.  One example is Obsidian.  Download it to your desktop here:  https://obsidian.md/download .   Open Obsidian and click on 'Open folder as vault'.  It should then be fairly intuitive how to edit files.

(4) Once you have finished editing, re-open GitHub Desktop.  Click on 'Fetch origin' to 'pull' any changes that anyone else has made.  Then write a comment in the 'Summary' box, and then click on 'Commit to main'

(5) Click on 'Push origin'

(6) Have another beer.

### Even More advanced writing (from a Windows machine)

Instead of 'GitHub Desktop', you can download 'Git Bash'. This is a bit like having a linux version of your windows files, and allows you to use git commands at the command line. See [instructions here](https://bristol-training.github.io/ukrn-intro-git-github).

#### 1. Configuration on Git Bash
**To be simple**, there are two ways to configure a local repo [branch `main` in git] (see repo on github as a remote repo [branch origin/main in git]):

- Create a repo directly on local desktop, and make edits, then create a repo on GitHub and add the remote repo on local directory.
  
  1. Create a new directory using git bash:
  
  `mkdir new_repo`

  2. Create new files and commit:
  ```
  echo "# Create a new repo." >> README.md
  git init
  git add README.md
  git commit -m "first commit"
  git branch -M main
  ```
  3. Create a remote repo on GitHub:
    - Add a new repo on Github (logon GitHub, click `Repositories` under the account on top left, and then click the green button on top right, or the plus sign to create a new repository)

    - On the following page, type the name of the repository, e.g., `new_repo`
  4. Link local and remote repo, on git bash:
  ```
  git remote add origin https://<GitHub_account>/new_repo.git
  git push -u origin main
  ```

- Clone from an existing repo from GitHub.
  
  1. Choose a directory where you want to fetch a remote repo on GitHub
  2. Fetch a remote repo
   
  `git clone https://<GitHub_account>/new_repo.git`

  3. Then hopefully you will have permission to commit changes and push to the remote repo, if not, it will be more complicated. Then you will need to ask for permission or you need to fork the repo, and then clone the repo under your account.

> [!NOTE]
> Git and GitHub
> Git is a version control system written by **Linus Torvaldes** (generally speaking, the creator of Linux), which works locally, tracks changes to files, and manage versions of project (directories) over time. Remember these multiple versions are all stored on your disk, and if you want to backup a git directory, you might want to zip (or tar) it into a zip file (or tarball), and then copy that file to another computer, a USB driver, or upload it to network storage (e.g., DropBox, OneDrive, Google Drive).
> Since this is not very convenient, we can choose to back up mannually using git backup services (e.g., GitHub, GitLab, and BitBucket) that store a backup of the `.git` folder (managing multiple git versions under the gitted directory).

#### 2. Make changes and commit

Before we make changes, just one more step to set up the local repo:

To set commit email address:

`git config user.email xxxxx@bristol.ac.uk`

To set commit user name:

`git config user.name xxxxx`

Then we can create/edit/remove files. You can use whatever editors you prefer, e.g., nano (simple), vi (powerful but has a learning curve), or VSCode (powerful and intuitive, would recommend this).

After making changes, we need to notify git to track changes on this file, instead of saying "*Git, if you wouldn't mind terribly, could you please consider staging these fine changes for the next commit? Much obliged.*", we do:

`git add .` or `git add <filename>`

Then we need to commit changes to make a new version of this repo, instead of saying "*Git, when you have a moment, might I trouble you to record these changes in the grand ledger of project history? A modest message follows, of course.*", we do:

`git commit -m 'Added feature X.'`

Lastly, it is time to upload changes to the remote repo, instead of saying "*Git, ever so sorry to intrude — would you be kind enough to convey my local efforts to the esteemed remote repository? It would mean the world.*", we do:

`git push origin main`


### From a MAC

Gitting from a MAC is not that different with Gitting from a windows or linux, but tools are different. On a MAC, no Git Bash is needed, default zsh from Terminal would be enough to access a remote host, and this mirrors what you do on a WSL on Windows (for Graphics application we need something different, XQuartz, and add an X flag when ssh to a host). So the workflow of VSCode (if you rely on it) doing the editing and Git Bash do the submitting works seamlessly here on a MAC.

If you are unsure about this, I (Yousheng) am more than willing to help.


### From a Linux machine.

Also definitely possible.  I have local repositories on eocene that Greg set up, for my code repositories.  I (Dan) have some notes on this if anyone is interested (and then you can update these instructions!).

Thanks Greg and Dan, I (Yousheng) have reviewed these notes and it has been helpful. Bad news is, we unfortunately cannot configure local repos on BRIDGE machines anymore because the system is too old and the SSH keys are identified by GitHub as unsecure since 2021. See [details here](https://github.blog/security/application-security/improving-git-protocol-security-github/). Good news is, we can set this on bluecrystal and bluepebble, or new BRIDGE machines.

Different from set up on windows using Git Bash (we used https), we need access through SSH kaypairs (use ssh). We only need to do this once, on bc4:
```
ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_github
passphrase:xxxxxx
```
on GitHub: profile > setting > ssh and gpg > New ssh key, copy from id_github.pub and paste.
on bc4:
create confit file in `~/.ssh`: `touch ~/.ssh/config`
and edit `config`:
```
Host github.com
    HostName = github.com
    User = git
    Identityfile = ~/.ssh/id_github
    ForwardX11 = no
```

Then you can config local repo follow the steps listed under [Git Bash](#even-more-advanced-writing-from-a-windows-machine).

Maybe also slightly differently, when set up user.name and user.email, we could add the `--global` flag. 
> Without it, you have to set it once per repos per machine. With it, you have to set it up once per machine. But if you have to use a different remote server with different settings, you will have to use a local setting for that repo if that makes sense.

Some more useful commands:

`git status` lists all files and says which are tracked

`git status -uno` lists files which have changed compared with repo

`git diff FILE` file difference

`git ls-files` lists all files which are tracked

Again, there are courses from the University, for beginners and advanced users.

