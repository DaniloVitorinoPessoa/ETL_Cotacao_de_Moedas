import requests

url_api = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL"

def extract_cotacoes():
    chamada_api = requests.get(url_api)
    dados_json = chamada_api.json()
    return dados_json