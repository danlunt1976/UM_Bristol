**Paul Valdes** - Craig Butts (HoS, chemistry) got money (from EPSRC?) for BC/BP replacement.  Cloud but local.  Dynamically partitioned.  But disk space is an issue.

**David Manley** - £1.2 million for x86 replacement.  EPSRC money.  Key people are Annela Seddon (APVC), Stacey Downton (leading on IT side).  Speak to Stacey about BC4 replacement.  BRICS - Bristol Research....  Also Simon Hanna who is the Academic Lead.  

**Simon Hanna** 
"Digital Labs".  Virtual Machine. One Partition will be "BC5"
Has a teaching component.
Sadaf's priority.
Questions for Simon:
* Size and speed?
* Scalability - can we add to it?  S: Would like to.
* Storage?
* Where? S: physics tank room
* Charging model: Baseline FPU
* Longevity?
* Timescale?
* Role of ACRC?
BC4 is currently £1M per year to run.  May be a 6-month option to extend.  
18th Dec: meet with Bond, Wooly, and others.
Annela Seddon is new APVC Faculty FRD.  Simon had a meeting with her, but crashed by Ian Bond.

Paul Valdes and Gethin Williams and Sadaf and Simon - Options for HPC
* **BC4** : maybe extended 6 months?  Few £100.  Guy Poppy VC for research.  Ian Bond currently decision maker while Guy spin up.  Climate is one of our uni Strategic Objectives.
* **Bluepebble**.  our jobs may have low priority as it favours single-core jobs.  We have 4 dedicated nodes.  Never used for a large ensemble (2 week queueing time).  Could buy more nodes.  BUT, still planned to be turned off.  May work multi-node for high-res model.  Will likely out-live BC4.   Maybe late 2026 turn-off.  But storage may deplete faster.
* **Digital Labs**. We don't have an account on this.  Maybe due to EPSRC funding.  Stacey Downton controls (Gethin says maybe not?).  No diskspace?  Would multi-node jobs work?  Sadaf's baby.  Uses OpenStack.  Flexible but very complex.  StackHPC is the company.  "mother of all learning curves". Uses VMs and cubinettis.  Ultimately, the user sees a slurm cluster. Craig Butts EPSRC £300k.  But no staff time for this.  Chris Woods is now employed on Isambard (in Thailand).  Sadaff in favour of this.  £1.3 million on x86 chips.  40 nodes x 200 cores.  Sadaff will ask someone to slurmify this.  The Gethin install the model.  Summer of this year for slurm to be there?  No idea how fast it will be.  Very filesystem and node dependent.  But Sadaf is now also head of isambard, so little time for this.  
  Simon says "The plan is to get a prototype x86 service running as soon as possible i.e. this month, and get some early users testing it.  Then we need to start the procurement exercise for the new nodes in order to have a replacement service running by the summer in time for the BC4 shutdown.  We had the promise of a substantial investment to kickstart the venture.  But, it’s a complex project and lots of people involved and we are waiting for a project manager to be appointed, so I’ve nothing definite to report on timescales.  It’s unlikely the prototype service will start now until February. However, there was acceptance that the service to users should not be interrupted over the summer, so everyone is working to that goal."...."Yes, I have you and others in Geography in mind as test users.  Also, some astrophysicists and chemists.  It’s important to stress test the system before we commit, and Sadaf is keen that we do this."
* **Archer2** Michael Mimmiter - Simon Tett.  Ensemble script on pre-Archer.  FAMOUS in container on Archer.  Maybe good for high-res model.  FPU if have a grant- NERC grant may help.  We may have low queue priority.  Gethin thinks may be OK.  Gethin could port to Archer - will need buy-in from Grenville and Annette.
* **Isambard 3 / AI** Gethin.  nupdate is an issue.  Original CRAY.  Mike Blackburn wrote a C nupdate.  CRAY did release source code.  Isambard 2 - 2 years per day!  Maybe 10 years per day.  Ideal solution if it can work.  Bristol has an FPU component that is very big. May be a panel for FPU component. Nodes are "Grace-Grace" = two Grace chips on a node.  Isambard 3 - UoB has 10% of this.  Gethin working on installing here.  nupdate (written in fortran?) is an issue.  The original code is a "binary blob" that is unpacked by nupdate.  Maybe ready sooner rather than later?  Arm design, build by nvidia, called Grace.  Not x86!
  Simon says "Regarding the code issues, I spoke with Sadaf Alam and Simon MS, and they are keen that the slow running should be resolved.  They have a sort of hotline to HPE for support with this sort of problem and have asked that Gethin raise tickets with them for investigation.  I’ve passed this on to Gethin so you might get some progress there.  The call for general UOB access to Isambard 3 (and Isambard AI) will go out this week for short projects beginning in February."...."Regarding Isambard, I think everyone is keen for it to be a success, including the vendors, so we should take advantage of this support while it is available."
* **Condor** PCs in department.  Speak to Jeff.  Don't go there says Gethin.
* **Cloud Computing** Price may increase and costly.  Data output?  Very expensive for volatile data.  £20k per year for 500 TBytes volatile.  If in a container then may work.  Code is working with gfortran.
* **Fanny's machines** Won't be replaced.  Stay away - don't tell Keith/Barney!
* **Self-service cluster (aka NextGen)**.  Keith Woolley.  Tony Payne used.  Not many cores.  Not for HPC.  But could be a test for the cloud.  Keith persuaded registrar to giv lots of cash - ££8M, but no one used.  Uses VMWARE version of openStack.  All cash spent on consultants.  May give it to ACRC!  Very little hardware.  Could merge with Digital Labs and make a success fo Keith?!  Barney ruined it by putting in security.

Keith Woolley > Matt Shard > Steph Downton
Woolley > Steve Edge... > Simon Spate > Duncan Baldwin > David Gardner
Woolley vs. Sadaf
Was Sadaf and Chapman but Chapman could not work with Sadaf and left.
Gethin currently doing extra role as Chapman left.
UK-wide - many groups struggling with UM install due to move from Centos7 to Rocky8.

**Isambard 3 application**

8. How many CPU hours are you requesting?
They ask how many CPU-hours that we will need for the project.  Looking at the spec, I am assuming that we will use one (half) node, so 72 cores, and probably the testing over 3 months will amount to a few hundred years of simulation (let's say 1000 years) (if things go well and we get to the point of evaluating the model).  This might be 20 days of solid integration (unless the model is very slow).  So, 72 * 20 * 24 = 34,560, so ask for 50,000 CPU-hours?

10.   How many terabytes (TB) of disk space in total do you expect to need?
For disk-space, I guess 200 GB will be enough, just for testing?

6. What is your proposed project name? 
HadCM3-Isambard3

7. Please give a brief description of your project (about 250-500 words).
We have been running a climate model on BC4 for about 15 years or so.  We have had great success with this, and it has been the primary tool of our research group which averages about 20 people or more in terms of funded postdocs and PhD students.  Given the impending end of BC4, it is imperative that we make the transition to either Digital Labs, or NextGen/self-service-cloud, or to Isambard 3/AI, as soon as possible, to ensure continuity of service and research across multiple UKRI/EU/industry funded projects.  However, this is non-trivial.  The (fortran) code is exceptionally complex and large, and is surrounded by wrappers, in total of order 1 million lines of code.  As such, we need considerable time to port the code.  In this project, we would like to continue our work, carried out by Gethin Williams, to port the code to Isambard.  This involves compiling, running, evaluating, and setting up the modelling infrastructure.  We anticipate using just one node (actually half a node, so 72 cores if I have understood correctly from the Isambard 3 spec).  Plus the head-node for compiling and testing wrapper scripts etc.  I am guessing 20 days of continuous run time in total over the 3 month period, but this is a best(largest)-case scenario, and assumes that we get onto the evaluation phase of the project (benchmarking results to previous simulations), which is very much a "stretch goal".       

**Stacey Downton**
* "self-service-cloud" (preferred name) and NextGen are one and the same.
* It is currently unclear which of self-service-cloud and DigitalLabs will go ahead, but Ian Bond has "promised" ~£1M for one or the other. It is hoped that the spec will be determined in Jan/Feb.
* The timescales of when this will be available for users (i.e. with slurm, and looking to the user like something similar to BC4) is unclear, but the university is hoping for continuity of service (i.e. it will be ready when BC4 closes).
*On Wednesday 18th December a sub group of the Digital Research Infrastructure Board met to consider the Ongoing HPC provision options for the University of Bristol during and beyond the Isambard commissioning. The group discussed the urgency of making a decision on this issue, given the age and running costs of the large scale BlueCrystal 4 HPC service, and considered the options for replacing the University's centralised cpu provision as set out in Simon Hanna’s HPC continuity options paper.* 
*It was agreed in principle that approximately £1 million of the £1.13 million ACRC 24/25 capital budget should be invested in the replacement HPC cpu and compute storage capacity. A project will be set up in January 2025 to plan for the procurement of the replacement system, the decommissioning of BlueCrystal 4 and the migration of the BC4 users. The precise specifications and costings for the replacement capacity will be determined in Jan/Feb 2025*

**Sadaf**
Met with Sadaf Alam and Gethin Williams and Richard Gilham.
Sadaf said that NVIDIA will not really be interested in our code as it is too old and bespoke, so no support for installing on Isambard.
- Now to mid-term: continue with x86 UoB HPC continuity on Digital Labs cluster.  It currently has 10x2 AMD x86 processors with 128 cores per node (Gethin can confirm).  Dan will check timeline with Ian Bond.  We are ready to go waiting for the approval where we can gradually increase x86 capacity to close to 80% of BC4 CPU core count in the next 6 months. 
- Medium to long term (6+ months plus) explore opportunities for code modernisation on newer multi-core x86 and ARM processors.  This would require a couple of RSE resources and possibly community efforts.
- In parallel, find out details and plans for the next gen facility by IT services (I do not have visibility).

