import matplotlib.pyplot as plt
import xarray as xr
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.path as mpath
import pandas as pd
import warnings

warnings.simplefilter("ignore", UserWarning)


DIRDADO = '/p1-chima/victor/estagio/dados/sst.mnmean.nc'
DIRFIGS = '/p1-chima/victor/estagio/figs/sst_global/'

# dado completo bruto
ds_sst = xr.open_dataset(DIRDADO)
ds_sst = ds_sst.assign_coords(lon=(((ds_sst.lon + 180) % 360) - 180)).sortby("lon")

num_tempos = len(ds_sst.time.values)
sst_lat = ds_sst['lat'] 
sst_lon = ds_sst['lon']




for i in range(0, num_tempos):

    sst = ds_sst['sst'].isel(time=i)
    tempo = pd.to_datetime(sst.time.values)
    tempo1 = tempo.strftime('%Y-%m')
    
    print(f"Fazendo para o tempo: {tempo.strftime('%Y-%m')}, {i}")

    # Criando a figura e o eixo com global

    
    fig = plt.figure(figsize=(10, 10))

    # Definir a extensão do mapa

    
    extent = [-180, 180, -90, 90]
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    ax.set_extent(extent, crs=ccrs.PlateCarree())
    ax.add_feature(cfeature.COASTLINE, linewidth=1, color='black')
    ax.add_feature(cfeature.BORDERS, linestyle='-', linewidth=0.5)
    land = cfeature.NaturalEarthFeature(
        category='physical', name='land', scale='110m',
        edgecolor='black', facecolor='.2'
    )
    ax.add_feature(land)
    
    levels= np.arange(-2, 34, 2)
    img1 = ax.contourf(sst_lon, sst_lat, sst, levels=levels, transform=ccrs.PlateCarree(), cmap='turbo', extend='both')
    
    plt.title(f'Média mensal da temperatura da superfície do mar (°C) {tempo1}')
    gl = ax.gridlines(crs=ccrs.PlateCarree(), color='black',
                      alpha=1.0, linestyle='--', linewidth=0.4,
                      xlocs=np.arange(-180, 181, 30),  # Ajustar intervalo de longitude conforme necessário
                      ylocs=np.arange(-90, 90, 30),  # Ajustar intervalo de latitude conforme necessário
                      draw_labels=True)
    gl.top_labels = False  # Desativar rótulos no topo
    gl.right_labels = False  # Desativar rótulos à direita

    cax_ = fig.add_axes([0.92, 0.2, 0.03, 0.6])

    cbar = fig.colorbar(img1, cax=cax_, orientation='vertical', shrink=0.8, pad=0.05, label = "Temperatura da Superfície do Mar (°C)", ticks=np.arange(-2, 34, 2))


    plt.savefig(f"{DIRFIGS}/global_sst_{tempo1}.png", dpi=100, bbox_inches='tight')
    plt.close()


