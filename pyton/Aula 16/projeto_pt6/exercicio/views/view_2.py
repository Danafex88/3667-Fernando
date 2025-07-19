def view_2_menu():
    while True:
        print("\nVocê esta na View 2")
        print("1 - Voltar ao menu Principal")
        print("2 - Sair do sistema")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            break
        elif opcao == '2':
            print("Saindo do Sistema.")
            exit()
        else:
            print("Opção inválida. Tente novamente.")
