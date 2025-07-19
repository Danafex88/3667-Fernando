class ErroPersonalizado(Exception):
    def __init__(self, mensagem="Erro personalizad: valor negativo não permitido."):
        super().__init__(mensagem)

while True:
    try:
        numero = int(input("Digite um número:  "))
        if numero < 0:
            raise ErroPersonalizado
        resultado = 10 / numero
        print(f"Resultado : {resultado}")
        break
    except ValueError:
        print("Erro: Você deve digitar um número válido.")
    except ErroPersonalizado as e:
        print(e)
    except ZeroDivisionError:
        print("Erro: Não é possivel dividir por zero.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado {e}")
