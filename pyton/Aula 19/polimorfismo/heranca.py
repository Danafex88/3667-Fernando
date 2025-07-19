# Classe mãe
class Veiculo:
    def __init__(self, modelo, cor):  # Atributos comuns: modelo e cor
        self.modelo = modelo
        self.cor = cor

    def mover(self):
        return f"O veículo {self.modelo} de cor {self.cor} esta se movendo"

# Classe filha


class Carro(Veiculo):
    def __init__(self, modelo, cor, numero_de_portas):  # Adiciona um atributo específico
        super().__init__(modelo, cor)  # Utiliza o contrutor da classe mãe
        self.numero_de_portas = numero_de_portas

    def mover(self):
        return f"O carro {self.modelo} de cor {self.cor} com {self.numero_de_portas} portas esta sendo dirigido"

# Classe filha


class Bicicleta(Veiculo):
    def __init__(self, modelo, cor, tipo_de_guidao):  # Adiciona um atributo específico
        super().__init__(modelo, cor)  # Utiliza o contrutor da classe mãe
        self.tipo_de_guidao = tipo_de_guidao

    def mover(self):
        return f"A bicicleta {self.modelo} de cor {self.cor} com guidão {self.tipo_de_guidao} está disponível."


# Instâncias das classes filhas
carro = Carro("Cruze", "branco perolizado", 4)
bicicleta = Bicicleta("Caloi", "azul", "reto")

# Usando polimorfismo:
# o método mover tem comprtamentos diferentes
print(carro.mover())
print(bicicleta.mover())
