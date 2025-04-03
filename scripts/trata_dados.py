
import xarray as xr


DIRDADO = '/p1-chima/victor/estagio/dados/sst.mon.mean.nc'

ds_sst = xr.open_dataset(DIRDADO)
print(ds_sst.time)
print(ds_sst.time.diff(dim="time"))
