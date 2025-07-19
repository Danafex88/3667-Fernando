class Pessoa:
    # Atributos da classe ~~
    def __init__(self, nome, idade):
        # Atributos especificos para cada instancia
        self.nome = nome  # Atributo que armazena o nome da pessoa
        self.idade = idade  # Atributo que armazena a idade da pessoa
    # Metodos de Classe ~~

    def falar(self):
        # Este método usa atributos da insrtancia para realizar uma ação
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

    def envelhecer(self):
        # Método que altrera o atributo da instancia
        self.idade += 1  # Aumenta a idade em 1 a cada vez que o método é chamado
        print(f"Agora tenho {self.idade} anos. ")


# Criando uma instancia da classe Pessoa
# (atributos personalizados para cada instancia)
pessoa1 = Pessoa("Marino", 30)

# Acessando atributos diretamente
print(pessoa1.nome)
print(pessoa1.idade)

# Chamando métodos (comportamentos)
# Definidos na classe
pessoa1.falar()
pessoa1.envelhecer()
pessoa1.falar()
