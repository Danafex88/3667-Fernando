from decimal import Decimal, getcontext

# Onfiguração da precisão decimal
getcontext().prec = 4

# Função de conversão
def converter_moeda(valor, taxa):
    return valor * Decimal(taxa)

def main():
    print("Bem-vindo à Calculadora de Conversão de Moedas!")

    #Taxas de câmbio
    taxas = {
        "1": Decimal("0.19"),  # Dolar (1/5.25)
        "2": Decimal("0.18"),  # Euro (1/5.63)
        "3": Decimal("27.03"), # Iene Japonês (1/0.037)
        "4": Decimal("0.67"),  # Novo shekel israelense (1/1.48)
        "5": Decimal("4.76"),  # Peso Cubano (1/0.21)  
    }

    valor_real = Decimal(input("Digite o valor em Reais (BRL): "))

    print("\nEscolha a moeda para a qual deseja converter:")
    print("1 - Dolar (USD) ")
    print("2 - Euro (EUR) ")
    print("3 - Iene Japonês (JPY) ")
    print("4 - Novo shekel israelense (ILS) ")
    print("5 - Peso cubano (CUP) ")

    escolha = input("Digite o número da opção desejada: ")

    if escolha in taxas:
        valor_convertido = converter_moeda(valor_real, taxas[escolha])
        print(f"\nO valor de R$ {valor_real:.2f} corresponde a {valor_convertido:.2f} na moeda escolhida.")
    
    else:
        print("Opção invalida. Tente novamente.")

if __name__ == "__main__":
    main()
