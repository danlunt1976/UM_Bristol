[Back to HadCM3_user_notes](HadCM3_user_notes.md)

# Python on the BRIDGE machines


Several of us are moving over to Python to do our post/pre-processing of UM simulations, after many years of using other languages, for example IDL, FORTRAN, NCL etc.

In order to help people make this transition, this is a brief guide to using Python on the BRIDGE machines.

## New Rocky-8 BRIDGE machines (e.g. miocene)

(1) Firstly you will need to add an 'anaconda' module. To find out what anaconda modules are available, type : ```module avail conda```
This will give you a list of available anaconda modules.  I chose the latest (actually, there was only one!).  Then add this module.  For example, for me this was: ```module add anaconda3/2023.09-0-gcc-8.5.0-wsxfmoc```
From now on in this login shell, the commands 'conda' and 'python' will be recognised, and will be self-consistent.

(2) You will need to add some initialisation stuff to your .bashrc file.  This activates some conda commands that are used later.  Type:  ```conda init bash``` 
You will see the new lines in your ~/.bashrc file.  You only need to do this once.  Once you have done this, log out and back in again, or type ```source ~/.bashrc```
You will notice that your linux command prompt now starts with '(base)'

(3) Python comes with many pre-loaded 'packages', which are basically a bunch of widely-used libraries (for example, 'numpy').  In order to be able to add some additional add-on packages, for example for reading netcdf files, and for plotting maps, you will need to load some yourself.  These additional packages are stored in an 'environment' for each user.  So, first you will need to set up an environment.  Type: ```conda create -n myenv``` 
where ```myenv``` can be any name you choose to call your environment.  Again, you only need to do this once.  You can see the result of this in ~/.conda

(4) Now, each time you want to use this environment with its additional packages, or to add packages to it, you need to activate the environment:
```conda activate myenv```
where ```myenv``` is whatever you chose to name your environment in the previous step.  You will notice that your linux command prompt now starts with '(myenv)'
To step out of this environment, type:
```conda deactivate```

(5) To add packages to this environment, once you have activated it, type:
```conda install -c conda-forge [packagename]```
For example, I have added the following packages:
```
conda install -c conda-forge netCDF4
conda install -c conda-forge matplotlib
conda install -c conda-forge cartopy
conda install -c conda-forge requests
```

(6) Now you are ready to rock and roll!  To run a python script, simply:
```python -i scriptname.py```

(7) If you would like to see a noddy python script that reads in some netcdf files and makes some plots, see ~ggdjl/rhodri/rhodri_coals.py

Good luck!!!!




