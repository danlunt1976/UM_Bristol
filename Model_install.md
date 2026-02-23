[Back to HadCM3_technical_notes](HadCM3_technical_notes.md)

The original CD with the code from the Met Office is lost

gcom is the hardest part of the install.  Gethin does this part.

nupdate is also a challenge.

Gethin has a cut-down version of the install.

Once the cut-down version is running, Paul modifies to make changes associated with running on different machines etc. invisible to the user, via clustersubmit.

Could put the model on github (Richard at BRICS also suggested this).

On bc4, the model code etc is here:
~ggpjv/UM_HOME , which is a link to: /mnt/storage/private/bridge/um/PUM64 , which is a link to PUM64_rocky8 .

The key code is here: /mnt/storage/private/bridge/um/PUM64_rocky8/um/vn4.5

----
18/2/2026

Gethin found the CD at home.
Plan:
1) Upload raw CD to github, once unpacked.
2) Upload Paul's changes:
	* whitsepace end of line
	* comments over lin length
	* automated makefiles (alphabetical order changed)
	* new configure file
	* get rid of pdksh
3) upload stripped copyright (keep line numbers)
4) upload new licence file
5) get rid of compiler-specifci section
6) GCOM (3.1, 3.8, 2.8 ?) new version
7) Met Office nupdate , or CRAY, or Mike Blackburn
8) upload again officially and make available
9) Longer term:
	* xconv, xancil
	* Bristol scripts/infrastrucutre/libancil etc.








