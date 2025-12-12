# Paper webpages

[Back to HadCM3_technical_notes](HadCM3_technical_notes.md)

There is a webpage that includes info on the experiments used in papers.  This can be very useful for collaborating, record-keeping, and for archiving requirements of some journals.

[https://www.paleo.bristol.ac.uk/ummodel/scripts/papers/](https://www.paleo.bristol.ac.uk/ummodel/scripts/papers/)

In order to make a page for your paper, you need to create a .dat file in ~swsvalde/ummodel/scripts/papers .  You can see the format of the file required by looking at one of the existing ones.  If you make a .dat file and put it in this location, then it should appear automatically overnight as there is a crontab that does this, I think.  

If you need to build a particular page rapidly, then you can run `~swsvalde/ummodel/scripts/papers/make_paper_pages`,but this creates all the papers and takes a long time.  Instead you can run e.g.  `make_new_html Lunt_et_al_2008a.dat` to just create one paper page. 

