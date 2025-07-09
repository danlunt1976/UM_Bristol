# BRIDGE System Administration



## To add a new user:

see notes on out old wiki:
http://paleo-wikis.ggy.bris.ac.uk/wiki/bridge/SystemAdmin/New-users

`sudo -i`
Your password

`ssh-agent $SHELL ; ssh-add ; [root password]`

`cd ~swsvsalde/sbin/`
`./add_bridge_user.sh -u [UoB username - top priority] -d [for debug - doesn't do anything] -n [surname etc. - uses ldap] -e "2017-12-01" [expiry date] [-g miocene,lentil] [-s ksh] [-q is for quiet]`

Then type number.  
Default is for one year.
Standard bash is in /etc/skel

## To modify a user:

`sudo -i`
`chage -l [USER]` : check for expiration date
`usermod -e YYYY-MM-DD [USER]` 




