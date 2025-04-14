import xarray as xr
import os
import numpy as np
import pandas as pd
import logging

################################
#         sst_process.py       #
################################

def process_sst_data():

    """
    Função para processar dados de temperatura da superfície do mar (SST).
    Lê o arquivo de dados, calcula a média anual e mensal, e salva os resultados.
    """
    # Diretório do script e base do projeto
    DIR_SCRIPTS = os.path.dirname(os.path.abspath(__file__))
    DIR_BASE = os.path.dirname(DIR_SCRIPTS)

    # Caminhos
    ARQ_SST = os.path.join(DIR_BASE, "dados", "sst.mon.mean.nc")
    DIR_SAIDA = os.path.join(DIR_BASE, "dados")
    LOG_FILE = os.path.join(DIR_BASE, "logs", "sst_process.log")

    # Logger
    logger = logging.getLogger("sst_process_logger")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = logging.FileHandler(LOG_FILE)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", "%Y-%m-%d %H:%M:%S")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    logger.info("Iniciando o processamento dos dados de SST")

    try:
        # Verificação de existência e tamanho do arquivo
        if not os.path.isfile(ARQ_SST):
            msg = f"Arquivo não encontrado: {ARQ_SST}"
            logger.error(msg)
            print(f"[ERRO] {msg}")
            return

        tamanho_arquivo = os.path.getsize(ARQ_SST)
        tamanho_gb = tamanho_arquivo / (1024 ** 3)

        if tamanho_gb < 2:
            msg = f"Arquivo encontrado, mas tem apenas {tamanho_gb:.2f} GB. Tamanho esperado: ≥ 2 GB."
            logger.error(msg)
            print(f"[ERRO] {msg}")
            return

        logger.info(f"Arquivo encontrado com {tamanho_gb:.2f} GB: {ARQ_SST}")
        print(f"[INFO] Arquivo OK: {ARQ_SST} ({tamanho_gb:.2f} GB)")

        # Lendo o dataset
        logger.info(f"Lendo arquivo: {ARQ_SST}")
        ds_sst = xr.open_dataset(ARQ_SST)

        # Pegando a variável SST
        var_sst = ds_sst["sst"]

        # Nome da variável e unidades
        nome_variavel = var_sst.name
        unidade = var_sst.attrs.get("units", "sem unidade")

        # Valores mínimo e máximo
        valor_min = float(var_sst.min().values)
        valor_max = float(var_sst.max().values)

        # Log e print das informações
        logger.info(f"Nome da variável: {nome_variavel}")
        logger.info(f"Unidade: {unidade}")
        logger.info(f"Valor mínimo: {valor_min:.2f}")
        logger.info(f"Valor máximo: {valor_max:.2f}")

        print("\n[INFO] Informações do arquivo SST:")
        print(f"→ Variável: {nome_variavel}")
        print(f"→ Unidade: {unidade}")
        print(f"→ Valor mínimo: {valor_min:.2f}")
        print(f"→ Valor máximo: {valor_max:.2f}")

        # Média global anual
        logger.info("Calculando média anual")
        sst_media_anual = ds_sst["sst"].groupby("time.year").mean(dim="time")

        # Média climatológica mensal
        logger.info("Calculando média mensal")
        sst_media_mensal = ds_sst["sst"].groupby("time.month").mean(dim="time")

        # Salvando os arquivos
        saida_anual = os.path.join(DIR_SAIDA, "sst_media_anual.nc")
        saida_mensal = os.path.join(DIR_SAIDA, "sst_media_mensal.nc")

        sst_media_anual.to_netcdf(saida_anual)
        logger.info(f"Média anual salva em: {saida_anual}")

        sst_media_mensal.to_netcdf(saida_mensal)
        logger.info(f"Média mensal salva em: {saida_mensal}")

        logger.info("Processamento concluído com sucesso!")

        ds_sst.close()

    except Exception as e:
        logger.error(f"Erro durante o processamento: {e}")
        print(f"[ERRO] {e}")

# Caso queira rodar esse script individualmente descomente as linhas abaixo
#if __name__ == "__main__":
#    print("\n[INFO] Iniciando processamento dos dados de SST...")
#    process_sst_data()
