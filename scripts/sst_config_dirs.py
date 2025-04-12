import os
import logging



# Diretório do script
DIR_SCRIPTS = os.path.dirname(os.path.abspath(__file__))


# Diretório base do projeto (sst_estag)
DIR_BASE = os.path.dirname(DIR_SCRIPTS)


def config_dirs():
    # Diretório do script
    DIR_SCRIPTS = os.path.dirname(os.path.abspath(__file__))
    
    # Diretório base do projeto (sst_estag)
    DIR_BASE = os.path.dirname(DIR_SCRIPTS)

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

if __name__ == "__main__":
    # Executa a função de download
    #print("\n[INFO] Criando os diretórios se necessário...")
    config_dirs()

    