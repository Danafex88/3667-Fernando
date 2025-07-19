import requests


def consultar_geolocalizacao(ip=""):
    # Se o IP não for informado, usará o IP público
    url = f"import requests"


def consultar_geolocalizacao(ip=""):
    # Se o IP não for informado, usará o IP público
    url = f"https://ipapi.co/{ip}/json/"
    # Fazendo a requisição GET
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        print(f"IP: {dados['ip']}")
        print(f"País: {dados['country_name']}")
        print(f"Cidade: {dados.get('city', 'Não disponível')}")
        print(f"Latitude: {dados.get('latitude', 'Não disponível')}")
        print(f"Longitude: {dados.get('longitude', 'Não disponível')}")
    else:
        print(f"Erro ao consultar o IP. Status: {resposta.status_code}")


consultar_geolocalizacao("192.168.100.242")


# Usa o IP público
# Ou, se você quiser consultar um IP específico:
# consultar_geolocalizacao("8.8.8.8")/"
# Fazendo a requisição GET
