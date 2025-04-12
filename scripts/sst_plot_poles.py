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
import logging

warnings.simplefilter("ignore", UserWarning)

DIR_SCRIPTS = os.path.dirname(os.path.abspath(__file__))
DIR_BASE = os.path.dirname(DIR_SCRIPTS)
ARQ_SST_MENSAL = os.path.join(DIR_BASE, "dados", "sst_media_mensal.nc")
ARQ_SST_ANUAL = os.path.join(DIR_BASE, "dados", "sst_media_anual.nc")
DIRFIGS = os.path.join(DIR_BASE, "figs")
DIR_POLAR = os.path.join(DIR_BASE, "figs", "polar")



# Configurar o log
log_path = os.path.join(DIR_BASE,'logs' ,"sst_plot_polar.log")
logging.basicConfig(
    filename=log_path,
    filemode='w',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)



def plot_polar_sst():

    # Criando diretórios das figuras
    if not os.path.exists(DIRFIGS):
        os.makedirs(DIRFIGS)
    if not os.path.exists(DIR_POLAR):
        os.makedirs(DIR_POLAR)
    
    # dado completo bruto
    ds_sst_mensal = xr.open_dataset(ARQ_SST_MENSAL, engine="netcdf4")
    num_tempos = len(ds_sst_mensal.month.values)
    
    logging.info(f"Iniciando o plot com projeção global")
    for i, mes in enumerate(ds_sst_mensal.month.values):
        sst = ds_sst_mensal['sst'].isel(month=i).load()
    

        sst_lat = ds_sst_mensal['lat']
        sst_lon = ds_sst_mensal['lon']
        
    
    
        tempo = pd.Timestamp(f"2000-{int(mes):02d}-01")
        tempo1 = tempo.strftime("%m")
        
        print(f"Fazendo para o tempo: {tempo.strftime('%m')}, {i}")
        logging.info(f"Fazendo para o tempo: {tempo.strftime('%m')}, {i}")
    
        fig = plt.figure(figsize=[10, 5])
        ax1 = fig.add_subplot(1, 2, 1, projection=ccrs.SouthPolarStereo())
        ax2 = fig.add_subplot(1, 2, 2, projection=ccrs.NorthPolarStereo())
        fig.subplots_adjust(bottom=0.05, top=0.95,
                            left=0.04, right=0.95, wspace=0.02)
    
        extent_sul = [-180, 180, -90, -30]
        extent_norte = [-180, 180, 90, 30]
        ax1.set_extent(extent_sul, ccrs.PlateCarree())
        ax2.set_extent(extent_norte, ccrs.PlateCarree())

        ax1.set_title('Hemisfério Sul')
        ax2.set_title('Hemisfério Norte')
    
        # Criar um círculo para limitar a projeção
        theta = np.linspace(0, 2*np.pi, 100)
        center, radius = [0.5, 0.5], 0.5
        verts = np.vstack([np.sin(theta), np.cos(theta)]).T
        circle = mpath.Path(verts * radius + center)
        ax1.set_boundary(circle, transform=ax1.transAxes)
    
        
    
        theta = np.linspace(0, 2*np.pi, 100)
        center, radius = [0.5, 0.5], 0.5
        verts = np.vstack([np.sin(theta), np.cos(theta)]).T
        circle = mpath.Path(verts * radius + center)
        ax2.set_boundary(circle, transform=ax2.transAxes)
    
        # Preencimento dos continentes
        land = cfeature.NaturalEarthFeature(
            category='physical', name='land', scale='110m',
            edgecolor='black', facecolor='.2'
        )
        ax1.add_feature(land)
    
        land = cfeature.NaturalEarthFeature(
            category='physical', name='land', scale='110m',
            edgecolor='black', facecolor='.2'
        )
        ax2.add_feature(land)

        fig.suptitle(
    f"Média mensal da Temperatura da Superfície do Mar (°C)\n"
    f"Projeção Polar | NOAA OI SST V2 High Resolution (0.25°)\n"
    f"Mês: {tempo.strftime('%B')}",
    fontsize=12,
    y=1.1  # pode ajustar se cortar
)


        levels= np.arange(-2, 36, 2)
    
        img1 = sst.plot.contourf(ax=ax1, levels=levels, transform=ccrs.PlateCarree(), cmap='turbo', add_colorbar=False, extend='both', add_title=False)
        ax1.set_title("Hemisfério Sul")

        cax_ = fig.add_axes([1, 0.2, 0.03, 0.6])
    
        cbar = fig.colorbar(img1, cax=cax_, orientation='vertical', shrink=0.8, pad=0.05, label = "Temperatura da Superfície do Mar (°C)", ticks=np.arange(-2, 36, 4))  
        cbar.ax.tick_params(labelsize=8)
        
    
        img2 = sst.plot.contourf(ax=ax2, levels=levels, transform=ccrs.PlateCarree(), cmap='turbo', add_colorbar=False, extend='both', add_title=False)
        ax2.set_title("Hemisfério Norte")

        nome_fig = os.path.join(DIR_POLAR, f"sst_polar_{tempo1}.jpg")
        plt.savefig(nome_fig, dpi=300, bbox_inches='tight')
        plt.close()
        del fig, ax1, img1, ax2, img2  # Remove objetos da memória
    ds_sst_mensal.close()
    
plot_polar_sst()