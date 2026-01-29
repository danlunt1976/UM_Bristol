
This page is for documenting the current BC4/BP workflow, and the BC5 workflow, in particular the associated data-flows.


**pre-HPC stage:**
1) Scientific plan/idea
2) Input file creation (boundary conditions, mods)


**HPC stage:**
3) **Code base** and user run scripts on HPC machine (could use github)
4) Compile (head node) - link to archer because of nartonal umui infrastrucute
5) Run simulations.
	* Typically ~10 simultaneous users in the group
	* Typically ~200 1-node simulations queued or running in the group
	* Typically ~100 1-node simulations running in the group
	* **Typically ~50GB per hour per simulation, in 100MB files (=500 files per hour per simulation).  Currently 600 TB on BP.**
6) **continually scp/sftp/sshfs these outputs to the BRIDGE machines**
7) **script/fortran-based post-processing suite and data archiving (currently be done at post-HPC stage)**

post-HPC stage:
7) **script/fortran-based post-processing suite and data archiving (could be done at HPC stage)**
8) analysis
9) paper-writing




