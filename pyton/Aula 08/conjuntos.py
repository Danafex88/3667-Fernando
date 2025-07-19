#Criando um conjunto
frutas = {"banana", "maçã", "laranja"}

#Adicionando um item ao conjunto
frutas.add("abacaxi")
print(frutas)

#Removendo um item do conjunto
frutas.remove("maçã")
print(frutas)

#Tentando adicionar um item ja exitente (nao causa erro, mas o item nao é duplicado)
frutas.add("banana")
print(frutas)

#Verificando se um item esta no conjunto 
print("abacaxi" in frutas)
