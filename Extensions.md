# Extensions

[Back to HadCM3_technical_notes](HadCM3_technical_notes.md)

Sometimes we want to extend simulations without changing the experiment name, but without deleting the previous webpage processing (e.g. as part of a staged series of spinup, or due to a change of STASH mid-simulation)

To do this, first process the original simulation, and ensure all files are removed from umdata.  Then create a symlink in umdata with a 1-digit extension in place of the original name, e.g. tfksa1 instead of tfks.  Set up a new html_list and inidata with the extended name.  Add the extended name to the downloads file in your bin directory.

Then continue the simulation and it should download into the new extended directory.  Then process the extended simulation.     

The above is my understanding, but I haven't tested it yet.

