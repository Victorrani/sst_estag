import sys
import time
import os


DIR_BASE = os.getcwd()
DIR_SCRIPTS = os.path.join(DIR_BASE, 'scripts')

sys.path.append(DIR_SCRIPTS)  # Adiciona ao sys.path
import sst_download

inicio = time.time()  # Marca o tempo de início

sst_download.download_sst_data()

fim = time.time()  # Marca o tempo de fim

tempo_total = fim - inicio
print(f"Tempo de execução total do script: {tempo_total:.2f} segundos")
