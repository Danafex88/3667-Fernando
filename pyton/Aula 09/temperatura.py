#Fução para converter Celsius para Fahrenheit
def celsius_para_Fahrenheit(celsius):
    return(celsius * 9/5) + 32

#Função para converter Fahrenheit em Celsius
def Fahrenheit_para_celsius(Fahrenheit):
    return (Fahrenheit - 32) *5/9

#Menu para usário
def menu():
    print("Escolha uma das opções: ")
    print("1 - Converter Celsius para Fahrenheit")
    print("2 - Converter Fahrenheit para Celsius")
    print("3 - Sair")

# Programa Principal
opcao = None

while opcao != "3":
    menu()
    opcao = input("Digite sua escolha:  ")
    
    if opcao == "3":
        print("Saindo do programa.")
        break

    if opcao in ["1", "2"]:
        temperatura = float(input("Digite a temperatura:  "))

        if opcao == "1":
            resultado = celsius_para_Fahrenheit(temperatura)
            print(f"{temperatura} °C é igual a {resultado} °F")

        elif opcao == "2":
            resultado = Fahrenheit_para_celsius(temperatura)
            print(f"{temperatura} °F é igual a {resultado}  °C")

    else:
        print("Opção Invalida. Tente Novamente.")
