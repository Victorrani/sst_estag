import matplotlib.pyplot as plt
import xarray as xr
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.path as mpath
import pandas as pd
import warnings
import os


warnings.simplefilter("ignore", UserWarning)

DIR_SCRIPTS = os.path.dirname(os.path.abspath(__file__))
DIR_BASE = os.path.dirname(DIR_SCRIPTS)
ARQ_SST_MENSAL = os.path.join(DIR_BASE, "dados", "sst_media_mensal.nc")
ARQ_SST_ANUAL = os.path.join(DIR_BASE, "dados", "sst_media_anual.nc")
DIRFIGS = os.path.join(DIR_BASE, "figs")
DIR_POLAR = os.path.join(DIR_BASE, "figs", "polar")

ds = xr.open_dataset(ARQ_SST_MENSAL, engine="netcdf4")
print(ds)
for i in (ds.month.values):
    print(i)