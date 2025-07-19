class Pessoa:
    #Lista para armazenar as pessoas
    lista_pessoas = []

    def __init__(self, nome, idade, naturalidade):
        self.nome = nome
        self.idade = nome
        self.naturalidade = naturalidade

    def detalhes(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Estado em que nasceu: {self.naturalidade}"
    
    @classmethod
    def adicionar(cls, pessoa):
        cls.lista_pessoas.append(pessoa)

    @classmethod
    def exibir_pessoas(cls):
        for pessoa in cls.lista_pessoas:
            print(pessoa.detalhes())

#crinado isntancia de pessoas
pessoa1 = Pessoa("Marcos Vinicius", 30, "SP")
pessoa2 = Pessoa("Emmanuel", 25, "PR")

#Adicionando as intancias a lista usando o metodo da classe
Pessoa.adicionar(pessoa1)
Pessoa.adicionar(pessoa2)

#Exibindo todas as pessoas cadastradas usando o metodo
Pessoa.exibir_pessoas()
