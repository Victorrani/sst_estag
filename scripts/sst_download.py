import os
import wget
import logging
import time

################################
#         sst_download.py      #
################################

# Diretórios e nome do arquivo
DIR_DADOS = "/p1-chima/victor/sst_estag/dados/"
ARQ_FILE = "sst.mon.mean.nc"
DOWNLOAD_URL = "https://downloads.psl.noaa.gov/Datasets/noaa.oisst.v2.highres/sst.mon.mean.nc"
LOG_FILE = "/p1-chima/victor/sst_estag/logs/sst_download.log"

# Criando diretório de logs (se não existir)
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

# Configuração do logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,  # Registra INFO, WARNING e ERROR
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Função para baixar os dados
def download_sst_data():
    start_time = time.time()  # Tempo inicial

    os.makedirs(DIR_DADOS, exist_ok=True)
    caminho_arquivo = os.path.join(DIR_DADOS, ARQ_FILE)

    logging.info("Verificando a existência do dado...")

    if os.path.isfile(caminho_arquivo):
        logging.info(f"Arquivo já existe: {caminho_arquivo}")
        print(f"Arquivo já existe: {caminho_arquivo}")
    else:
        logging.info("Arquivo não encontrado. Iniciando download...")
        print("Arquivo não encontrado. Iniciando download...")
        try:
            wget.download(DOWNLOAD_URL, caminho_arquivo)
            logging.info(f"Download concluído: {caminho_arquivo}")
            print(f"\nDownload concluído: {caminho_arquivo}")
        except Exception as e:
            logging.error(f"Erro ao baixar o arquivo: {e}")
            print(f"\nErro ao baixar o arquivo: {e}")

    # Tempo final
    end_time = time.time()
    elapsed_time = end_time - start_time
    logging.info(f"Tempo de execução: {elapsed_time:.2f} segundos")
    print(f"Tempo de execução: {elapsed_time:.2f} segundos")

