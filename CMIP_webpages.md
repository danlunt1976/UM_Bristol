# CMIP wepbages

[Back to HadCM3_technical_notes](HadCM3_technical_notes.md)

There is a script called ~swsvalde/CMIP6s/mount_CMIP6d which mounts the /bp1/geog-tropical disk. The other folders (CMIP6 and CMIP6d) are sym links to sub-folders within geog-tropical.

I have run it on oligocene, holocene4 and triassic. All you need to do is login as swsvalde and run the command (occasionally the commands may have crashed in a bad way so you may have to type: fusermount -uz $HOME/geog-tropical first).
