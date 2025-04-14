import os
import logging





def config_dirs():
    """
    Função para configurar os diretórios do projeto.
    Cria diretórios principais: logs, dados e figs.
    """

    # Diretório do script
    DIR_SCRIPTS = os.path.dirname(os.path.abspath(__file__))

    # Diretório base do projeto (sst_estag)
    DIR_BASE = os.path.dirname(DIR_SCRIPTS)

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


# Caso queira rodar esse script individualmente descomente as linhas abaixo
#if __name__ == "__main__":
    #print("\n[INFO] Criando os diretórios se necessário...")
    #config_dirs()

    