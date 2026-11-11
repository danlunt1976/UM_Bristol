# UM Webpages

[Back to HadCM3_technical_notes](HadCM3_technical_notes.md)

See ~swsvalde/cgi-bin (=  /export/holocene/holocene-01/www/www.paleo.bris.ac.uk/cgi-bin)

Active scripts are:

step01_select_which_part.cgi

date_umpart01.cgi

webcontrol.cgi

Page_new2.cgi

orbit.cgi
  

I am not sure about date_new2_umpart04.cgi. I thought it was still in use, but when I searched through key webpages etc, I did not find it so maybe it is redundant these days.

Scanning through the files, I think the main thing will be paths (/home/bridge to /home) and there may be issues about permissions (the whole system was designed around the web server running as swsvalde).

There are also a whole set of perl scripts:

adduser.pl    login.pl      removeuser.pl  setup.pl             setup_web.pl     webcontrol.pl

login_new.pl  login_web.pl  setup_new.pl   setup_webcontrol.pl  step00_login.pl

which control our rudimentary login/password system.