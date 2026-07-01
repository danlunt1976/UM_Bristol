[Back to HadCM3_user_notes](HadCM3_user_notes.md)

# IT Support

These pages include a list of ongoing IT support work associated with the BRIDGE machines.

# Requesting Support
All requests for support should go through one of three routes:
(1) For faults (e.g. can't log in, something that used to work is no longer working), use the [IT self-service pages](https://uob.haloitsm.com/portal/) and click on "Report a Fault".  Start your request with the "standard heading" text below. 
(2) For requests for relatively small to medium scale jobs, e.g. installing new software on the BRIDGE machines, use the [IT self-service pages](https://uob.haloitsm.com/portal/) and click on "Request something" and then "Advice and Information".  Start your request with the "standard heading" text below. 
(3) For longer term requests that involve significant amounts of time (e.g. purchasing a new machine, reconfiguring operating systems), please discuss this with your PI.  They can then make a request via the [Strategic Evaluation Tool  SET](https://uob.sharepoint.com/teams/grp-strategic-evaluation) 

### Standard Subject for requests via IT services

"Linux BRIDGE Research Computing Geog Sci: (**your brief description**)"  

### Standard Initial Text for requests via IT services

"This issue relates to the Linux machines of the BRIDGE research group in Geographical Sciences.  These machines are normally managed by the Science and Engineering Academic Apps Team, including e.g. David Gardner (dg12158): (**your longer description**)"  

# Log of outstanding requests

## Faults - urgent

* none at present

## Faults - non-urgent

* Dan and Paul to sudo on new machines for file access (ID:0145026).  David to add Dan and Paul.
* convsh error messages to root mailbox.  Dan emailed Paul re. error message.


## Day-to-day user support

* ~freeze wiki to read-only: [http://paleo-wikis.ggy.bris.ac.uk/wiki/bridge/](http://paleo-wikis.ggy.bris.ac.uk/wiki/bridge/)~ and switch to static copy.  David tested and just need to move to new location. 
* Wiki - prior to freezing.... check mechanism for updates to the user quota stats page: [http://paleo-wikis.ggy.bris.ac.uk/wiki/bridge/Computing/StorageStats#Pliocene] and add to new machines.
* Miocene needs new batteries.  David to order new ones.
* IDL standard libraries in one place.
* deepmip/umbrella from wordpress to campuspress?  pros/cons...?


## Long-term support

* Migrate all machines to Rocky 8 (SET submitted)
* happi machine reconfigured as standard BRIDGE machine.  Wait for Rocky 8 migration. 
* Set up up paleocene as the new webserver and ummodel/data
* swsvalde webserver - no longer run as swsvalde - use webserver user. Possible solution - only internal users allowed to write files.  Externals can no longer make new plots.  Make ACL (access control list) to determine who can read/write.  Need to set up SE Linux rules for the webserver to able to write, for security.
* plans for more frequent reboots - e.g. script to check for downloads running. 

# Completed

* ~IDL licence issues~
* ~subfigure in latex on miocene~
* ~pdfcrop on miocene~
* ~swsvalde user account new UID~
* ~convsh/xconv install on new machines~
* ~holocene4 disk has failed - look at options for warranty/re-raiding etc.~
* ~Disk array location on new machines?~
* ~rdsf - put links in sub-directory.~
* ~warranty renewal for all Lenovo machines. Dan put in request to faculty, which was successful.  David is exploring 3rd-party warranty and sent serial numbers. David still waiting for reply.~

# Plan for new systems


| Order | Task                                                                                                                             | Person responsible         | Target date for completion | Completed                 |
| ----- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------- | -------------------------- | ------------------------- |
| (1)   | Finish installation of convsh and xconv on new machines, either hacked version or full-build version.                            | DG                         | 5/12/2025                  | Y                         |
| (2)   | Make a "paleo2-test.ggy.bris.ac.uk" domain which can be used for testing users' webpages and view-only of ~swsvalde/ummodel      | DG                         | 31/1/2026                  | Y                         |
| (3)   | Ask paleo users to empty silurian, or accept risk of losing data.                                                                | DL                         | 7/1/2026                   | Y                         |
| (4a)  | Convert silurian to Rocky 8 (need to install temporary disks for RAID metadata)                                                  | DG                         | 31/5/2026                  |                           |
| (4b)  | Move all paleo users home directories from old-eocene to eocene2                                                                 | all paleo users            | 9/2/2026                   |                           |
| (4c)  | Move ~swsvalde from old-eocene to eoecne2                                                                                        | PJV                        | 9/2/2026                   |                           |
| (4d)  | Add paleocene as new web server (i.e. move from paleo2.bris.ac.uk to paleo.bris.ac.uk, and put oligocene onto paleo2.bris.ac.uk) | DG                         | 9/2/2026                   | currently working on this |
| (5)   | Testing of new systems                                                                                                           | all paleo users            | 27/2/2026                  |                           |
| (6)   | Ask climate-dynamics users to empty anthropocene, or accept risk of losing data.                                                 | DM                         | 6/3/2026                   |                           |
| (7)   | Convert anthropocene to Rocky 8                                                                                                  | DG                         | 20/3/2026                  |                           |
| (8)   | Move all climate-dynamics home directories to eocene2                                                                            | all climate-dyanmics users | 27/3/2026                  |                           |
| (9)   | Testing of new systems                                                                                                           | all climate-dyanmics users | 17/4/2026                  |                           |
| (10)  | Retire oligocene and old-eocene                                                                                                  | DG                         | 17/4/2026                  |                           |
| (11)  | Cybersecurity deadline                                                                                                           |                            | possibly end-March         |                           |
| (12)  | Open up the new firewall hole for paleocene and bypass miocene                                                                   | DG                         |                            |                           |


