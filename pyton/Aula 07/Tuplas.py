#Criando uma tupla
carros = ("Fusca", "Civic", "Corolla")

#Acessando elementos
print(carros[0])   #Fusca

#Tentar modificar uma tulpa gera erro
#carros[0] = "Ferrari"  #Isso causara erro!

# Para adicionar ou remover elementos, é necessario criar uma nova tulpa
carros = carros +("Ferrari",)
print(carros)

# licing (possivel em listas, puplas e trings)
print(carros[2:])   #(Corolla, ferrari)
