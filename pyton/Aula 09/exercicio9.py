usuarios = ["Bruno", "Guilherme"]

def create():
    novo_usuario = input("Digite o nome do novo usuário:  ")
    usuarios.append(novo_usuario)
    print(f"Usuário {novo_usuario} cadastrado com sucesso!")

def read():
    print("Usuários cadastrados:")
    for i, usuario in enumerate(usuarios, start=1):
        print(f"{i}. {usuario}")

def update():
    read()
    indice = int(input("Digite o número de usuarios que desja atualizar:  ")) - 1
    if 0 <= indice < len(usuarios):
        novo_nome = input(f"Digite o novo nome para {usuarios[indice]}:  ")
        usuarios[indice] = novo_nome
        print(f"Usuário atualizado para {novo_nome} com sucesso!")
    else:
        print("Usuário Inválido.")

def delete():
    read()
    indice = int(input("Digite o número do usário que deseja excluir:  ")) - 1
    if 0 <= indice < len(usuarios):
        removido = usuarios.pop(indice)
        print(f"Usuários {removido} excluido com sucesso!")
    else:
        print("Usuario inválido.")

def menu():
    opcao = 0
    while opcao != 5:
        print("\n Escolha uma opção:")
        print("1 - Cadastrar Usuários")
        print("2 - Ler Usuários")
        print("3 - Atualizar Usuários")
        print("4 - Deletst Usuário")
        print("5 - Sair")

        opcao = int(input("Digite o número da opção desejada:  "))

        if opcao == 1:
            create()
        elif opcao == 2:
            read()
        elif opcao == 3:
            update()
        elif opcao == 4:
            delete()
        elif opcao == 5:
            print("Encerrando o sistema.")
        else:
            print("Opção Inválida. Tente Novamente.")

## -- Inicio -- ##
menu()
