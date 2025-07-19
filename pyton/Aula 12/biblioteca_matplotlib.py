import matplotlib.pyplot as plt

class Vendedor:
    def __init__(self, nome, total_vendas):
        self.nome = nome
        self.total_vendas = total_vendas

vendedores = [
    Vendedor("Pietro", 1500.00),
    Vendedor("Valentina", 2000.00),
    Vendedor("Davi", 1200.00),
    Vendedor("Miguel", 1800.00),
    Vendedor("Enzo", 2100.00)
]

#Extraindo nomes totais de vendas para o grafico
nomes = [v.nome for v in vendedores]
vendas_totais = [v.total_vendas for v in vendedores]

#Criando o grafico de barras 
plt.figure(figsize=(10, 5))
plt.bar(nomes, vendas_totais, color= 'blue')
plt.title("Total de vendas por Vendedor")
plt.xlabel("vendedores")
plt.ylabel("Total de Vendas (R$)")
plt.grid(axis='y')

#Exibindo o grafico
plt.show()

        