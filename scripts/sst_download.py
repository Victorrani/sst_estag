import os
import wget
import logging
import time

#############################################
#              sst_download.py              #
#-------------------------------------------#
# Script para baixar dados mensais de SST   #
# NOAA OISST V2 HighRes                     #
#############################################

# Diretório do script
DIR_SCRIPTS = os.path.dirname(os.path.abspath(__file__))
print(f"[INFO] Diretório do script: {DIR_SCRIPTS}")

# Diretório base do projeto (sst_estag)
DIR_BASE = os.path.dirname(DIR_SCRIPTS)
print(f"[INFO] Diretório base do projeto: {DIR_BASE}")

# Criando diretórios principais do projeto
name_dir = ['logs', 'dados', 'figs']

print("\n[INFO] Verificando/criando diretórios necessários:")
for dir_name in name_dir:
    caminho = os.path.join(DIR_BASE, dir_name)
    if os.path.exists(caminho):
        print(f"Diretório já existe: {caminho}")
    else:
        os.makedirs(caminho)
        print(f"Diretório criado: {caminho}")

# Arquivo, URL e caminhos de log/dados
ARQ_FILE = "sst.mon.mean.nc"
DOWNLOAD_URL = "https://downloads.psl.noaa.gov/Datasets/noaa.oisst.v2.highres/sst.mon.mean.nc"
LOG_FILE = os.path.join(DIR_BASE, 'logs', 'sst_download.log')
DIR_DADOS = os.path.join(DIR_BASE, 'dados')

# Configurando o log
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Função para baixar os dados
def download_sst_data():
    start_time = time.time()
    caminho_arquivo = os.path.join(DIR_DADOS, ARQ_FILE)

    logging.info("Verificando a existência do dado SST.")
    print("\n[INFO] Verificando se o arquivo já existe...")

    if os.path.isfile(caminho_arquivo):
        msg = f"Arquivo já existe: {caminho_arquivo}"
        logging.info(msg)
        print(f"{msg}")
    else:
        msg = "Arquivo não encontrado. Iniciando download..."
        logging.info(msg)
        print(f"{msg}")
        try:
            wget.download(DOWNLOAD_URL, caminho_arquivo)
            logging.info(f"Download concluído: {caminho_arquivo}")
            print(f"\nDownload concluído: {caminho_arquivo}")
        except Exception as e:
            logging.error(f"Erro ao baixar o arquivo: {e}")
            print(f"\nErro ao baixar o arquivo: {e}")

    elapsed_time = time.time() - start_time
    minutos = int(elapsed_time // 60)
    segundos = int(elapsed_time % 60)

    logging.info(f"Tempo total de execução do Download: {minutos} min {segundos} s")
    print(f"\n[INFO] Tempo total de execução do Download: {minutos} min {segundos} s")

# Caso queira rodar esse script individualmente descomente as linhas abaixo
# if __name__ == "__main__":
#     # Executa a função de download
#     print("\n[INFO] Iniciando o download do arquivo SST...")
#     download_sst_data()
