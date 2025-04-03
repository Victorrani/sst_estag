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


DIRDADO = '/p1-chima/victor/estagio/dados/sst.mon.mean.nc'
DIRFIGS = '/p1-chima/victor/sst_estag/figs/south_pole_imgs/'

# dado completo bruto
ds_sst = xr.open_dataset(DIRDADO, engine="netcdf4")
num_tempos = len(ds_sst.time.values)
ds_sst.close()
for i in range(0, num_tempos):

    ds_sst = xr.open_dataset(DIRDADO, engine="netcdf4")

    num_tempos = len(ds_sst.time.values)
    sst = ds_sst['sst'].isel(time=i).load()
    sst_lat = ds_sst['lat']
    sst_lon = ds_sst['lon']
    ds_sst = ds_sst.assign_coords(lon=(((ds_sst.lon + 180) % 360) - 180)).sortby("lon")


    tempo = pd.to_datetime(sst.time.values)
    tempo1 = tempo.strftime('%Y-%m')
    
    print(f"Fazendo para o tempo: {tempo.strftime('%Y-%m')}, {i}")

    # Criando a figura e o eixo com projeção polar sul
    extent = [0, 360, -90, 0]
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.SouthPolarStereo())

    # Definir a extensão do mapa
    ax.set_extent(extent, ccrs.PlateCarree())

    # Criar um círculo para limitar a projeção
    theta = np.linspace(0, 2*np.pi, 100)
    center, radius = [0.5, 0.5], 0.5
    verts = np.vstack([np.sin(theta), np.cos(theta)]).T
    circle = mpath.Path(verts * radius + center)
    ax.set_boundary(circle, transform=ax.transAxes)

    # Adicionar a Antártica preenchida de preto
    land = cfeature.NaturalEarthFeature(
        category='physical', name='land', scale='110m',
        edgecolor='black', facecolor='.2'
    )
    ax.add_feature(land)
    levels= np.arange(-2, 36, 2)

    img1 = sst.plot.contourf(ax=ax, levels=levels, transform=ccrs.PlateCarree(), cmap='turbo', add_colorbar=False, extend='both')

    plt.title(f'Média mensal da temperatura da superfície do mar (°C)\nProjeção polar (Hemisfério Sul)\nNOAA OI SST V2 High Resolution 0.25° x 0.25°\n{tempo1}')
    cax_ = fig.add_axes([0.92, 0.2, 0.03, 0.6])

    cbar = fig.colorbar(img1, cax=cax_, orientation='vertical', shrink=0.8, pad=0.05, label = "Temperatura da Superfície do Mar (°C)", ticks=np.arange(-2, 36, 4))  

    ax.gridlines()

    plt.savefig(f"{DIRFIGS}south_pole_sst_{tempo1}.jpg", dpi=90, bbox_inches='tight')
    plt.close()
    del fig, ax, img1  # Remove objetos da memória
    ds_sst.close()
ds_sst.close()

