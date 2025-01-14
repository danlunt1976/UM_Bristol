Paul Valdes - Craig Butts (HoS, chemistry) got money (from EPSRC?) for BC/BP replacement.  Cloud but local.  Dynamically partitioned.  But disk space is an issue.

David Manley - £1.2 million for x86 replacement.  EPSRC money.  Key people are Annela Seddon (APVC), Stacey Downton (leading on IT side).  Speak to Stacey about BC4 replacement.  BRICS - Bristol Research....  Also Simon Hanna who is the Academic Lead.  

Simon Hanna - 
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

Paul Valdes and Gethin Williams - Options for HPC
* **BC4** : maybe extended 6 months?  Few £100.  Guy Poppy VC for research.  Ian Bond currently decision maker while Guy spin up.  Climate is one of our uni Strategic Objectives.
* **Bluepebble**.  our jobs may have low priority as it favours single-core jobs.  We have 4 dedicated nodes.  Never used for a large ensemble (2 week queueing time).  Could buy more nodes.  BUT, still planned to be turned off.  May work multi-node for high-res model.  Will likely out-live BC4.   Maybe late 2026 turn-off.  But storage may deplete faster.
* **Digital Labs**. We don't have an account on this.  Maybe due to EPSRC funding.  Stacey Downton controls (Gethin says maybe not?).  No diskspace?  Would multi-node jobs work?  Sadaf's baby.  Uses OpenStack.  Flexible but very complex.  StackHPC is the company.  "mother of all learning curves". Uses VMs and cubinettis.  Ultimately, the user sees a slurm cluster. Craig Butts EPSRC £300k.  But no staff time for this.  Chris Woods is now employed on Isambard (in Thailand).  Sadaff in favour of this.  £1.3 million on x86 chips.  40 nodes x 200 cores.  Sadaff will ask someone to slurmify this.  The Gethin install the model.  Summer of this year for slurm to be there?  No idea how fast it will be.  Very filesystem and node dependent.  But Sadaf is now also head of isambard, so little time for this.
* **Archer2** Michael Mimmiter - Simon Tett.  Ensemble script on pre-Archer.  FAMOUS in container on Archer.  Maybe good for high-res model.  FPU if have a grant- NERC grant may help.  We may have low queue priority.  Gethin thinks may be OK.  Gethin could port to Archer - will need buy-in from Grenville and Annette.
* **Isambard 3 / AI** Gethin.  nupdate is an issue.  Original CRAY.  Mike Blackburn wrote a C nupdate.  CRAY did release source code.  Isambard 2 - 2 years per day!  Maybe 10 years per day.  Ideal solution if it can work.  Bristol has an FPU component that is very big. May be a panel for FPU component. Nodes are "Grace-Grace" = two Grace chips on a node.  Isambard 3 - UoB has 10% of this.  Gethin working on installing here.  nupdate (written in fortran?) is an issue.  The original code is a "binary blob" that is unpacked by nupdate.  Maybe ready sooner rather than later?  Arm design, build by nvidia, called Grace.  Not x86!
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
