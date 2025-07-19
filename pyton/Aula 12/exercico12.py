import matplotlib.pyplot as plt

vendedores = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace"]
vendas = [1200, 1800, 1600, 1900, 2100, 1400, 1750]

#Combinar vendededores com cendas em uma lista de tuplas
vendedores_vendas = list(zip(vendedores, vendas))

#ordenar os vendedores com base nas vendas (do maior para o menor)
vendedores_vendas.sort(key=lambda x: x[1], reverse=True)

#Selecionar os 4 elementos
melhores_vendedores = [v[0] for v in vendedores_vendas[:4]]
melhores_vendas = [v[1] for v in vendedores_vendas[:4]]

#Criando o grafico pizza
plt.pie(melhores_vendas, labels=melhores_vendedores, autopct='%1.1f%%', startangle= 360)
plt.title("Top 4 Vendedores")
plt.show()
