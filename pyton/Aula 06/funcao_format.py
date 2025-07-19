# Criando um array de tamanho 5
numeros = [0] * 5

#Solicitando 5 inteiros ao usuário
for i in range(5):
    numeros[i] = int(input("Digite o {}º número inteiro: ".format(i + 1)))

#Imprimindo cada numero com sua posção na lista
for i, numero in enumerate(numeros):
    print("O número {} está na posição {} da lista.".format(numero, i))
    