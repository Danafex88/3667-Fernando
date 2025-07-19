from models.usuarioSistema import UsuarioSistema

def menu():
    sistema = UsuarioSistema()  # Não passa a lista inicial, pois a classe carrega do arquivo

    opcao = 0
    while opcao != 5:
        print("\nEscolha uma opção:")
        print("1 - Cadastrar Usuário")
        print("2 - Ler Usuários")
        print("3 - Atualizar Usuário")
        print("4 - Deletar Usuário")
        print("5 - Sair")

        try:
            opcao = int(input("Digite o número da opção desejada: "))
        except ValueError:
            print("Por favor, insira um número válido.")
            continue

        if opcao == 1:
            sistema.create()
        elif opcao == 2:
            sistema.read()
        elif opcao == 3:
            sistema.update()
        elif opcao == 4:
            sistema.delete()
        elif opcao == 5:
            print("Encerrando o sistema.")
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
