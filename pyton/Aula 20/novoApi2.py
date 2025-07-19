import requests


def consultar_geolocalizacao(ip=""):
    # Usa o IP público se nenhum IP for informado
    url = f"http://ip-api.com/json/{ip}" if ip else "http://ip-api.com/json/"

    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        if dados['status'] == 'success':
            print(f"IP: {dados.get('query', 'Não disponível')}")
            print(f"País: {dados.get('country', 'Não disponível')}")
            print(f"Cidade: {dados.get('city', 'Não disponível')}")
            print(f"Latitude: {dados.get('lat', 'Não disponível')}")
            print(f"Longitude: {dados.get('lon', 'Não disponível')}")
        else:
            print(
                f"Erro: {dados.get('message', 'Não foi possível obter os dados')}")
    else:
        print(f"Erro ao consultar o IP. Status: {resposta.status_code}")


# Teste com IP específico
consultar_geolocalizacao("8.8.8.8")

# Ou para usar o IP público do cliente:
# consultar_geolocalizacao()
