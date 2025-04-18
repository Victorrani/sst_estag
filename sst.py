import sys
import time
import os


#############################################
#               sst.py                      #
#-------------------------------------------#
# SCRIPT principal para gerar figuras SST   #
# NOAA OISST V2 HighRes                     #
#############################################

DIR_BASE = os.getcwd()
DIR_SCRIPTS = os.path.join(DIR_BASE, 'scripts')

sys.path.append(DIR_SCRIPTS)
import sst_download
import sst_process
import sst_plot_poles
import sst_config_dirs
import sst_plot_reg
import sst_gifs

inicio = time.time()  # Marca o tempo de início

# Você pode utiizar cada função de forma independente

## configuração / download / processamento
sst_config_dirs.config_dirs() # prepara o ambiente

sst_download.download_sst_data() # donwload do arquivo

sst_process.process_sst_data() # processa o arquivo

## plot polar
sst_plot_poles.plot_polar_sst("A") # plota projeção polar anual

sst_plot_poles.plot_polar_sst("M") # plota projeção polar mensal

## plot regional / global
globe = [-180, 180, -90, 90]
atlantico = [-90, 20, -60, 60]
escolha_usuario  = [-180, -70 , -90, 90] 

sst_plot_reg.plot_sst_reg('A', globe) # plota projeção regional anual

sst_plot_reg.plot_sst_reg('M', globe) # plota projeção regional mensal

## criação dos gifs
sst_gifs.sst_cria_gif(400) # cria gifs

fim = time.time()  # Marca o tempo de fim

tempo_total = (fim - inicio) / 60
print(f"Tempo de execução total do script: {tempo_total:.2f} minutos")
