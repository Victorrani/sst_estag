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

## 🚀 Como Usar
1. Baixe os dados de SST e coloque na pasta `/dados`.
1.1 O dado utilizado pode ser encontrado aqui: https://psl.noaa.gov/data/gridded/data.noaa.oisst.v2.highres.html
1.2 Descrição:
Monthly values from 1981/09 to 2025/04
0.25 degree latitude x 0.25 degree longitude global grid (1440x720)
89.875S - 89.875N,0.125E to 359.875E
nome do arquivo: sst.mon.mean.nc


2. Execute o script principal:  
   ```bash
   python scripts/plot_sst.py
   ```  
3. As figuras serão salvas na pasta `/figuras`.  

