import os
import json

# Nome do arquivo JSON 
arquivo_json = 'nomes.json'

#Verifica se o arquivo existe
if not os.path.exists(arquivo_json):
    # Se nao existir, cria o arquivo e inicializa com uma lista vazia
    with open(arquivo_json, 'w', encoding='utf-8') as arquivo:
        json.dump([], arquivo) # Cria uma lista vazia em formato Json
    print(f"Arquivo '{arquivo_json}' criado com uma lista vazia.")

# lê o conteúdo do arquivo
with open(arquivo_json, 'r', encoding='utf-8') as arquivo:
    nomes = json.load(arquivo)

#Verifica se a lista de nomes esta vazia
if not nomes:
    print("Lista de nomes vazia.")
else:
    print("Nomes encontrados:", nomes)
