[Back to HadCM3_user_notes](HadCM3_user_notes.md)

The starting point for this document was [Paul's notes](https://www.paleo.bristol.ac.uk/UM_Docs/Bristol_Tech_Notes/Starting_Using_the_Hadley_Centre_Climate_Model.docx)

# Introduction

This document describes some of the aspects of using the Hadley Centre model HadCM3 and its variants (e.g., FAMOUS) on the BRIDGE servers and the University of Bristol’s HPC machines (bluecrystal and bluepebble). The Hadley Centre model is also known as the Unified Model (UM) which refers to the unification of the model for weather and climate forecasting (the weather forecast model normally uses much higher resolution that the climate version, but it is the same code base). HadCM3 corresponds to version 4.5.1 of the UM (FAMOUS is 4.5.3).

In practice, it takes a lot of time to build experience with all aspects of the system. This document is just a start, but the aim is to gradually expand the content until it is a relatively complete description of the complete system.

Unfortunately, computing platforms and software are always changing, and it is almost certain that some aspects of this document are out-of-date. It is also a developing document, and the aim is to gradually expand it. Therefore it is probably better to always access the online version, rather than having your own copy.

# Obtaining Accounts

We use a variety of different computers for running and processing climate model outputs and the first task is to obtain user accounts. Unfortunately, this is always changing so some of this information is out-of-date but it will give you some guidance.

(a) BRIDGE servers. These are used for most day-to-day analysis of model simulations. We have a number of machines, called after geological periods (eocene.ggy.bris.ac.uk, triassic.ggy.bris.ac.uk, silurian.ggy.bris.ac.uk, anthropocene.ggy.bris.ac.uk). To get an account on these machines, please contact your supervisor/PI.

(b) Bluecrystal phase4 and bluepebble. These are our main high-performance computers on which we run climate model simulations. They consist of “login nodes” and many “computer nodes”. The login nodes are called: bc4login.acrc.bris.ac.uk and bp1-login04.acrc.bris.ac.uk. To get an account on these machines, [https://www.acrc.bris.ac.uk/login-area/apply.cgi](https://www.acrc.bris.ac.uk/login-area/apply.cgi) .  Under “Project details” choose “Join an existing project” and give the code (provided by supervisor/PI).  Under “preferred log-in shell” choose bash.  In the box for additional info, you can just state “HadCM3 user”. NOTE: Also specify that you want an account on bluecrystal as well as bluepebble. The default is bluepebble only.

(c) For bluepebble only, You may also need to email them because you need to ask them to create a folder: /bp1store/geog-tropical/users/(your username). Also ask to be added to the s-tropical group. Cc [p.j.valdes@bristol.ac.uk](mailto:p.j.valdes@bristol.ac.uk) on your email since they need to confirm additions.

(d) Puma2.  ”puma2” is the machine that holds a database of (almost) all Met Office Unified Model (UM) climate simulations ever carried out in universities in the UK.  It is also the machine from which we set up and submit simulations.  puma2 is now part of the Archer national computing resources. To get access to puma, you need to have an account on archer2. Instructions for access the system are here: [https://cms.ncas.ac.uk/puma2/](https://cms.ncas.ac.uk/puma2/)

I would strongly recommend that you choose the same username on puma/archer as at Bristol. It makes life simpler.

In order to access the system, you need to create a ssh-key from one of our servers. The new system allows multiple such keys. I would suggest you do this on bluecrystal but also on our BRIDGE servers. To create the key, on bluecrystal and/or BRIDGE server type:

`ssh-keygen -t rsa -f ~/.ssh/id_rsa_puma2`

The resulting key needs to be sent to archer, following the instructions in the NCAS website above.

(e) You also need access to our webpage server. Go to: [https://www.paleo.bristol.ac.uk/](https://www.paleo.bristol.ac.uk/).   This gives you access to all of our model simulations. This is almost overwhelming since over the last 30 years we have performed about 50000 simulations!!!  More details about the web page can be found here: [https://www.paleo.bristol.ac.uk/ummodel/scripts/papers/Using_BRIDGE_webpages.pdf](https://www.paleo.bristol.ac.uk/ummodel/scripts/papers/Using_BRIDGE_webpages.pdf)

There are also some help pages on our BRIDGE wiki (note that you will need to be on the university network/VPN to access this). See: [https://www.paleo.bristol.ac.uk/wiki/bridge/](https://www.paleo.bristol.ac.uk/wiki/bridge/)

