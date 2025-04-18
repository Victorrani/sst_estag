# Estágio - Análise de Temperatura da Superfície do Mar (SST)

Este repositório contém scripts para leitura, processamento e visualização de dados de **Temperatura da Superfície do Mar (SST)**, com foco em médias **mensais** e **anuais**. O projeto visa automatizar o fluxo de trabalho desde o download dos dados até a geração dos mapas.

---

## Funcionalidades
- Preparação dos diretórios necessários
- Leitura de arquivos SST no formato NetCDF  
- Cálculo de médias mensais e anuais  
- Geração de mapas com diferentes projeções:
  - Projeção polar
  - Projeção regional (podendo ser alterado de acordo com a necessidade)

---

## Como Usar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/sst_estag.git
   cd sst_estag
   ```

2. Crie o ambiente Conda:
   ```bash
   conda env create -f environment.yml -n sst
   conda activate sst
   ```

3. Execute o script principal:
   ```bash
   python sst.py
   ```

O script (`sst.py`) executa automaticamente todas as etapas: **download dos dados, processamento e geração dos mapas**.

> Alternativamente, os scripts localizados no diretório `scripts/` podem ser executados individualmente, conforme necessidade (não se esqueça de descomentar as linhas finais de cada script).

---

## Dados Utilizados

- Arquivo: `sst.mon.mean.nc`
- Fonte: [NOAA PSL](https://psl.noaa.gov/data/gridded/data.noaa.oisst.v2.highres.html)
- Link direto:  
  https://downloads.psl.noaa.gov/Datasets/noaa.oisst.v2.highres/sst.mon.mean.nc  
- Descrição:
  - Resolução espacial: 0.25° x 0.25°
  - Cobertura global: 89.875S - 89.875N, 0.125E - 359.875E
  - Período: setembro/1981 até abril/2025

---

## Estrutura do Repositório

```
sst_estag/
├── sst.py                   # Script principal que executa todo o fluxo (download, processamento, plotagem)
├── environment.yml          # Arquivo de configuração para ambiente Conda
├── scripts/                 # Scripts individuais para cada etapa do fluxo
│   ├── sst_config_dirs.py      # Configura os diretórios do projeto
│   ├── sst_download.py         # Script para download dos dados de SST
│   ├── sst_process.py          # Processamento dos dados e cálculo de médias (mensal/anual)
│   ├── sst_plot_poles.py       # Geração de mapas com projeção polar (hemisférios Norte e Sul)
│   ├── sst_plot_reg.py         # Geração de mapas para regiões específicas (ex: Atlântico, Pacífico etc.)
│   ├── sst_gifs.py             # Criação de GIFs animados com as imagens geradas
├── dados/                  # Pasta onde os dados de SST são armazenados
├── figs/                   # Imagens geradas pelos scripts
│   ├── polar/
│   │   ├── mensal/
│   │   └── anual/
│   ├── regional/
│   │   ├── mensal/
│   │   └── anual/
├── logs/                   # Arquivos de log com histórico das execuções
└── README.md               # Explicação do projeto e instruções de uso
```
