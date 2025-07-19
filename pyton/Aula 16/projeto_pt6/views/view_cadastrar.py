from models.usuarioSistema import UsuarioSistema


def view_cadastrar(sistema: UsuarioSistema):
    print("Você escolheu a opção Cadastrar")
    novo_usuario = input("Digite o nome do novo usuario: ")
    sistema.create(novo_usuario)
