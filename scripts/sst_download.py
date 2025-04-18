import os
import wget
import logging
import time

####################################################
#              sst_download.py                     #
#--------------------------------------------------#
# Script para baixar dados méidas mensais de SST   #
# NOAA OISST V2 HighRes                            #
####################################################


def download_sst_data():
    """
    Função para baixar os dados de temperatura da superfície do mar (SST) da NOAA OISST V2 HighRes.
    O arquivo é baixado apenas se não existir ou se o tamanho for menor que 2 GB.
    """
    # Diretório do script
    DIR_SCRIPTS = os.path.dirname(os.path.abspath(__file__))
    print(f"[INFO] Diretório do script: {DIR_SCRIPTS}")
    
    # Diretório base do projeto (sst_estag)
    DIR_BASE = os.path.dirname(DIR_SCRIPTS)
    
    # Arquivo, URL e caminhos de log/dados
    ARQ_FILE = "sst.mon.mean.nc"
    DOWNLOAD_URL = "https://downloads.psl.noaa.gov/Datasets/noaa.oisst.v2.highres/sst.mon.mean.nc"
    LOG_FILE = os.path.join(DIR_BASE, 'logs', 'sst_download.log')
    DIR_DADOS = os.path.join(DIR_BASE, 'dados')
    
    # Configurando o log
    
    logging.basicConfig(
        filename=LOG_FILE,
        filemode='a',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logging.info("Iniciando a criação das imagens com projeção polar dos dados de SST")

    start_time = time.time()
    caminho_arquivo = os.path.join(DIR_DADOS, ARQ_FILE)

    logging.info("Verificando a existência do dado SST.")
    print("\n[INFO] Verificando se o arquivo já existe...")

    if os.path.isfile(caminho_arquivo):
        tamanho_arquivo = os.path.getsize(caminho_arquivo)
        tamanho_gb = tamanho_arquivo / (1024 ** 3)

        if tamanho_gb > 2:
            msg = f"Arquivo já existe e tem {tamanho_gb:.2f} GB: {caminho_arquivo}"
            logging.info(msg)
            print(f"{msg}")
        else:
            msg = f"Arquivo existe mas tem apenas {tamanho_gb:.2f} GB. Iniciando novo download..."
            logging.info(msg)
            print(f"{msg}")
            try:
                wget.download(DOWNLOAD_URL, caminho_arquivo)
                logging.info(f"Download concluído: {caminho_arquivo}")
                print(f"\nDownload concluído: {caminho_arquivo}")
            except Exception as e:
                logging.error(f"Erro ao baixar o arquivo: {e}")
                print(f"\nErro ao baixar o arquivo: {e}")
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
#if __name__ == "__main__":
#    # Executa a função de download
#    print("\n[INFO] Iniciando o download do arquivo SST individualmente...")
#    download_sst_data()
