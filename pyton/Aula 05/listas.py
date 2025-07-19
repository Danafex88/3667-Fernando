#Criando uma lista de números
numeros = [1, 3, 5, 7, 9]

# Acessando elementos da lista
print("Primeiro elemento:", numeros [0])
print("Último elemnto:", numeros [-1])

# Modificando um elemento da lista
numeros[0] = 10
print("Lista após a modificação:", numeros)

# Adicionar um novo elemento à lista
numeros.append(6)
print("Lista após a adição:", numeros)

# remosvendo o ultimo elemento da lista
ultimo_elemento = numeros.pop()
print("Elemento removido:", ultimo_elemento)
print("Lista após a remoção:", numeros)

# Removendo um numero especifico da lista
numeros.remove(5)  # remove o numero 5 da lista
print("Lista após a remoção:", numeros)

# Removendo um elemento especifico pelo indice da lista
print("Elemento que será removido", numeros[2])
del numeros[2]  #Remove o elemento de indice 2 da lista
print("Lista após a remoção: ", numeros)



