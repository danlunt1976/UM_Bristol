[Back to HadCM3_user_notes](HadCM3_user_notes.md)
# Introduction

The BRIDGE (Bristol Research Initiative for the Dynamic Global Environment) research group works with collaborators at XTBG (Xishuanbanna Tropical Botanical Garden) use computer models to research past, present and future climate change, investigate the causes of these changes, and the impact on plants and biodiversity. We use plant fossil data combined with computer models of climate and vegetation. Climate models require high performance computing.

Computer climate models work by simulating the day-to-day variations of weather, and then creating the climate by performing statistical analysis of the resulting output. Substantial computing resources are needed to both run the models, and store the “weather” output before it is processed into climate.

HadCM3/HadAM3/HadRM3 Software

We use the Hadley Centre climate model for all of our research. This is a relatively old climate model (developed in 1999) but has the benefit that it is computationally cheap so that we can perform long simulations and multiple sensitivity studies.

The software consists of three major components:

a. The scientific code base is about 500,000 lines of fortran 77 code.

b. Data output and the interface to parallisation library is about 20,000 line of C

c. A relatively complex set of korn shell scripts control the simulation (20,000 lines)

The code requires the mpirun library to be installed

In addition to the Hadley centre, there is also a code base required to convert output data to a common format (netcdf) and then process the output to produce the climate data. This is about another 200,000 lines of code, in a range of languages (C, Fortran, and bash). It also uses the nco and cdo operators (free netcdf processing software). Almost all of this code is single core.


# Typical Workflow

 To perform a simulation requires the following steps:

1. Prepare the “job” to be submitted. This uses a software tool called **umui** which is run on a UK university computer. Although this could also be copied to other servers, there is no requirement to do so. Furthermore, there is benefit in continuing to use one version so that there remains a unique and single database of all simulations. The output from the umui is a set of files which need to be copied onto the HPC machine.

2. Prepare the input data for the simulation. This typically uses a range of tools, depending on the user and the scientific motivation. This normally is very quick to run. The input data needs to be copied to the HPC machine.

3. Compile the fortran and c code on the HPC machine

4. Run the resulting executable. This may take weeks or more to run.

5. Depending on file storage on the HPC machines, it is likely that data needs to be transferred from the HPC machine to a machine which has significant storage.

6. The data also needs to be converted from a non-standard format to netcdf (a widely used format for geographical data). We often do this at the same time as transferring data

7. Once the whole simulation is completed, a set of programs and scripts need to be run to calculate the climate (the average of the weather data and other statistics). The climate output needs to be stored for many years.

8. Once the climate output has been produced, it is often OK to either delete or archive the weather data. Archiving is best for long simulations where it has taken a lot of effort to produce the data, whereas we some times delete smaller/shorter simulations when it would be simple to rerun the model is further analysis is required.

9. Scientific analysis and discovery of the climate output. This requires a lot of investigation and the production of many different graphics.

# Code Performance

The performance of the model depends on the grid size used to represent the Earth system. It also depends on whether the model represents only the atmosphere or is also coupled to the ocean. If the model includes the ocean, then it is likely that longer simulations are required to allow the ocean to come into equilibrium with the rest of the system.

The following table summarises the computing and disk requirements for a range of different model configurations:

|             |                                                 |                                                      |                           |                         |                       |                              |                            |                                        |                                  |
| ----------- | ----------------------------------------------- | ---------------------------------------------------- | ------------------------- | ----------------------- | --------------------- | ---------------------------- | -------------------------- | -------------------------------------- | -------------------------------- |
| Model Name  | Atmosphere Resolution                           | Ocean Levels                                         | Typical number cores $^a$ | Run Speed$^{b,c}$       | Typical length of run | Typical Duration of run $^d$ | Total number of core hours | Typical Amount of raw “weather” output | Typical Amount of climate output |
| HadCM3      | 96 longitudes, 73 latitudes,<br><br>19 levels   | 288 longitudes,<br><br>144 latitudes, 20 levels      | 28                        | 100 model years per day | 5000 years            | 7 weeks                      |                            |                                        |                                  |
| HadCM3L     | 96 longitudes, 73 latitudes,<br><br>19 levels   | 96 longitudes,<br><br>73 latitudes,<br><br>20 levels | 28                        |                         | 5000 years            |                              |                            |                                        |                                  |
| HadAM3      | 96 longitudes, 73 latitudes,<br><br>19 levels   |                                                      | 28                        |                         | 100 years             |                              |                            |                                        |                                  |
| HadAM3-N216 | 432 longitudes, 325 latitudes,<br><br>30 levels |                                                      | 84                        |                         | 100 years             |                              |                            |                                        |                                  |
| HadRM3_0.44 | 96 longitudes, 73 latitudes,<br><br>19 levels   |                                                      | 28                        |                         | 100 years             |                              |                            |                                        |                                  |
| HadRM3_0.11 | 96 longitudes, 73 latitudes,<br><br>19 levels   |                                                      | 28                        |                         | 100 years             |                              |                            |                                        |                                  |

$^a$ The model parallelises well across cores within the same motherboard. For instance, in the example above, there were two chips (each with 14 cores) on the same motherboard. It is also very flexible and we can run with any number of cores. The parallisation is poorer when running across several nodes and often completely fails to lead to further performance increases. The key influence is the inter-node transfer speed. Machine with faster internal networking (such as infiniband) allow for better parallelisation across nodes.

$^b$ Based on intel xeon chips, but about 5 years old.

$^c$ Run speed is controlled by the clock speed and number of cores, but is also influenced by the memory speed/structure and disk speed (writing output to disk can be a bottleneck)

$^d$ This does not include any time spent queuing. The model can be stopped and restarted at any time and is efficient at restarting so individual steps can be any length.


# Number of simulations

Paleoclimate simulations have a number of uncertainties and to fully quantify this uncertainty requires...

