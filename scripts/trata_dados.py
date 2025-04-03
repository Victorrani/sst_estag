import xarray as xr

# Caminho do arquivo
DIRDADO = '/p1-chima/victor/estagio/dados/sst.mon.mean.nc'

# Abrir o dataset
ds_sst = xr.open_dataset(DIRDADO)

# Média global anual (para cada ano)
sst_media_anual = ds_sst["sst"].groupby("time.year").mean(dim="time")

# Média climatológica mensal (para cada mês do ano considerando todos os anos)
sst_media_mensal = ds_sst["sst"].groupby("time.month").mean(dim="time")

# Salvar os resultados
sst_media_anual.to_netcdf("/p1-chima/victor/estagio/dados/sst_media_anual.nc")
sst_media_mensal.to_netcdf("/p1-chima/victor/estagio/dados/sst_media_mensal.nc")
