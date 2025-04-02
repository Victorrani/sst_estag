# 📌 Estágio - Análise de SST 🌊

Este repositório contém scripts para leitura de dados de **Temperatura da Superfície do Mar (SST)** e geração de mapas com médias **mensais e anuais**.

## 🛠️ Funcionalidades
✔️ Leitura de arquivos de SST em formato NetCDF  
✔️ Cálculo de médias mensais e anuais  
✔️ Geração de mapas com colormap adequado  

## 📂 Estrutura do Repositório
```
/scripts       # Códigos para processamento e plotagem  
/dados         # Diretório para armazenar os arquivos de SST (não incluídos no GitHub)  
/figuras       # Mapas gerados pelos scripts  
README.md      # Descrição do projeto  
```

## 🚀 Como Usar
1. Baixe os dados de SST e coloque na pasta `/dados`.  
2. Execute o script principal:  
   ```bash
   python scripts/plot_sst.py
   ```  
3. As figuras serão salvas na pasta `/figuras`.  

