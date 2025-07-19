import os
import json

# Criar a pasta " Dados " se ela nao existir
if not os.path.exists('exercicio13/dados'):
    os.makedirs('exercicio13/dados')

frutas = ["Maçã", "Laranja", "Carambola", "Pitanga"]

#Caminho do arquivo onde a lista sera salva
caminho_arquivo = os.path.join('exercicio13/dados', 'frutas.json')

#Salvando a lista no arquivo JSON
with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo_json:
    json.dump(frutas, arquivo_json, ensure_ascii=False, indent=4)

print(f'Arquivo {caminho_arquivo} criado com sucesso!')
