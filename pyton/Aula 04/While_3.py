# Este código solicita ao usuario uma resposta e continua executando
# enquanto a resposta for "sim"
resposta = input("Deseja continuar? (digite 'sim' para continuar):  ")

# A função lower()transforma toda string em letras minusculas
while resposta.lower() == "sim":
    resposta = input("Deseja continuar? (digite 'sim' para continuar):  ")
