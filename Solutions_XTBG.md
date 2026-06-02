
Python and its associated libraries are continually being updated.  New versions are not always backwards-compatible, and so depending on what version of python, cartopy etc. that you have, there may be some changes required to the code in the Handbook. 

First, when using newer versions of Python, some people may get the following error when plotting the bathymetry:
- ```TypeError: 'GeometryCollection' object is not subscriptable```

One solution is to downgrade Cartopy, as this seems to be caused by a compatibility issue between Cartopy and Shapely. Putting the following command at the top of your code should solve the problem:
```
!pip install cartopy==0.24.1
```
   
Second, some people may encounter a problem in Cell 21 and Cell 25 where the colors in the plots cannot be rendered properly. A general solution is to make sure that the longitude array matches the data array after adding the cyclic point, and to use a 2D meshgrid when plotting with transform_first=True.

For example, in Cell 21, the original cyclic-point section could be replaced with the following:
```
# mean_mamc = cutil.add_cyclic_point(mean_mam)
# mylsmc = cutil.add_cyclic_point(mylsm)
# CHANGED: guarantees the longitude array always matches the data array
mean_mamc, lon_cyc = cutil.add_cyclic_point(mean_mam, coord=mylon)
mylsmc,    _       = cutil.add_cyclic_point(mylsm,    coord=mylon) 
# CHANGED: build a 2D meshgrid, which is required by transform_first=True` 
lon2d, lat2d = np.meshgrid(lon_cyc, mylat)
```

Then, in the plotting section, you can use `ax.contourf()` rather than `plt.contourf()`, for example:
```
contour = ax.contourf(     lon2d, lat2d, mean_mamc,     transform=ccrs.PlateCarree(),     levels=my_levs,     cmap='YlGnBu',     extend='max',     transform_first=True ) ax.contour(     lon2d, lat2d, mylsmc,     levels=[0.5],     colors='black',     linewidths=0.2,     transform=ccrs.PlateCarree(),     transform_first=True )
```

The same logic can also be applied to Cell 25 if you encounter the same colour-rendering issue there. 

  As an alternative solution, for students people still experience other unexpected issues, or who find it too difficult to install and run Conda on their own computers, Tianyi Chu from Nanjing University has also set up an online JupyterLab environment ([http://140.245.99.146:8888](http://140.245.99.146:8888/ "http://140.245.99.146:8888")), which he will  keep maintaining until the end of the workshop.
You can use their own name in English as the username. 
The password is: 
```WDTRcn/HwOgQiZgdqb0WRef6```

Different usernames will create separate folders for each person, but all users will share the same Python 3.9 environment. This should help avoid most environment-related problems.

