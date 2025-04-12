import sys
import time
import os


DIR_BASE = os.getcwd()
DIR_SCRIPTS = os.path.join(DIR_BASE, 'scripts')

sys.path.append(DIR_SCRIPTS)  # Adiciona ao sys.path
import sst_download
import sst_process
import sst_plot_poles

inicio = time.time()  # Marca o tempo de início

sst_download.download_sst_data()

sst_process.process_sst_data()

sst_plot_poles.plot_polar_sst()

fim = time.time()  # Marca o tempo de fim

tempo_total = (fim - inicio) / 60
print(f"Tempo de execução total do script: {tempo_total:.2f} minutos")
