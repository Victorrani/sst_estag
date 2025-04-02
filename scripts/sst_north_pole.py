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
DIRFIGS = '/p1-chima/victor/estagio/figs/north_pole_imgs/'

# dado completo bruto
ds_sst = xr.open_dataset(DIRDADO)

num_tempos = len(ds_sst.time.values)

for i in range(250, num_tempos):
    sst = ds_sst['sst'].isel(time=i)



    tempo = pd.to_datetime(sst.time.values)
    tempo1 = tempo.strftime('%Y-%m')
    
    print(f"Fazendo para o tempo: {tempo.strftime('%Y-%m')}, {i}")

    # Criando a figura e o eixo com projeção polar sul
    extent = [0, 360, 0, 90]
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.NorthPolarStereo())

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
    levels= np.arange(-2, 34, 2)

    img1 = sst.plot.contourf(ax=ax, levels=levels, transform=ccrs.PlateCarree(), cmap='turbo', add_colorbar=False, extend='both')

    plt.title(f'Média mensal da temperatura da superfície do mar (°C)\nProjeção polar (Hemisfério Norte)\n{tempo1}')
    cax_ = fig.add_axes([0.92, 0.2, 0.03, 0.6])

    cbar = fig.colorbar(img1, cax=cax_, orientation='vertical', shrink=0.8, pad=0.05, label = "Temperatura da Superfície do Mar (°C)", ticks=np.arange(-2, 34, 2))  

    ax.gridlines()

    plt.savefig(f"{DIRFIGS}/north_pole_sst_{tempo1}.png", dpi=100, bbox_inches='tight')
    plt.close()


