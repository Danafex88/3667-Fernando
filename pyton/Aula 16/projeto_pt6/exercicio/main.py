from views.view_1 import view_1_menu
from views.view_2 import view_2_menu


def menu():
    while True:
        print("\nMenu Principal")
        print("1 - Ir para View 1")
        print("2 - Ir para View 2")
        print("3 -Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            """AQUI VOCÊ CHAMA VIEW 1"""
        elif opcao == '2':
            """AQUI VOCÊ CHAMA VIEW 2"""
        elif opcao == '3':
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
