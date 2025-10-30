
[Back to HadCM3_technical_notes](HadCM3_technical_notes.md)

# Cloud Services

These are instructions for how to set up the VPS (virtual private server) for [https://data.deepmip.org](https://data.deepmip.org) , but will be useful to anyone setting up cloud services.

(1) In order to pay for cloud services with corporate credit card, need this category (0005 - telecommunications services, or maybe 4816) to be unlocked on the card.  Contact corporate-cloud mailbox, and IT services.  

(2) Need to have a cloud provider.  We will rent a VPS (virtual private server).  Seb uses ovhcloud. Another option is microsoft azure.  [https://ovcloud.com](https://ovhcloud.com) .  Go to "Bare Metal and VPS / VPS / Configure your VPS".  I went for VPS-1 (8GB RAM (smallest size available, sufficient for data.deepmip.org), and Ubuntu (same as Seb).  12 months.  France (Gravelines).  £48.96.  Made an ovh account.

(3) go to ovh.com, log in, and go to "Dashboard".  Click on your new VPS.  Also click on "getting started".  

(4) You will receive an email with login details, e.g.:
our VPS name is: vps-b97454e8.vps.ovh.net  
  - IPv4 address: 37.59.98.55  
  - IPv6 address: 2001:41d0:305:2100::b644  
  - Username:  ubuntu
and a link to reset your password.

(5) Log in using e.g. ssh ubuntu@37.59.98.55

(6) reset your password

(7) Have a beer.

(8) not done this bit yet....
nginx web server.  runs a docker.  container.  configure sslx access.  can restart server.  data.deepmip.org.

(9) N.B. - the actual DeepMIP database is still live, and is on the ESGF.
