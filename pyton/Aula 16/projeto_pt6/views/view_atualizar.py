from models.usuarioSistema import UsuarioSistema


def view_atualizar(sistema: UsuarioSistema):
    print("Você escolheu a opção Atualizar")
    sistema.update()
