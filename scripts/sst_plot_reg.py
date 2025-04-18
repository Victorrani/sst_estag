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


def plot_sst_reg(tipo, regiao):
    """
    Plota a temperatura da superfície do mar (SST) em projeção polar.
    Args:
        tipo (str): Tipo de média a ser plotada ('M' para mensal ou 'A' para anual).
        regiao lista: Lista com os limites da região a ser plotada [lon_min, lon_max, lat_min, lat_max].
    """
    # Configurações iniciais

    DIR_SCRIPTS = os.path.dirname(os.path.abspath(__file__))
    DIR_BASE = os.path.dirname(DIR_SCRIPTS)
    ARQ_SST_MENSAL = os.path.join(DIR_BASE, "dados", "sst_media_mensal.nc")
    ARQ_SST_ANUAL = os.path.join(DIR_BASE, "dados", "sst_media_anual.nc")
    DIRFIGS = os.path.join(DIR_BASE, "figs")
    DIR_REG = os.path.join(DIR_BASE, "figs", "regional")

    log_path = os.path.join(DIR_BASE, "logs", "sst_plot_reg.log")
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
    logging.info("Iniciando a criação das imagens com projeção regional dos dados de SST")

    if tipo not in ["M", "A"]:
        raise ValueError("O argumento 'tipo' deve ser 'M' para mensal ou 'A' para anual.")

    # Define diretórios e arquivos com base no tipo
    ARQ_SST = ARQ_SST_MENSAL if tipo == "M" else ARQ_SST_ANUAL
    subdir_tipo = "mensal" if tipo == "M" else "anual"
    DIR_SAIDA = os.path.join(DIR_REG, subdir_tipo)

    # Criar diretório de saída
    os.makedirs(DIR_SAIDA, exist_ok=True)

    ds_sst = xr.open_dataset(ARQ_SST, engine="netcdf4")

    tempos = ds_sst.month.values if tipo == "M" else ds_sst.year.values
    num_tempos = len(tempos)

    for i, tempo_valor in enumerate(tempos):
        dim = 'month' if tipo == "M" else 'year'
        sst = ds_sst['sst'].isel({dim: i}).load()
        sst_lat = ds_sst['lat']
        sst_lon = ds_sst['lon']

        if tipo == "M":
            tempo = pd.Timestamp(f"2000-{int(tempo_valor):02d}-01")
            tempo_str = tempo.strftime("%m")
            tempo_legenda = tempo.strftime('%B')
        else:
            tempo = int(tempo_valor)
            tempo_str = str(tempo)
            tempo_legenda = tempo_str

        logging.info(f"Fazendo para: {'Mês' if tipo == 'M' else 'Ano'} {tempo_str}")
        print((f"[INFO] Fazendo para: {'Mês' if tipo == 'M' else 'Ano'} {tempo_str}"))


        fig = plt.figure(figsize=[10, 5])
        ax1 = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
        
        fig.subplots_adjust(bottom=0.05, top=0.95, left=0.04, right=0.95, wspace=0.02)

        
        ax1.set_extent(regiao, ccrs.PlateCarree())


        ax1.add_feature(cfeature.NaturalEarthFeature(
                category='physical', name='land', scale='110m',
                edgecolor='black', facecolor='.2'))
        gl = ax1.gridlines(crs=ccrs.PlateCarree(), color='black',
                      alpha=1.0, linestyle='--', linewidth=0.4,
                      xlocs=np.arange(-180, 181, 30),  # Ajustar intervalo de longitude conforme necessário
                      ylocs=np.arange(-90, 90, 30),  # Ajustar intervalo de latitude conforme necessário
                      draw_labels=True)
        gl.top_labels = False  # Desativar rótulos no topo
        gl.right_labels = False  # Desativar rótulos à direita

    
        levels = np.arange(-2, 36, 1)
        img1 = sst.plot.contourf(ax=ax1, levels=levels, transform=ccrs.PlateCarree(), cmap='turbo', add_colorbar=False, extend='both', add_title=False)
        

        ax1.set_title(f"Média {'mensal' if tipo == 'M' else 'anual'} da Temperatura da Superfície do Mar (°C)\n"
    f"NOAA OI SST V2 High Resolution (0.25°)\n"
    f"{'Mês' if tipo == 'M' else 'Ano'}: {tempo_legenda}",
    fontsize=12)
        cbar = fig.colorbar(img1, ax=ax1 , orientation='vertical', shrink=0.8, pad=0.05, label="Temperatura da Superfície do Mar (°C)", ticks=np.arange(-2, 36, 2))
        cbar.ax.tick_params(labelsize=8)

        nome_fig = os.path.join(DIR_SAIDA, f"sst_reg_{tempo_str}.jpg")
        plt.savefig(nome_fig, dpi=300, bbox_inches='tight')
        plt.close()
        del fig, ax1, img1

    ds_sst.close()

#if __name__ == "__main__":
#    # Executa a função de download
#    print("\n[INFO] Iniciando a criação das imagens individualmente...")
#    plot_sst_reg("M")