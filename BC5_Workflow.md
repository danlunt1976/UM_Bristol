
This page is for documenting the current BC4/BP workflow, and the BC5 workflow, in particular the associated data-flows.


**pre-HPC stage:**
1) Scientific plan/idea
2) Input file creation (boundary conditions, mods)


**HPC stage:**
1) **Code base** permanently on HPC machine (use github for individual user scripts)
2) Compile (head node) - link to archer because of national umui infrastructure
3) Run simulations.
	* Typically ~10 simultaneous users in the group
	* Typically ~200 1-node simulations queued or running in the group
	* Typically ~100 1-node simulations running in the group
	* **Typically ~50GB per hour per simulation, in 100MB files (=500 files per hour per simulation).  Currently 600 TB on BP.**
4) **continually scp/sftp/sshfs these outputs to the BRIDGE machines**
5) **script/fortran-based post-processing suite and data archiving (currently be done at post-HPC stage)**


post-HPC stage:
1) **script/fortran-based post-processing suite and data archiving (could be done at HPC stage)** 
2) analysis 
3) paper-writing 




