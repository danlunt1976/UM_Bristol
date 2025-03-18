[Back to HadCM3_technical_notes](HadCM3_technical_notes.md)

This is a summary of the current state of our BRIDGE machines

| Machine                  | OS          | Array disk         | Main usage                                       | Plans                                                                                                                               |
| ------------------------ | ----------- | ------------------ | ------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| eocene                   | Centos 6.10 | /home/bridge 2 TB  | main login node.  home directories               | needs replacing as old and slow. Replace with paleocene.  Could move to Computer Centre to save time, as this does not require CE+. |
| silurian                 | Centos 6.10 | array-01 132 TB    | UM downloads                                     |                                                                                                                                     |
| triassic                 | Centos 6.10 | array-01 74 TB     | UM downloads                                     | needs replacing as old and slow.  Remove as much data as possible and Rebuild.                                                      |
| anthropocene             | Centos 6.10 | array-01 132 TB    | Climate Dynamics group                           |                                                                                                                                     |
| oligocene (aka holocene) | Centos 6.10 | holocene-01 327 TB | web server and ummodel/data.  Has firewall hole. | needs replacing as old and slow.                                                                                                    |
| miocene                  | Rocky 8     |                    | will be UM downloads                             | To be tested.                                                                                                                       |
| holocene4                | Rocky 8     |                    | will be UM downlaods                             | Currently moving triassic array data to this disk array.                                                                            |
| eocene2                  |             |                    | will be new main login node and home directories |                                                                                                                                     |
| paleocene                |             |                    | will be new web server.                          | will replace oligocene.                                                                                                             |
                                                                                            

Array disk size from: `df -BG`
OS from: `rpm -qa centos-release` or `rpm -qa rocky-release`

We need to comply with CyberEssentials+.  Deadline end-March 2025.  Requires update from Centos 6.10 to Rocky8.  But not for silurian or anthropocene as they are situated elsewhere(?!).  And we will physically move eocene to avoid this requirement for now.

Rocky8 now on miocene.  But not tested.  gfortran does not compile all the scripts.  Intel compiler is fine though.  qplot does not compile.

Plan - open miocene up to group.  When working, send to group and ask for feedback.

BluePebble is possibly the future of local hardware.  Could have a head-node plus a disk.  However, Digital Labs may be replacing Bluepebble.  See [University_HPC](University_HPC)

Fund machines via Capital Bids?

