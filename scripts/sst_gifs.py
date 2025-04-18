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
from PIL import Image


def sst_cria_gif(duracao):
    """
    Cria GIFs animados com imagens de SST em todos os subdiretórios de 'figs'.
    Args:
        duracao (int): Duração de cada frame do GIF em milissegundos.
    """
    DIR_SCRIPTS = os.path.dirname(os.path.abspath(__file__))
    DIR_BASE = os.path.dirname(DIR_SCRIPTS)
    DIR_FIGS = os.path.join(DIR_BASE, "figs")

    log_path = os.path.join(DIR_BASE, "logs", "sst_GIFS.log")
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
    logging.info("Iniciando a criação dos gifs")

    subdirs = [
        os.path.join(DIR_FIGS, "polar", "mensal"),
        os.path.join(DIR_FIGS, "polar", "anual"),
        os.path.join(DIR_FIGS, "regional", "mensal"),
        os.path.join(DIR_FIGS, "regional", "anual"),
    ]

    for pasta in subdirs:
        imagens = sorted([
            os.path.join(pasta, f) for f in os.listdir(pasta)
            if f.endswith(".jpg")
        ])

        if not imagens:
            print(f"[AVISO] Nenhuma imagem .jpg encontrada em: {pasta}")
            logging.warning(f"Nenhuma imagem .jpg encontrada em: {pasta}")
            continue

        frames = [Image.open(img) for img in imagens]
        nome_gif = os.path.join(pasta, "sst_animado.gif")

        frames[0].save(
            nome_gif,
            format='GIF',
            save_all=True,
            append_images=frames[1:],
            duration=duracao,
            loop=0,
            optimize=True,
            quality=95,
        )

        print(f"[GIF] Criado com sucesso: {nome_gif}")
        logging.info("GIFs criados com sucesso.")

#if __name__ == "__main__":
#    sst_cria_gif(300)