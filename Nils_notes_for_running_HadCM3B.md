# Preliminary steps HadCM3
- Get accounts (archer2, puma, bc, bp, bridge servers)
- Set up ssh-keys
- Start umui (note for ubuntu users: fonts-terminus-otb package needed for proper rendering)

# Create new job on puma
- Start umui
- Search --> Filter: owner
	- swsvalde: standard configurations of differenct HadCM3B versions
		- tdem --> HadAM standard with dyn veg (PI)
		- tdaa --> HadCM3 with dyn veg (PI)
	- USERNAME: my experiments
- Experiment --> new: create experiment code (4 letters) with some description
- Select reference job (not experiment but job within experiment) and new experiment
- Job --> copy: select identifier for job (5th letter in the job code) and description
- This creates new job in the new experiment
- File --> open read/write: this opens new window in which simulation can be further configured (mods = code modifications compared to vn4.5.1, ancil = boundary conditions, initial conditions, parameters)
	- "Model Selection --> Sub-Model Independent --> Compilation and Modification": Select mods and compile options (Modifications for the model --> relevant mods for model updates / bug fixes)
		- for compile options use: "Compile and build the executable named below, then stop" is standard ("Run from existing executable" rare alternative, because running new job with existing executable is normally done on different level where it's faster to update the specifications you want to change than to click through the whole umui configuration gui)
		- e.g., "Modifications for the model" --> abx0f406 --> change MOSES1 to MOS2.1
	- "Model Selection --> Sub-Model Independent --> Ancillary reference time": Set reference time for boundary conditions (usually 1849-12-1 for PI, as simulations tend to start on Dec 1)
	- "Model Selection --> Sub-Model Independent --> Starte Date and Run Length Options": Set start date (this can be a random year for all simulations with fixed orbit, as orbit time is specified somewhere else, typically 1850-12-1; for transient orbit there is option to use offset to have negative years for orbit calculation but still use positive years in output files), and run length (typically 100yr + 1 months for the initial December which exists to still have 100 DJFs in 100 yr simulations)
	- "Model Selection --> Atmosphere": Specific Atmosphere:
		- "Model Selection --> Atmosphere --> Section by section --> Vegetation" allows configuring some vegetation parameters
		- "Model Selection --> Atmosphere --> Ancillary and input data files": boundary conditions
		- "Model Selection --> Atmosphere --> STASH": output specification (define diagnostics, i.e., variable, time averaging, usage)
		- "Model Selection --> Atmosphere --> STASH --> STASH. Specification of Diagnostic requirements --> Diagnostics" --> Load diagnostics to add new variable, then specific time, domain and usage
		- After modifications run "Diagnostics --> Verify Diagnostics" to check for potential errors
	- "Model Selection --> Ocean GCM": similar to athmosphere
	- Click "Save"
	- Click "Process" --> this creates the relevant configuration files
- Executable location --> $DATAW
- Output --> $DATAM
- Exit puma
- On ARCHER2: job configuration in "umui_jobs/umui_jobs/JOBNAME": these are just text files containing the full configuration of the job, that are then used to compile the job

# Creating mods
- During configuration of add mod name to the list of mods
	- Select Model Selection --> Sub-Model Independent --> Compilation and Modifications --> Modifications for the model
	- In Fortran mods, add a line after the existing mods: $MY_UPDATES/MODNAME.mod and set Y/N to Y
	- Then process job as previously described
- $MY_UPDATES refers to ~/um_updates/
- In ~/um_updates create new file with "emacs MODNAME.mod" (.mod is not needed and just helps to identify the file as mod, in newest emacs version, its annoying because it is treated like a module file which makes writing the code very annoying)
- Structure of a mod file
	- First line: 	`*ID MODNAME` Define the modname
	- Second line: `*DECLARE FILENAME` Defines in which file of the code deck, the code should be changed (note that for modifications of previous mods, the name of the mode needs to mentioned afterwards, but only the actual .f file needs to be declared here)
	- Afterwards, three types of modifications are possible:
		- `*D  FILENAME.LINENUMBER \n NEWCODE` --> Delete the specified number of code in the specified file and replace it by the (potentially multiple lines of) code provided in the following line (after \n)
		- `*I  FILENAME.LINENUMBER \n NEWCODE` --> Insert NEWCODE after line LINENUMBER in file FILENAME
		- `*B  FILENAME.LINENUMBER \n NEWCODE` --> Insert NEWCODE before line LINENUMBER in file FILENAME
- Example structure of a mod:

		*ID CO2_FACTORIZATION_150PPM
		*DECLARE PHYSIO7A
		*I PHYSIO7A.129
					
		!----------------------------------------------------------------------
		! Set atmospheric CO2 used in MOSES to 150ppm
		!----------------------------------------------------------------------
		      REAL CO2_VEG                 ! CO2 value for factorization
				                              
		      PARAMETER(CO2_VEG = 0.000227874)
				
		*D ACN1F405.125
		     &,               CO2_VEG,CO2_3D,CO2_DIM,L_CO2_INTERACTIVE
					
- Note: Check im browser code deck what line in what file need to be changed (line number correspond to the versio available at https://www.paleo.bristol.ac.uk/UM4.5/UMbrowser/index.html)
- Note: Correct inundation is important
- Note: For inspiration can look at Paul's experimental mods in ggpjv/um_updates
- Note: For inspiration can look at operational mods in ggpjc/swsvalde/um_updates
- Afterwards, check if the mode worked by checking if compile produced any errors and can check if the final code files in dataw/comp_JOBNAME.tar.gz look as intended (sometimes a different mod can change the file in an unexpected way such that the final code doesn't look as intended)

# Copy job to Bristol servers
- Log onto eocene
- Run eval $(ssh-agent); ssh-add ~/.ssh/id_rsa_puma2
- copy first to Eocene by running on Eocene: scp -rp archer2:umui_jobs/umui_jobs/JOBNAME umui_jobs/.
- copy from Eocene to BC4 by running on Eocene: scp -rp umui_jobs/JOBNAME bc4:umui_jobs/.
- then log onto bc4 with ssh bc4 to continue

# Compile job
- Run on bc4: clustersubmit -C y JOBNAME
- This creates executable
- To check if compilation was successful run on bc4: leave_file_errors_02 JOBNAME

# Brute force code modifications
- Unpack comp_JOBNAME.tar.gz file from dataw into code directly (which should be empty after compile)
- Modify fortran files (`xxx.f`) as needed with emacs and save them
- Then run two line to recompile the changed files:
	- make -f makefile.compile
	- make -f makefile.link
- Note: this procedure does not work if the subroutine is in the standard code deck, because the code directory only contains symlinks to standard files and will not recompile those files

# Creating runs without using umui GUI:
- Create new job prior to compiling:
	Step 1) Sript to copy job files, give new name to experiment, change EXPTID and JOBID in the job files where needed: `new_expt_letter OLDJOBID NEWJOBID`
	Step 2) Modify jobfiles as desired (e.g. change modset in MODS_UM)
	Step 3) Compile and run
- Create new job from existing executable:
	Step 1) Create baseline job with desired configuration (modsets)
	Step 2) Run script to create ensembles: `create_ensemble`
	Step 3) Modify namelist parameters (and ancil files if relevant?) in new jobs
	Step 4) Run jobs (with clustersubmit?)

# Run job
- Run on bc4: clustersubmit -c n -s y -a y -q veryshort -r bc4 -p 7x4 -P PROJECTNUMBER JOBNAME
- "-c n" --> new run
- "-c y" --> continuation
- "-q veryshort" : max. 6h runtime
- "-q cpu": max 14d runtime
- I don't remember what -s and -a mean
- Machine: "-r bc4"
- Configuration for splitting domain: "-p 7x4"
- Account: "-P PROJECTNUMBER"
- Defaults for machine, configuration, and account can also be set in $HOME/.um/clustersubmit.conf

# Supervising running jobs
- Checking status of your jobs: myqs1
- Executable and logs in $HOME/DUMP2HOLD/um/JOBNAME/dataw/ (astart = atmosphere initial condition, ostart = ocean start condition, pe0-pe27: log from cores, pe0: lead core, thist: save current timestep for restart if model crashes)
- Output in $HOME/DUMP2HOLD/um/JOBNAME/datam/ (da = dump, pc/pd/pi/pf/pg = output files for each month, solarorbit = orbit configuration in case of transient orbits)
- Checking current state of simulation: "tail xqcra.fort6.pe0"
- Checking state of all jobs and used diskspace: "special_where"
- You can find your jobid with the following command: squeue -u USERNAME
- The normal method to kill a Slurm job is: scancel JOBID

# Postprocessing:
- Through webinterface
- Open https://www.paleo.bristol.ac.uk/web_pages.htm (bridge, webpages)
- Click on "Add/Modify List Runs": enter new job into list of eperiments: if building directly on previous experiment, can use this one to set default values
- Click on "Get_boundary_condition_files": if building directly on previous experiment, can use this one to create symlinks to old experiment) (Note: I'm not sure if this is actually needed at this point, or enough to do it after the run is finished and all files are transferred to silurian, should only work if I copy job files from puma first to eocene and then to bc4 and not if I copy them directly to bc4; in the latter case, it's likely that it should still work if it's only added after copying everything onto silurian]
- Log onto silurian with "ssh -X USERNAME@silurian.ggy.bris.ac.uk"
- create directory "bin" in your home directory (this is only needed once in the beginning)
- create file "ftp_sh.bc4.params" (this is only needed once in the beginning)
- Add jobname in file "ftp_sh.bc4.params"
- There is automatic download script which runs through all users every 4h, downloads files from bc4 onto silurian, and converts them into nc files
- For manual download, run "ftp_master -machine bc4 -expt JOBNAME" (this downloads files from bc4 onto silurian and converts them into nc files)
- Data can be accessed from eocene through umdata/JOBNAME (umdata is a symlink /home/bridge/swsvalde/umdata, where symlinks to the actual locations of the data are collected, the actual location of the data is selected automatically by the system by searching for the disk with the most available space)
- When run is finished, run "tidy_expt -machine bc4 -expt JOBNAME" (this copies all remaining files and converts them to nc files, tar's and gzip's the dataw directory such that run could be restarted from those files if needed, and deletes all run files from bc4)
- After this, all model output is stored on silurian
- Open https://www.paleo.bristol.ac.uk/web_pages.htm
- Click on "Run_scripts", enter jobname, and click on run_scripts
- Specify diagnostics that should be run
- Click on "Run_Diag"
- This creates all files that are available trough the webserver, from eocene they can be accessed through "ummodel/data/JOBNAME" (ummodel is just a symlink to "/home/bridge/swsvalde/ummodel"; not sure how this ultimately works because that disk is too small to carry all runs available on the webserver, the majority has to lie somewhere else)
- Progress of the postprocessing scripts can be tracked under https://www.paleo.bristol.ac.uk/ummodel/access/USERNAME_JOBNAME/
- Delete all job files from silurian whenever it's clear that the run is not needed anymore
- Note: there is currently no simple way to transfer data from disk to tape, so, normally after cleaning up everything only the data on the webserver is still available from an experiment
