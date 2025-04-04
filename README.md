#  Estágio - Análise de SST 

Este repositório contém scripts para leitura de dados de **Temperatura da Superfície do Mar (SST)** e geração de mapas com médias **mensais e anuais**.

##  Funcionalidades
-> Leitura de arquivos de SST em formato NetCDF  
-> Cálculo de médias mensais e anuais  
-> Geração de mapas com diversas projeções (polar, global e regional)  

##  Estrutura do Repositório
```
/scripts       # Códigos para processamento e plotagem  
/dados         # Diretório para armazenar os arquivos de SST (não incluídos no GitHub)  
/figs       # Mapas gerados pelos scripts  
README.md      # Descrição do projeto  
```

## Como Usar
1. Baixe os dados de SST e coloque na pasta `/dados`.
1.1 O dado utilizado pode ser encontrado aqui: https://psl.noaa.gov/data/gridded/data.noaa.oisst.v2.highres.html
-> https://downloads.psl.noaa.gov/Datasets/noaa.oisst.v2.highres/sst.mon.mean.nc
1.2 Descrição:
Monthly values from 1981/09 to 2025/04
0.25 degree latitude x 0.25 degree longitude global grid (1440x720)
89.875S - 89.875N,0.125E to 359.875E

2. Execute o script principal:  
   ```bash
   python scripts/plot_sst.py
   ```  
   
📂 sst_estag/
├── 📜 sst.py → Script principal que chama as funções na ordem correta.
├── 📜 config.yaml → Arquivo de configuração para ambiente Anaconda.
├── 📂 scripts/
│ ├── 📜 sst_download.py → Função para baixar os dados.
│ ├── 📜 sst_process.py → Tratamento dos dados brutos.
│ ├── 📜 sst_plot_polar.py → Geração de imagens em projeção polar.
│ ├── 📜 sst_plot_global.py → Geração de imagens para visão global.
│ ├── 📜 sst_plot_regional.py → Geração de imagens para regiões específicas.
├── 📂 data/ → Pasta onde os dados baixados serão armazenados.
├── 📂 figs/ → Pasta para salvar imagens e resultados finais.
├── 📜 README.md → Explicação do repositório.


