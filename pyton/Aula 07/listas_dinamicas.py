lista_de_carros = []

quantidade = int(input("Quantos carros você deseja adicionar á Lista? "))

# Adiciona carros a linsta dconforme a quantidade especificada
for i in range(quantidade):
    carro = input(f"Digite o nome do carro {i}: ")
    lista_de_carros.append(carro)

    print("Lista de carros criada:", lista_de_carros)

#Cria um loop para exibir a posição e o carro da lista
for index, carro in enumerate(lista_de_carros):
    print(f"Na posição {index} está o carro : {carro}")

#Solicita o indice par excluir
indice_exclusao = int(input(f"Digite o Indice de 0 a {len(lista_de_carros) -1} para excluir um carro "))

#Verifica se o Indice esta dentro do intervalo valido
if 0 <= indice_exclusao < len(lista_de_carros):
        carro_removido = lista_de_carros.pop(indice_exclusao)
        print(f"Carro '{carro_removido}' foi removido da lista.")
else:
     print("Erro: indice inválido. ")
     
