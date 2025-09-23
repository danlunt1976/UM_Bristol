[Back to HadCM3_technical_notes](HadCM3_technical_notes.md)

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
Annela Seddon is new APVC Faculty FRD.  Simon had a meeting with her, but also attended by Ian Bond.  
"No, sorry, I can give no update.  I’ve tried to find out what is going on, but I have also been told to wait.  We are not waiting for each other, we are specifically awaiting permission from above to spend the money.  I think there are many factors in play here but anything I might say at this point would be guesswork, so best not said.  I suggest agitating with Heads of School and above - we wanted to move with the project at the start of January in order to have a viable service before BC4 gets shut down.  The longer we wait, the less likely that becomes."

Paul Valdes and Gethin Williams and Sadaf and Simon - Options for HPC
* **BC4** : maybe extended 6 months?  Few £100.  Guy Poppy VC for research.  Ian Bond currently decision maker while Guy spins up.  Climate is one of our uni Strategic Objectives.
* **Bluepebble**.  our jobs may have low priority as it favours single-core jobs.  We have 4 dedicated nodes.  Never used for a large ensemble (2 week queueing time).  Could buy more nodes.  BUT, still planned to be turned off.  May work multi-node for high-res model.  Will likely out-live BC4.   Maybe late 2026 turn-off.  But storage may deplete faster.  Currently working really well as the "new silurian".
* **Digital Labs**. We don't have an account on this.  Maybe due to EPSRC funding.  Stacey Downton controls (Gethin says maybe not?).  Low diskspace?  Would multi-node jobs work?  Sadaf is the lead.  Uses OpenStack.  Flexible but complex.  StackHPC is the company.  "mother of all learning curves". Uses VMs and cubinettis.  Ultimately, the user sees a slurm cluster. Craig Butts EPSRC £300k.  But no staff time for this.  Chris Woods is now employed on Isambard (in Thailand).  Sadaff in favour of this.  £1.3 million on x86 chips.  40 nodes x 200 cores.  Sadaff will ask someone to slurmify this.  The Gethin install the model.  Summer of this year for slurm to be there?  No idea how fast it will be.  Very filesystem and node dependent.  Sadaf is now also head of Isambard.  
  Simon says "The plan is to get a prototype x86 service running as soon as possible i.e. this month, and get some early users testing it.  Then we need to start the procurement exercise for the new nodes in order to have a replacement service running by the summer in time for the BC4 shutdown.  We had the promise of a substantial investment to kickstart the venture.  But, it’s a complex project and lots of people involved and we are waiting for a project manager to be appointed, so I’ve nothing definite to report on timescales.  It’s unlikely the prototype service will start now until February. However, there was acceptance that the service to users should not be interrupted over the summer, so everyone is working to that goal."...."Yes, I have you and others in Geography in mind as test users.  Also, some astrophysicists and chemists.  It’s important to stress test the system before we commit, and Sadaf is keen that we do this."
  Key thing is to press for the necessary storage on this system.  Think this sits under Bristol Centre for Supercomputing (BriCS).  
* **Archer2** Michael Mimmiter - Simon Tett.  Ensemble script on pre-Archer.  FAMOUS in container on Archer.  Maybe good for high-res model.  FPU if have a grant- NERC grant may help.  We may have low queue priority.  Gethin thinks may be OK.  Gethin could port to Archer - will need buy-in from Grenville and Annette.
* **Isambard 3 / AI** Gethin.  nupdate is an issue.  Original CRAY.  Mike Blackburn wrote a C nupdate.  CRAY did release source code.  Isambard 2 - 2 years per day!  Maybe 10 years per day (Gethin updated this to say it is 2-10 times slower than on BC4.  But largely irrelevant as Isambard 3 is very different to Isambard 2).  Ideal solution if it can work.  Bristol has an FPU component that is very big. May be a panel for FPU component. Nodes are "Grace-Grace" = two Grace chips on a node.  Isambard 3 - UoB has 10% of this.  Gethin working on installing here.  nupdate (written in fortran?) is an issue.  The original code is a "binary blob" that is unpacked by nupdate.  Maybe ready sooner rather than later?  Arm design, build by nvidia, called Grace.  Not x86!  One issue is the "swapbounds" step in the UM, which brings all calculations back to a single node every timestep, and does not scale well on non-x86 chips.
  Simon says "Regarding the code issues, I spoke with Sadaf Alam and Simon MS, and they are keen that the slow running should be resolved.  They have a sort of hotline to HPE for support with this sort of problem and have asked that Gethin raise tickets with them for investigation.  I’ve passed this on to Gethin so you might get some progress there.  The call for general UOB access to Isambard 3 (and Isambard AI) will go out this week for short projects beginning in February."...."Regarding Isambard, I think everyone is keen for it to be a success, including the vendors, so we should take advantage of this support while it is available."
* **Condor** PCs in department.  Speak to Jeff.  Not a good solution according to Gethin.
* **Cloud Computing** Price may increase and costly.  Data output?  May be very expensive for volatile data.  ~£20k per year for 500 TBytes volatile.  If in a container then may work.  Code is working with gfortran.  Informally, Stacey recommends considering this approach.
* **Fanny's machines** Won't be replaced.  Not a long-term solution.
* **Self-service cluster (aka NextGen)**.  Keith Woolley.  Tony Payne used.  Not many cores.  Not for HPC.  But could be a test for the cloud.  Uses VMWARE version of openStack.  Has a lot of security.  Stacey has EPSRC grant to inject funding.  ACRC sites in IT services.    

**Organisation**
Keith Woolley > Matt Shard > Steph Downton
Woolley > Steve Edge... > Simon Spate > Duncan Baldwin > David Gardner
Keith Woolley and Sadaf lead IT services and BriCS respectively.
Previously was Sadaf and Chapman.  Gethin currently doing extra role as Chapman left.
ACRC will likely be split between BRiCS and IT services.
Digital Labs will sit in BriCS (with Isambards).
NextGen-AI will sit in IT services.
RDSF will sit in IT services.

**Gethin**
UK-wide - many groups struggling with UM install due to move from Centos7 to Rocky8.
1-day MOAP, 1-day Paul.  3 days ACRC.
Saane - Polly - Stacey
Currently Thursdays until 2025.  50 days of MOAP.
Options for funding are extend MOAP, ask Neil Abel, Past2Future, RSE.  Dan to speak to Stacey regarding RSE.

**Pilot Digital Labs**
Has 10 nodes = 1280 cores (cf BC4=15,000).  200TB of solid-sate

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
*On Wednesday 18th December a sub group of the Digital Research Infrastructure Board (Bond, Sadaf, Stacey, Woolley, O'Shea, Guy Poppy Polly Eccelstone, others) met to consider the Ongoing HPC provision options for the University of Bristol during and beyond the Isambard commissioning. The group discussed the urgency of making a decision on this issue, given the age and running costs of the large scale BlueCrystal 4 HPC service, and considered the options for replacing the University's centralised cpu provision as set out in Simon Hanna’s HPC continuity options paper.* 
*It was agreed in principle that approximately £1 million of the £1.13 million ACRC 24/25 capital budget should be invested in the replacement HPC cpu and compute storage capacity. A project will be set up in January 2025 to plan for the procurement of the replacement system, the decommissioning of BlueCrystal 4 and the migration of the BC4 users. The precise specifications and costings for the replacement capacity will be determined in Jan/Feb 2025*

See Simon Hanna document.  

**Sadaf**
Met with Sadaf Alam and Gethin Williams and Richard Gilham.
Sadaf said that NVIDIA will not really be interested in our code as it is too old and bespoke, so no support for installing on Isambard.
- Now to mid-term: continue with x86 UoB HPC continuity on Digital Labs cluster.  It currently has 10x2 AMD x86 processors with 128 cores per node (Gethin can confirm).  Dan will check timeline with Ian Bond.  We are ready to go waiting for the approval where we can gradually increase x86 capacity to close to 80% of BC4 CPU core count in the next 6 months. 
*It is great to hear that Digital Labs will eventually be close to 80% of BC4 core count.  This is really good news for us.  I will push Ian on the timeline for the £1M investment.
Is the 80% what we expect to get from Ian Bond's £1M?  Or does 80% include an expectation that users will also provide funds for cores? 
Are the initial 10 AMD processors ready to use for testing now?  i.e. is slurm installed and can we have a test account, please.   As I explained, for continuity of service we really need to start the work of installing and benchmarking our code asap.
A key thing for us is plenty of disk space on the cluster, as we produce a lot of data!  How much disk space is currently on Digital Labs, what is the aspiration for eventual disk space, and how does this compare with what is on BC4?

- Medium to long term (6+ months plus) explore opportunities for code modernisation on newer multi-core x86 and ARM processors.  This would require a couple of RSE resources and possibly community efforts.
*Yes, Gethin has started on this.  How much he works on this, and how much on installing the model on Digital Labs, is a decision that depends on the answers to the above questions, I guess.*

- In parallel, find out details and plans for the next gen facility by IT services (I do not have visibility).
*I have chatted to Sophie Downton about this.  She seemed unclear as to whether Ian's investment of £1M would go to Digital Labs or to NextGen, so this makes things a little confusing for us.  It would be good to have some clarity - I will chat to Ian about this too.  From what I heard from you, it sounds like Digital Labs would be our preferred option.*

**Ian Bond**
Thank you for your time on Tuesday - it was much appreciated.

In terms of the HPC part of our discussion, see below for my understanding of what we discussed - please let me know if any of this is incorrect.  If you are happy then I will disseminate this more widely in Geography.

- As part of the "x86 HPC" community, I am really pleased that the Faculty recognises the importance of maintaining an x86 capability, and grateful for the investment of ~£1 million.
    
- The Faculty recognises the importance of "continuity of service", in particular for ongoing funded grants and deliverables, and that this will mean a period of overlap between the old and new systems due to the timescales required to port complex codes, including extending BC4 if necessary (which will hopefully not be needed!)
    
- The new system will be DigitalLabs and will be procured, maintained, and supported through BriCS, led by Sadaf Alam.
    
- I will email Sadaf to ensure that the Users have meaningful input into the specification of the new machine, in particular with regard to ensuring an appropriate balance between storage and compute.

**Simon, Sadaf, India**

As you may be aware, the University has given the green light for investing in a new HPC service at the university.

Once in place, the new environment will gradually replace first [BlueCrystal 4](https://www.bristol.ac.uk/acrc/high-performance-computing/hpc-systems-tech-specs/ "https://www.bristol.ac.uk/acrc/high-performance-computing/hpc-systems-tech-specs/") and then [BluePebble](https://www.bristol.ac.uk/acrc/high-performance-computing/hpc-systems-tech-specs/ "https://www.bristol.ac.uk/acrc/high-performance-computing/hpc-systems-tech-specs/"). Launched in 2017 and 2020 respectively, our current systems are aging rapidly - and no longer meet energy-efficiency standards.

**Contemporary x86 HPC CPUs and planned upgrade programme**   

The University’s new HPC service will offer significant benefits to users compared with BlueCrystal 4 and BluePebble, including faster processors and a planned upgrade programme allowing the environment to grow with demand and remain up-to-date.  

The CPU based system will be focused on the x86 architecture but will adapt to users requirements as technologies change. It is also a sustainable solution, both in terms of regular hardware investments to maintain and grow the system, and in terms of the huge energy and financial saving involved in switching away from BlueCrystal 4 and BluePebble.

Once in place, the new HPC system will sit alongside the University allocations of [Isambard 3 and Isambard-AI](https://uob.sharepoint.com/sites/itservices/SitePages/Supercomputing.aspx?csf=1&web=1&e=DniBlk&CID=5471928e-225f-4e84-9e85-04ef47b08902 "Original URL: https://uob.sharepoint.com/sites/itservices/SitePages/Supercomputing.aspx?csf=1&web=1&e=DniBlk&CID=5471928e-225f-4e84-9e85-04ef47b08902. Click or tap if you trust this link."), to offer a comprehensive range of HPC solutions to staff and students.

**HPC Service Continuity**

The University’s [Digital Research Infrastructure Board](https://www.bristol.ac.uk/acrc/team-and-governance/digital-research-infrastructure-board/ "https://www.bristol.ac.uk/acrc/team-and-governance/digital-research-infrastructure-board/") and [IT Services](https://uob.sharepoint.com/sites/itservices "Original URL: https://uob.sharepoint.com/sites/itservices. Click or tap if you trust this link."), appreciate that any programme of changes to your HPC service will be a cause for concern.

Over a thousand research projects and teaching courses throughout the University depend on high performance computing.

We are committed to continuing to provide a university wide HPC service that meets your research and teaching needs throughout the transition to a new HPC service.

**Timelines**

We are currently developing the timelines for the transition to the new HPC system, and we will adjust these where needed to ensure there are no interruptions to the continuity of your HPC services.   

**Transition to a modern x86 HPC facility**

Once the new HPC system is built and ready for use, we will gradually transition users from BlueCrystal 4 and BluePebble onto the new HPC facility. This will be an incremental process to ensure the continuity of your HPC services at the University.

**Keeping you informed**

We appreciate that the continuity of HPC services is vital for your research and teaching, and we will send you monthly updates on the HPC transition project and timelines as these are developed and refined.

You can also get in touch with your school representative on the [HPC and RDSF Executive Committee](https://www.bristol.ac.uk/acrc/team-and-governance/hpc-and-rdsf-executive-committee-/ "https://www.bristol.ac.uk/acrc/team-and-governance/hpc-and-rdsf-executive-committee-/") who may be able to answer your questions.  The committee Chair is Simon Hanna, School of Physics.

We are setting up a direct way for you to communicate with the HPC Transition Team, so you can ask questions or raise concerns. In our next update, we will let you know how you can get in touch with the team directly.  

Simon Hanna, Chair of the High Performance Computing Executive

Sadaf Alam, Director of Advanced Computing - Strategy and Academia

India Davison, Senior Project Manager for the HPC Transition Project


**HPC User Forum, 24/2/2025**

Sanne Terry, Simon Hanna
There was a HPC user group/meeting - one person per School
Volunteers to chair User Group meetings
Phase 1 pilot system 
Aim for Phase 2 in July
First project meeting this afternoon - 2x sys admin, Sadaf, Gethin, Simon (representing users)
Will be 0.5 to 0.7 of BC4.


**HPC User Forum, March 2025**

Chris Woodgate, Sanne Terry
Now called BC5.
BriCS = Isambard3 + Isambard AI
BC5 = x86, CPU>GPU, hosted as part of Digital Labs
April = procurement
June+August = building
August = migrating users
https://uob.sharepoint.com/sites/hpc
HPC transition project
Firm commitment to continuity of service
"Costing your research" document


**DRI User Forum, August 2025**

Helen Jones - Project Manager, BC5.
Physics tank room - racked and cabled.
Early user testing, September.
304 32-core nodes.  4GB per core.
1.2 PBytes storage.

Simon Hanna.
Allocation process.
full utilization, equitable, compliant, accountable.
easy to use, and flexible.
Projects - self-contained research (or teaching).
Apply for X node hours.  Extensions allowed.
How account for grants?
Grants will get higher priority on queue
Maybe will be expanded if there is a lot of grant income.
Some BC5 expansion will replace BP.
ACRC = BC4, BP, RDSF
BriCS = BC5, Isambards

**Gethin 11/9/2025**

Isambard 3 completed 300 years.  
Data on /work/um/tfcub/data_300_i3_pd/ pd files.



