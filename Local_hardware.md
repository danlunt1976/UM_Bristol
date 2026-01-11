[Back to HadCM3_technical_notes](HadCM3_technical_notes.md)

This is a summary of the current state of our BRIDGE machines

| Machine                  | OS          | Array disk                                                   | Main usage                                                                                           | Plans                                                                                                                                                                               | Location              |
| ------------------------ | ----------- | ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| eocene                   | CentOS 6.10 | /home/bridge 2 TB                                            | Main login node.  Home directories                                                                   | Needs replacing (with eocene2) as old and slow.  Moved to Computer Centre as an interim step, as outside CE+ scope.  Currently used for Tivoli archive access to paleocene storage. | Computer Centre (CC)  |
| silurian                 | CentOS 6.10 | array-01 132 TB                                              | UM downloads                                                                                         |                                                                                                                                                                                     | Computer Centre (CC)  |
| triassic                 | Rocky 8     | array-01 74 TB                                               | UM downloads                                                                                         |                                                                                                                                                                                     | Geog server room      |
| anthropocene             | CentOS 6.10 | array-01 132 TB                                              | Climate Dynamics group                                                                               |                                                                                                                                                                                     | Computer Centre (CC)  |
| oligocene (aka holocene) | CentOS 6.10 |                                                              | Web server.  Has (indirect) firewall hole.                                                           | Needs replacing as old and slow.  Paleocene is the intended replacement.                                                                                                            | Computer Centre (CC)  |
| miocene                  | Rocky 8     | ~22TB                                                        | will be UM downloads (was CMIP6 data, which is now on BP)                                            | To be tested.   Currently acting as webserver proxy for oligocene external traffic.                                                                                                 | Geog server room      |
| holocene4                | Rocky 8     | ~160 TB.  Old copy of ummodel/data that is no longer needed. | will be UM downlaods                                                                                 | Currently moving triassic array data to this disk array.                                                                                                                            | Computer Centre (CC)  |
| eocene2                  | Rocky 8     | ~7TB homedirs                                                | New home directories are on here.  Will also be used for Tivoli archive access to paleocene storage. | Has Paul's home directory to test.                                                                                                                                                  | Computer Centre (CC)  |
| paleocene                | Rocky 8     | holocene-01 327 TB                                           | will be new web server and ummodel/data.                                                             | will replace oligocene.                                                                                                                                                             | Computer Centre (CC)  |
| stage3                   |             |                                                              | Retired.                                                                                             |                                                                                                                                                                                     | Computer Centre (CC)  |


Array disk size from: `df -BG`
OS from: `rpm -qa centos-release` or `rpm -qa rocky-release`

We need to comply with CyberEssentials+.  Deadline end-March 2025.  Requires update from Centos 6.10 to Rocky8.  But not for silurian or anthropocene as they are out of scope at present.  Eocene and Oligocene physically moved to an out of scope location to avoid this requirement for now.

Rocky8 now on miocene.  But not tested.  gfortran does not compile all the scripts.  Intel compiler is fine though.  qplot does not compile.

Plan - open miocene up to group.  When working, send to group and ask for feedback.

BluePebble is possibly the future of local hardware.  Could have a head-node plus a disk.  However, Digital Labs may be replacing Bluepebble.  See [University_HPC](University_HPC)

Fund machines via Capital Bids?

Issue is that the UID for swsvalde has been used elsewhere in the university.  Maybe also the paleo group ID.  (Conflicts exist because the old UIDs/GIDs were allocated locally via NIS, rather than using the central identity management)

