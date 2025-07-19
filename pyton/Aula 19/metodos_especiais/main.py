from produto import Produto
from carrinho import Carrinho

# Cria alguns produtos para adicionar ao carrinho
# Instância de produto com nome e preço
produto1 = Produto("Camiseta", 29.90)
produto2 = Produto("Calça", 59.90)
produto3 = Produto("Boné", 19.90)

# Cria um carrinho de compras vazio
carrinho = Carrinho()

# Adciona os produtos aos carrinhos
carrinho.adicionar_produto(produto1)
carrinho.adicionar_produto(produto2)

# Exibe a quantidade de itens no carrinho usando o método espercial __len__
print(f"Total de itens no carrinho: {len(carrinho)}")

# Exibe a descrição do carrinho com os produtos
# usando o método especial __str__
print(carrinho)

# Verifica se um produto especifico esta no carrinho
# usando o método especial __contains___
print(produto1 in carrinho)
print(produto3 in carrinho)
