


import sys
import time

DIR_SCRIPT = "/p1-chima/victor/sst_estag/scripts/"
sys.path.append(DIR_SCRIPT)  # Adiciona ao sys.path
import sst_download

inicio = time.time()  # Marca o tempo de início

sst_download.download_sst_data()

fim = time.time()  # Marca o tempo de fim

tempo_total = fim - inicio
print(f"Tempo de execução: {tempo_total:.2f} segundos")
