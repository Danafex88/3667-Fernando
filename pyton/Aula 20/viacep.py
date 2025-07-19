import requests


def consultar_cep(cep):
    # Remove qualquer caractere nao numérico do CEP
    cep = ''.join(filter(str.isdigit, cep))

    # URL da API ViaCep
    url = f"https://viacep.com.br/ws/{cep}/json/"
    # Faz a requisição GET para a API
    resposta = requests.get(url)

    # Verifica se a resposta foi bem sucedida
    if resposta.status_code == 200:
        dados = resposta.json()

        # Verifica se o CEP existe
        if "erro" not in dados:
            print(f"CEP:{dados['cep']}")
            print(f"Logradouro:{dados['logradouro']}")
            print(f"Bairro:{dados['bairro']}")
            print(f"Cidade:{dados['localidade']}")
            print(f"Estado:{dados['uf']}")
        else:
            print("CEP não encontrado.")
    else:
        print("Erro na consulta da API.")


# Solicita o CEP ao usuário
cep_usuario = input("Digite o CEP (somente números): ")
consultar_cep(cep_usuario)
