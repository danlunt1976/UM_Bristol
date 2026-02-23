[Back to HadCM3_user_notes](HadCM3_user_notes.md)

# Documentation for useful tools
# Introduction

When interacting with models and model results, some tools are useful for visualising (e.g., xconv, panoply), some tools are useful for downloading files (e.g., ftp_master), and some tools are useful for configuration/ancillary manipulation (e.g., xancil, isla).

A quick rule of thumb:
- GUI/X11 tools (xconv, xancil) are usually easiest to run on BRIDGE with X-forwarding (or on a local desktop if installed).
- Command-line tools (cdo) are best run on the server close to the data.
- BRIDGE download wrappers (ftp_master) are BRIDGE-specific convenience scripts for moving model output from HPC to BRIDGE storage.

If you are on the newer Rocky-8 BRIDGE machines, most software is provided via environment modules:
- Discover: `module avail`
- Load: `module load <name>`
- Check what you have: `module list`

For X11 forwarding from macOS:
- Install and start XQuartz
- SSH with X forwarding: `ssh -Y user@<bridge-host>`
- If a GUI won’t start, try `ssh -X` (less permissive) vs `ssh -Y` (more permissive), and confirm XQuartz is running.

## xconv

https://ncas-cms.github.io/xconv-doc

Xconv is a point-and-click X-windows application widely used to inspect and quickly plot UM PP fields and netCDF. It’s particularly handy for “sanity checking” fields (are values sensible? missing values? time axis?) and for quick regridding/output conversion to netCDF for downstream analysis.

How to access
- On BRIDGE: log in with X-forwarding enabled (see intro), then run `xconv` if it’s on your PATH.
- If not found, try locating it via modules: `module avail xconv` then `module load ...`.
- Quick check: `which xconv`.

Basic tips / quick workflow
- Open files: File → Open, or start from a terminal in the data directory and open via the GUI.
- Inspect metadata: check variable names, levels, time axis, missing values, units.
- Quick plots: use the built-in plotting to verify spatial patterns and time evolution.
- Export: when you need Python/CDO workflows, export to netCDF (where supported) for easier scripting.

Common gotchas
- X11 requirement: if you see display/GLX errors, it’s almost always missing X-forwarding or XQuartz not running.
- Very large files: xconv can feel slow; for batch processing use `cdo`/Python instead.

Where to get advanced tips
- Official docs: https://ncas-cms.github.io/xconv-doc
- For deeper UM-format work, many teams eventually switch to scripted workflows (Iris/xarray + CDO/NCO) once the “quick look” step is done.

## xancil

https://ncas-cms.github.io/xancil-doc/singlehtml/index.html

Xancil is an X-windows application for creating UM ancillary files (e.g., land surface / emissions / climatologies) from netCDF inputs. It’s commonly used when you have prepared a netCDF on a UM-compatible grid and need a UM ancil for the model.

How to access
- On BRIDGE: log in with X-forwarding (see intro) and run `xancil` if on PATH.
- If not found, use modules: `module avail xancil` then `module load ...`.
- Quick check: `which xancil`. User version 0.62.

Basic tips (what to prepare before opening xancil)
- Ensure your netCDF has clear dimension/coordinate definitions (time, lat, lon, levels as needed).
- Ensure metadata is sensible (units, missing_value/_FillValue, variable naming).
- Know your target UM grid and vertical structure (xancil expects consistency).

Common gotchas / troubleshooting
- “Dimension not recognised” style issues usually mean the netCDF coordinate/dimension names or attributes aren’t what xancil expects.
- A practical workflow is: generate netCDF (often with Python/Iris), then fix dimension/attribute naming with NCO (e.g., `ncrename`, `ncatted`) before xancil.
- Some processing chains can lose metadata (e.g., certain `cdo` operations). If xancil complains, validate the netCDF headers before trying again.

Where to get advanced tips
- Official docs: https://ncas-cms.github.io/xancil-doc/singlehtml/index.html
- Practical BRIDGE/CMIP7 workflow notes mentioning xancil + netCDF cleanup: bridge_um/CMIP7_fcg_GHG_CO2.md

## panoply

https://www.giss.nasa.gov/tools/panoply/

Panoply is a desktop GUI for exploring and plotting netCDF/HDF/GRIB data. It’s great for quick-look plotting of netCDF outputs (including those produced by `um2nc`, `xconv`, or post-processing pipelines) without writing any code.

How to access
- Best on your local machine (Panoply is a Java desktop app):
  - Download from the NASA Panoply page and install for macOS/Linux/Windows.
- On servers/HPC it can work via X-forwarding, but it’s usually slower and more brittle than running locally.

Basic tips
- Use it for quick inspection of netCDF variable names, dimensions, and coordinate interpretation.
- If maps look wrong, check whether lon is 0–360 vs -180–180 and whether lat/lon are correctly identified as coordinates.
- For time series, confirm the time units/calendar; odd calendars can affect GUI interpretation.

Where to get advanced tips
- NASA documentation and FAQs on the Panoply page.
- For “publication-grade” plotting or complex workflows, consider scripted plotting (Python: xarray/iris + matplotlib/cartopy).

## cdo

https://code.mpimet.mpg.de/projects/cdo
https://code.mpimet.mpg.de/projects/cdo/embedded/index.html

CDO (Climate Data Operators) is a fast command-line toolbox for common climate/data operations on netCDF/GRIB: temporal means, spatial remapping, subsetting, merges, arithmetic, climatologies, etc. It’s ideal for batch processing near the data (BRIDGE/HPC).

How to access
- On BRIDGE: try `cdo -V` to see if it’s available.
- If missing, load via modules: `module avail cdo` then `module load ...`.

Basic tips / common commands
- Inspect file quickly: `cdo sinfo file.nc` or `cdo infon file.nc`
- List variable names: `cdo showname file.nc`
- Time mean: `cdo timmean in.nc out_timmean.nc`
- Monthly climatology: `cdo ymonmean in.nc out_ymonmean.nc`
- Spatial remap (example): `cdo remapbil,targetgrid.txt in.nc out_remap.nc`


Common gotchas
- Metadata: some operators can drop or simplify attributes. If you need strict CF metadata, check outputs with `ncdump -h` or Python.
- Calendars/time axes: confirm time units/calendar after operations, especially when concatenating or slicing.
- PP vs netCDF: CDO is primarily for netCDF/GRIB; convert UM PP to netCDF first if needed.

Where to get advanced tips
- Operator index/tutorials: https://code.mpimet.mpg.de/projects/cdo/embedded/index.html
- Built-in help: `cdo -h` and `man cdo`
- For CMIP7-style workflows, you already note that CDO is useful but may lose metadata (see bridge_um/CMIP7_fcg_GHG_CO2.md).

## ftp_master

`ftp_master` is a BRIDGE-specific command used to download experiment output from a remote machine (commonly the University HPC) onto BRIDGE storage, and (in typical configurations) convert outputs into netCDF as part of the transfer workflow. It is often used `tidy_expt` (finalise/copy remaining files and clean up).

How to access
- Run on BRIDGE (not on your laptop). If your PATH is set up for BRIDGE utilities, you can invoke it directly.
- If you’re unsure how your account is configured, see the BRIDGE download notes in bridge_um/Downloading.md.

Basic usage patterns
- Manual download for an experiment (example pattern):
  - `ftp_master -machine bc4 -expt JOBNAME`
- After the run is finished, a typical finalisation step:
  - `tidy_expt -machine bc4 -expt JOBNAME`

Where the data ends up / how to find it
- Output is accessible via your BRIDGE `umdata` dir.
- If you can’t find the files, search in your `umdata` tree for the experiment ID.

Common gotchas
- Don’t run `tidy_expt` too early: it can delete/clean remote run directories as part of tidying.

Where to get advanced tips
- BRIDGE-wide download process + wrapper notes: bridge_um/Downloading.md
- Concrete step-by-step notes (including params file mention and how data is arranged): bridge_um/Nils_notes_for_running_HadCM3B.md

## utils_cmip7

https://github.com/Climateyousheng/utils_cmip7

utils_cmip7 is a Python toolkit for carbon cycle analysis from UM climate model outputs. It handles the full workflow from raw UM output files to validated results against CMIP6 and RECCAP2 observations.

How to install
```
git clone https://github.com/Climateyousheng/utils_cmip7.git
cd utils_cmip7
pip install -e .
```

Requirements: Python >= 3.8, numpy, pandas, matplotlib, iris, cartopy, xarray, cf-units, netCDF4 (all installed automatically with `pip install -e .`).

### Input data

The toolkit works with two types of input:

**Option A: Pre-processed annual mean NetCDF files** (recommended, faster)
Located in `~/annual_mean/{expt}/`:
- `{expt}_pa_annual_mean.nc` — atmosphere (temperature, precipitation)
- `{expt}_pt_annual_mean.nc` — TRIFFID (GPP, NPP, soil respiration, carbon stocks, PFTs)
- `{expt}_pf_annual_mean.nc` — ocean (fgco2)

Generate these from raw output using:
```
./annual_mean_cdo.sh "xqhuj" ~/annual_mean pt pd pf
```

**Option B: Raw monthly UM files**
Located in `~/dump2hold/{expt}/datam/`, matching pattern `{expt}a#pi00000{YYYY}{MM}+`.

### STASH code mappings

The toolkit centralises STASH code mappings so you don't need to remember them:

| Variable | STASH (PP) | STASH (NC) | Description |
|----------|------------|------------|-------------|
| GPP | m01s03i261 | 3261 | Gross Primary Production |
| NPP | m01s03i262 | 3262 | Net Primary Production |
| Rh | m01s03i293 | 3293 | Soil respiration |
| CV | m01s19i002 | 19002 | Vegetation carbon |
| CS | m01s19i016 | 19016 | Soil carbon |
| fracPFTs | m01s19i013 | 19013 | PFT fractions |
| fgco2 | m02s30i249 | 30249 | Ocean CO2 flux |
| tas | m01s03i236 | 3236 | Surface air temperature |
| pr | m01s05i216 | 5216 | Precipitation |

Unit conversions are applied automatically (e.g. kgC/m2/s to PgC/yr for fluxes, kgC/m2 to PgC for stocks).

### Basic usage

Extract annual means from pre-processed NetCDF:
```python
from utils_cmip7 import extract_annual_means
ds = extract_annual_means(expts_list=['xqhuc'])

# Access data
gpp = ds['xqhuc']['global']['GPP']
print(f"GPP: {gpp['data']} {gpp['units']}")

# Extract specific regions
ds = extract_annual_means(['xqhuc'], regions=['global', 'Europe', 'Africa'])
```

Extract from raw monthly UM files:
```python
from utils_cmip7 import extract_annual_mean_raw
data = extract_annual_mean_raw('xqhuj', start_year=1850, end_year=1900)
```

### Scripts

**extract_preprocessed.py** — Extract annual means for all RECCAP2 regions (global + 10 regions) and generate time series plots:
```
python scripts/extract_preprocessed.py xqhuc
```
Outputs to `validation_outputs/single_val_{expt}/`: a CSV of time-mean values plus per-region time series plots for carbon fluxes, stocks, climate variables, and PFT fractions.

**extract_raw.py** — Extract from raw monthly files:
```
python scripts/extract_raw.py xqhuj --outdir ./plots
```

**validate_experiment.py** — Three-way validation (UM vs CMIP6 vs RECCAP2):
```
python scripts/validate_experiment.py xqhuc
```
Outputs to `validation_outputs/single_val_{expt}/`:
- `{expt}_metrics.csv` — UM results in observational format
- `{expt}_bias_vs_cmip6.csv` — bias, bias %, RMSE, within-uncertainty flag
- `{expt}_bias_vs_reccap2.csv` — same for RECCAP2
- `comparison_summary.txt` — text summary comparing UM performance
- `plots/` — three-way comparison bar charts, regional bias heatmaps, time series

### CLI commands (experimental)

```
utils-cmip7-extract-raw xqhuj
utils-cmip7-extract-preprocessed xqhuc
utils-cmip7-validate-experiment xqhuc
utils-cmip7-validate-ppe
```

### Common gotchas

- If plots show only a subset of variables, the missing ones were not found during extraction. Check that the annual mean files exist and were generated with the correct STASH codes.
- Raw extraction reads many monthly files and can be slow. Prefer pre-processed annual mean files when available.
- STASH codes in NetCDF headers may show a trailing `s` suffix (e.g. `3261s`) — this is normal CDL type notation and does not affect extraction.
- For regional results, ensure the RECCAP2 mask file is available. Default location: `~/scripts/hadcm3b-ensemble-validator/observations/RECCAP_AfricaSplit_MASK11_Mask_regridded.hadcm3bl_grid.nc`. Override with `export UTILS_CMIP7_RECCAP_MASK=/path/to/mask.nc`.

[Back to HadCM3_user_notes](HadCM3_user_notes.md)
