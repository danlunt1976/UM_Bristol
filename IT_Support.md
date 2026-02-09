[Back to HadCM3_user_notes](HadCM3_user_notes.md)

# IT Support

These pages include a list of ongoing IT support work associated with the BRIDGE machines.

# Requesting Support
All requests for support should go through one of three routes:
(1) For faults (e.g. can't log in, something that used to work is no longer working), use the [IT self-service pages](https://uob.haloitsm.com/portal/) and click on "Report a Fault".  Start your request with the "standard heading" text below. 
(2) For requests for relatively small to medium scale jobs, e.g. installing new software on the BRIDGE machines, use the [IT self-service pages](https://uob.haloitsm.com/portal/) and click on "Request something" and then "Advice and Information".  Start your request with the "standard heading" text below. 
(3) For longer term requests that involve significant amounts of time (e.g. purchasing a new machine, reconfiguring operating systems), please discuss this with your PI.  They can then make a request via the [Strategic Evaluation Tool  SET](https://uob.sharepoint.com/teams/grp-strategic-evaluation) 

### Standard heading for requests via IT services

"This issue relates to the Linux machines of the BRIDGE research group in Geographical Sciences.  These machines are normally managed by David Gardner (dg12158)."  


# Log of outstanding requests

## Faults

* ~IDL licence issues~
* ~subfigure in latex on miocene~
* pdfcrop on miocene

## Day-to-day user support

* ~convsh/xconv install on new machines~
* IDL standard libraries in one place.
* warranty renewal for all Lenovo machines.  Dan put in request to faculty.  David to explore 3rd-party warranty.
* deepmip/umbrella from wordpress to campuspress?  pros/cons...?
* ~holocene4 disk has failed - look at options for warranty/re-raiding etc.  Fixed.~
* freeze wiki to read-only: [http://paleo-wikis.ggy.bris.ac.uk/wiki/bridge/](http://paleo-wikis.ggy.bris.ac.uk/wiki/bridge/)

## Long-term support

* Migrate all machines to Rocky 8 (SET submitted)
* ~swsvalde user account new UID~
* happi machine reconfigured as standard BRIDGE machine.  Wait for Rocky 8 migration. 
* Set up up paleocene as the new webserver and ummodel/data
* swsvalde webserver - no longer run as swsvalde. Possible solution - only internal users allowed to write files.  Externals can no longer make new plots.


# Plan for new systems


| Order | Task                                                                                                                             | Person responsible         | Target date for completion | Completed |
| ----- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------- | -------------------------- | --------- |
| (1)   | Finish installation of convsh and xconv on new machines, either hacked version or full-build version.                            | DG                         | 5/12/2025                  | Y         |
| (2)   | Make a "paleo2.bris.ac.uk" domain which can be used for testing users' webpages and view-only of ~swsvalde/ummodel               | DG                         | 31/1/2026                  |           |
| (3)   | Ask paleo users to empty silurian, or accept risk of losing data.                                                                | DL                         | 7/1/2026                   | Y         |
| (4a)  | Convert silurian to Rocky 8 (need to install temporary disks for RAID metadata)                                                  | DG                         | 28/2/2026                  |           |
| (4b)  | Move all paleo users home directories from old-eocene to eocene2                                                                 | all paleo users            | 9/2/2026                   |           |
| (4c)  | Move ~swsvalde from old-eocene to eoecne2                                                                                        | PJV                        | 9/2/2026                   |           |
| (4d)  | Add paleocene as new web server (i.e. move from paleo2.bris.ac.uk to paleo.bris.ac.uk, and put oligocene onto paleo2.bris.ac.uk) | DG                         | 9/2/2026                   |           |
| (5)   | Testing of new systems                                                                                                           | all paleo users            | 27/2/2026                  |           |
| (6)   | Ask climate-dynamics users to empty anthropocene, or accept risk of losing data.                                                 | DM                         | 6/3/2026                   |           |
| (7)   | Convert anthropocene to Rocky 8                                                                                                  | DG                         | 20/3/2026                  |           |
| (8)   | Move all climate-dynamics home directories to eocene2                                                                            | all climate-dyanmics users | 27/3/2026                  |           |
| (9)   | Testing of new systems                                                                                                           | all climate-dyanmics users | 17/4/2026                  |           |
| (10)  | Retire oligocene and old-eocene                                                                                                  | DG                         | 17/4/2026                  |           |
| (11)  | Cybersecurity deadline                                                                                                           |                            | possibly end-March         |           |
| (12)  | Open up the new firewall hole for paleocene and bypass miocene                                                                   | DG                         |                            |           |


