#1. Criando uma lista de frutas disponiveis
frutas_disponiveis = ["banana", "maça", "laranja"]

#2. Criando uma tupla com informações sobre uma fruta 
#(nome, preço, quantidade)
info_fruta =("banana", 3.50, 20)

#3. Criando um conjunto de frutas fora do estoque
frutas_fora_de_estoque = {"maçã", "kiwi"}

#4. Criando um dicionario para associar frutas a preços e quantidades
estoque = {
        "banana": {"preço": 3.50, "quantidade" : 20},
        "laranja": {"preço": 2.75, "quantidade": 15},
}

#Exibindo informações
print("Frutas disponiveis:", frutas_disponiveis)
print("Informações sobre a fruta:", info_fruta)
print("Frutas fora do estoque:", frutas_fora_de_estoque)
print("Estoque atualizado:", estoque)

#Exibindo preço e quantidade da banana
print("Preço da banana:", estoque["banana"]["preço"])
print("Quantidade de banana:", estoque["banana"]["quantidade"])
