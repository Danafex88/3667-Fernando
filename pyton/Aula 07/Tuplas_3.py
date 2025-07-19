tupla = (1, 2, 3, 2, 4, 5)

#Contando a ocorrencia do numero 2
print(tupla.count(2)) #Saida: 2

#Encontrando o indice da primeira ocorrencia do numero 2
print(tupla.index(2)) #Saida: 1

#Obtendo o comprimento da tupla
print(len(tupla))  #Saida: 6 

#Encontrando o maior elemento da tupla
print(max(tupla))  #Saida: 5

#Encontrando o menor elemento da tupla
print(min(tupla))  #Saida: 1

#Calculando a soma de todos os elementos da tupla
print (sum(tupla))  #Saida:  17

#Verificando se algum elemento é verdadeiro
print(any(tupla)) #Saida: True ( pois ha numeros diferentes de 0)

#Verificando se todos os elementos sao verdadeiros
print(all(tupla))  #Saida: True(pois todos sao diferentes de zero)

# Ordenando a tupla (retorna uma lista)
print(sorted(tupla)) #Saida: [1, 2, 2, 3, 4, 5]

#Revertendo a tupla (retorna um iterador)
print(list(reversed(tupla))) #Saida: [5, 4, 2, 3, 2, 1]

