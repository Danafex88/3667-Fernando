#Criando um dicionario
precos = {"banana": 3.50, "maça": 4.00, "laranja": 2.75}

#Adicionando um novo par chave-valor
precos["abacaxi"] = 5.50
print(precos)

#removendo um item do dicionario
del precos["maça"]
print(precos)

#Modificando o valor de uma chave exitente
precos["banana"] = 2.90
print(precos)

#Verificando se uma chave esta no dicionario 
print("abacaxi" in precos)

#Escrevendo o valor de uma chave especifica
print(precos["abacaxi"])
