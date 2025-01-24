import os
import shutil
import xml.etree.ElementTree as ET

# Carrega o arquivo XML
tree = ET.parse('2200301011.xml')  # Substitua 'arquivo.xml' pelo caminho do seu arquivo
root = tree.getroot()

# Função para buscar o termo dentro do XML
def buscar_termo(elemento, termo):
    if elemento.text and termo in elemento.text:
        return True
    for child in elemento:
        if buscar_termo(child, termo):
            return True
    return False

def processar_arquivos_xml(pasta_origem, pasta_destino, termo):
    # Verifica se a pasta de destino existe; caso contrário, cria
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    # Itera sobre todos os arquivos da pasta de origem
    for arquivo in os.listdir(pasta_origem):
        if arquivo.endswith(".xml"):
            caminho_arquivo = os.path.join(pasta_origem, arquivo)
            
            # Carrega o arquivo XML
            try:
                tree = ET.parse(caminho_arquivo)
                root = tree.getroot()
                
                # Verifica se o termo está presente no XML
                if buscar_termo(root, termo):
                    # Copia o arquivo para a pasta de destino se o termo for encontrado
                    shutil.copy(caminho_arquivo, pasta_destino)
                    print(f'Termo encontrado no arquivo: {arquivo}. Copiado para a pasta destino.')
                else:
                    print(f'Termo NÃO encontrado no arquivo: {arquivo}.')
            except ET.ParseError:
                print(f'Erro ao ler o arquivo XML: {arquivo}. Pulando...')

# Caminhos das pastas
pasta_origem = r'C:\Users\Renan\Desktop\Renan\python\ExtracaoDOU\S02082012'  
pasta_destino = r'C:\Users\Renan\Desktop\Renan\python\ExtracaoDOU\ExercicioAnterior'  
termo = 'art. 248'

# Processar os arquivos XML
processar_arquivos_xml(pasta_origem, pasta_destino, termo)
