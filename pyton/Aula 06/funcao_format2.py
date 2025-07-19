produtos = ["PC Gamer", "Xbox Series", "PlayStation 5", "Nitendo Switch", "Notebook Gamer"]
valores = [8000, 3000, 4500, 2500, 6000]

# Percorrendo duas listas ao mesmo tempo

#zip()
for produto, valor in zip(produtos, valores):
    print("O Valor de {} é R${}".format(produto, valor))

#range()
#for i in range(len(produtos)):
#   print("O Valor de {} é R${}".format(produtos[i], valores[i]))

#enumerate()
#for i, produto in enumerate(produtos):
#    print("O valor de {} é R$ {}".format(produto, valores[i]))
