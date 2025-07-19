import requests


def consultar_geolocalização(ip=""):
    # Se o IP nao for informado, usaro o IP publico
    url = f"https://ipapi.co/{ip}/json/"
    # fazendo a requisição GET
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        print(f"IP: {dados['ip']}")
        print(f"País: {dados['contry_name']}")
        print(f"Cidade: {dados.get('city', 'Não Disponível')}")
        print(f"Latitude: {dados.get('latitude', 'Não Disponível')}")
        print(f"Longitude: {dados.get('longitude', 'Não Disponível')}")
    else:
        print(f" Erro ao consultar o IP. Status: {resposta.status_code}")


consultar_geolocalização()
