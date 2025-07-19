class Produto:
    def __init__(self, nome, preco):
        """
        Inicializa um novo produto com o nome e um preço.
        """
        self.nome = nome  # Atribui o nome do produto
        self.preco = preco  # Atribui o preço do produto

    def __str__(self):
        """
        Mensagem padrão que é exibida quando usado
        print(produto)
        """
        return f"{self.nome} - R${self.preco:.2f}"

    def __repr__(self):
        """
        Retorna uma representação do objeto Produto para debugging.
        """
        return f"Produto(nome='{self.nome}', preco={self.preco})"

    def __eq__(self, outro):
        """
        Compra dois produtos para ver se são iguais.
        Parâmetros:
            outro (Produto): Outro objeto Produto para comprar.

        Retorna:
            bool: True se os produtos tem o mesmo nome e preço, False caso contrário.
        """
        return self.nome == outro.nome and self.preco == outro.preco
