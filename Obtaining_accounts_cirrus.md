
# Obtaining an account on Cirrus


You can apply for a Cirrus account through the SAFE system ([https://safe.epcc.ed.ac.uk/](https://safe.epcc.ed.ac.uk/ "https://safe.epcc.ed.ac.uk/")).  

Login in to SAFE with your SAFE credentials.

Go to Login accounts → Request login account, select the "n02" project and click Next.  Then choose "Cirrus" as the machine and click Next.  
  
Note: Your Cirrus username must match your ARCHER2 username.  This should also be the same as your UoB account.

Upload an SSH public key, created on the machine that you wish to log in from.  For example, in holocene4 I did:
`ssh-keygen -t rsa -f ~/.ssh/id_rsa_cirrus`



----
## emails from NCAS (to be deleted later)...



Project budget codes are unchanged from ARCHER2 and have been populated with the awarded allocations, where appropriate.  
  
The Cirrus work filesystem is located at /epccfs/n02. To facilitate the transfer of essential data, this filesystem is also mounted on ARCHER2 at /nscds/n02.  
  
Please transfer only essential files to Cirrus. The n02 disk quota is the same as on ARCHER2. Please do not simply transfer all files across otherwise we will run out of space quite quickly.  Please take this opportunity to remove unwanted files. Only active files needed to run your simulations should be stored on Cirrus; output data should be moved to other storage, e.g. JASMIN.  
  
Guidance on transferring data to Cirrus, including using rclone, is available in the ARCHER2 documentation ([https://docs.archer2.ac.uk/user-guide/data/#local-file-transfer](https://docs.archer2.ac.uk/user-guide/data/#local-file-transfer "https://docs.archer2.ac.uk/user-guide/data/#local-file-transfer")).  
  
  
IMPORTANT: Unified Model Users  
—------------------------------  
You can apply for an account on Cirrus (if your project has been awarded time) and transfer over essential data, but you will not yet be able to run UM workflows. Please continue to use your ARCHER2 budget until the end of the ARCHER2 service. NCAS-CMS are working hard to set up the UM, associated infrastructure and to provide documentation on how to upgrade your workflows to run on Cirrus. We will announce when the UM is available for use.  
  
Not all UM versions currently available on ARCHER2 will be installed on Cirrus.  Initially we will focus on versions 13.5-13.9, 14.x.  A few other older key UM versions will also be installed where there is an identified need;  e.g. CMIP6. Other versions will be considered on a case-by-case basis.  
  
With the move to Cirrus, Cylc 7 will be officially retired, and all workflows will need to use Cylc 8.  
  
PUMA2 will continue to act as the Cylc workflow server and will work with Cirrus in the same way as it does with ARCHER2. We are working with EPCC to reconfigure PUMA2, and users will need to undertake a small amount of transition work. We will make a further announcement when the timescales and required actions are confirmed.  
  
If you have any questions please raise a ticket on the NCAS-CMS helpdesk: [https://cms-helpdesk.ncas.ac.uk/](https://cms-helpdesk.ncas.ac.uk/ "https://cms-helpdesk.ncas.ac.uk/")  
  
Best Regards,  
Ros



Dear PUMA2 User,  
  
EPCC are in the process of migrating the PUMA2 service from the ARCHER2 domain to the Cirrus domain. As part of this work, the current PUMA2 /home filesystem, which is hosted on ARCHER2, will be replaced by a new /home filesystem hosted on Cirrus.  
  
Summary Timeline:  
-----------------  
* PUMA2 will be down for maintenance 09:00-17:00 Wednesday 18th November.  
  
* Copy your PUMA2 files to the new /home filesystem ahead of the maintenance.  
  
* Plan to finish running Rose/Cylc jobs by Wed 18th November.  
  
What do you need to do?  
-----------------------  
All users are responsible for copying their own data from their existing PUMA2 home directory to their new Cirrus-based home directory.  
  
The new Cirrus /home filesystem is already accessible from PUMA2 at:  /mnt/cephfs/n02/n02-puma2/<username>  
  
You will need to have a Cirrus account in order to access the above directory. Copy any files and directories that you wish to retain from your current PUMA2 home directory into your new home directory. PLEASE DO NOT COPY OVER  THE cylc-run DIRECTORIES.  
  
Please take this opportunity to review your existing home directory and avoid transferring unnecessary files.  
  
Home directory quotas and usage:  
--------------------------------  
Please be aware that the new Cirrus-based home filesystem has user quotas enforced.  
  
PUMA2 home directories are intended for Rose suites and Cylc directories, plus necessary smaller working files. Large datasets and other bulky data files should not be stored in your PUMA2 home directory.  
  
PUMA2 Maintenance – Wednesday 18th November:  
--------------------------------------------  
PUMA2 will be taken offline for maintenance from 09:00 till 17:00 on Wednesday 18th November. During this maintenance, EPCC will switch the default home directory from the ARCHER2 filesystem to the new Cirrus filesystem.  
  
Once the maintenance is complete and PUMA2 is available again, logging in will automatically place you in your new Cirrus-based PUMA2 home directory. You will no longer be able to continue running existing Rose/Cylc suites on ARCHER2.  
  
ARCHER2 shutdown – Friday 20th November:  
----------------------------------------  
Following the migration, the existing ARCHER2-based home directory will remain accessible, allowing you to retrieve and copy across any files you may have missed during the initial transfer.  
  
However, this access will only be available until 14:00 on Friday 20th November. After this time, the old ARCHER2-based home directory will no longer be accessible.  
  
If you have any questions or encounter any problems with the migration, please contact the CMS Helpdesk.  
  
Best regards,  
NCAS-CMS