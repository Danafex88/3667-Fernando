#Menu Para usuario
def menu():
    print("Escolha uma das opções: ")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair")

#Funçoes basicas da calculadora
def somar(a, b):
    return a + b

def subtrair (a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por Zero"
    return a / b


#Programação Principal
opcao = None

while opcao != "5":
    menu()
    opcao = input("Digite sua escolha:  ")

    if opcao == "5":
        print("Saindo da calculadora. ")
        break

    if opcao in ["1", "2", "3", "4"]:
        num1 = float(input("Digite o primeiro número:  "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == "1":
            print(f"Resultado da soma: {somar(num1, num2)} ")
        elif opcao == "2":
            print(f"Resultado da subrtração: {subtrair(num1, num2)}  ")
        elif opcao == "23":
            print(f"Resultado da multiplicação:{multiplicar(num1, num2)}  ")
        elif opcao == "4":
            print(f"Resultado da divisão: {dividir(num1, num2)}  ")

    else:
        print("Opção Invalida. Tente novamente.")
        
        