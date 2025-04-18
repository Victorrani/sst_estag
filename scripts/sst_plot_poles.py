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




def plot_polar_sst(tipo):
    """
    Plota a temperatura da superfície do mar (SST) em projeção polar.
    Args:
        tipo (str): Tipo de média a ser plotada ('M' para mensal ou 'A' para anual).
    """
    # Configurações iniciais

    DIR_SCRIPTS = os.path.dirname(os.path.abspath(__file__))
    DIR_BASE = os.path.dirname(DIR_SCRIPTS)
    ARQ_SST_MENSAL = os.path.join(DIR_BASE, "dados", "sst_media_mensal.nc")
    ARQ_SST_ANUAL = os.path.join(DIR_BASE, "dados", "sst_media_anual.nc")
    DIRFIGS = os.path.join(DIR_BASE, "figs")
    DIR_POLAR = os.path.join(DIR_BASE, "figs", "polar")



    log_path = os.path.join(DIR_BASE, "logs", "sst_plot_polar.log")
    os.makedirs(os.path.dirname(log_path), exist_ok=True)

        # Reset logging config
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    logging.basicConfig(
        filename=log_path,
        filemode='a',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logging.info("Iniciando a criação das imagens com projeção polar dos dados de SST")

    if tipo not in ["M", "A"]:
        raise ValueError("O argumento 'tipo' deve ser 'M' para mensal ou 'A' para anual.")

    # Define diretórios e arquivos com base no tipo
    ARQ_SST = ARQ_SST_MENSAL if tipo == "M" else ARQ_SST_ANUAL
    subdir_tipo = "mensal" if tipo == "M" else "anual"
    DIR_SAIDA = os.path.join(DIR_POLAR, subdir_tipo)

    # Criar diretório de saída
    os.makedirs(DIR_SAIDA, exist_ok=True)

    # Abrir dataset
    ds_sst = xr.open_dataset(ARQ_SST, engine="netcdf4")

    tempos = ds_sst.month.values if tipo == "M" else ds_sst.year.values
    num_tempos = len(tempos)

    for i, tempo_valor in enumerate(tempos):
        dim = 'month' if tipo == "M" else 'year'
        sst = ds_sst['sst'].isel({dim: i}).load()
        sst_lat = ds_sst['lat']
        sst_lon = ds_sst['lon']

        if tipo == "M":
            tempo = pd.Timestamp(f"2000-{int(tempo_valor):02d}-01")  # fictício
            tempo_str = tempo.strftime("%m")
            tempo_legenda = tempo.strftime('%B')
        else:
            tempo = int(tempo_valor)
            tempo_str = str(tempo)
            tempo_legenda = tempo_str

        logging.info(f"Fazendo para: {'Mês' if tipo == 'M' else 'Ano'} {tempo_str}")
        print((f"[INFO] Fazendo para: {'Mês' if tipo == 'M' else 'Ano'} {tempo_str}"))


        fig = plt.figure(figsize=[10, 5])
        ax1 = fig.add_subplot(1, 2, 1, projection=ccrs.SouthPolarStereo())
        ax2 = fig.add_subplot(1, 2, 2, projection=ccrs.NorthPolarStereo())
        fig.subplots_adjust(bottom=0.05, top=0.95, left=0.04, right=0.95, wspace=0.02)

        ax1.set_extent([-180, 180, -90, -30], ccrs.PlateCarree())
        ax2.set_extent([-180, 180, 90, 30], ccrs.PlateCarree())

        for ax in [ax1, ax2]:
            theta = np.linspace(0, 2*np.pi, 100)
            center, radius = [0.5, 0.5], 0.5
            verts = np.vstack([np.sin(theta), np.cos(theta)]).T
            circle = mpath.Path(verts * radius + center)
            ax.set_boundary(circle, transform=ax.transAxes)
            ax.add_feature(cfeature.NaturalEarthFeature(
                category='physical', name='land', scale='110m',
                edgecolor='black', facecolor='.2'))

        fig.suptitle(
    f"Média {'mensal' if tipo == 'M' else 'anual'} da Temperatura da Superfície do Mar (°C)\n"
    f"Projeção Polar | NOAA OI SST V2 High Resolution (0.25°)\n"
    f"{'Mês' if tipo == 'M' else 'Ano'}: {tempo_legenda}",
    fontsize=12, y=1.1
)
        

        levels = np.arange(-2, 36, 2)
        img1 = sst.plot.contourf(ax=ax1, levels=levels, transform=ccrs.PlateCarree(), cmap='turbo', add_colorbar=False, extend='both', add_title=False)
        img2 = sst.plot.contourf(ax=ax2, levels=levels, transform=ccrs.PlateCarree(), cmap='turbo', add_colorbar=False, extend='both', add_title=False)

        ax1.set_title("Polo Sul", fontsize=10)
        ax2.set_title("Polo Norte", fontsize=10)
        cax_ = fig.add_axes([1, 0.2, 0.03, 0.6])
        cbar = fig.colorbar(img1, cax=cax_, orientation='vertical', shrink=0.8, pad=0.05, label="Temperatura da Superfície do Mar (°C)", ticks=np.arange(-2, 36, 4))
        cbar.ax.tick_params(labelsize=8)

        nome_fig = os.path.join(DIR_SAIDA, f"sst_polar_{tempo_str}.jpg")
        plt.savefig(nome_fig, dpi=300, bbox_inches='tight')
        plt.close()
        del fig, ax1, ax2, img1, img2

    ds_sst.close()

#if __name__ == "__main__":
#    # Executa a função de download
#    print("\n[INFO] Iniciando a criação das imagens individualmente...")
#    plot_polar_sst("A")
