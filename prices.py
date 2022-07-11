import time
import requests
from config import baseINV


def formatarLista(lista):
    texto = str(lista)
    texto = texto.replace("[", "").replace("]", "")
    texto = texto.replace("'", "").replace(",", "%2C")
    texto = texto.replace(" ", "")
    return texto


def buscarPrices(fundos):
    try:
        url = f"https://brapi.dev/api/quote/{fundos}"
        json = requests.get(url).json()
        prices = json['results']
        return prices

    except:
        print(f"Não foi possível encontrar informações na API")


def atualizarPrice(codigo, price):
    if price:
        query = "UPDATE fundos_imobiliarios SET price = %s WHERE codigo = %s;"
        parametros = [price, codigo]
        baseINV.executar(query, parametros)
        print(f"{codigo} -> {price}")


def gerarPrices():
    query = "SELECT codigo FROM fundos_imobiliarios;"
    fundos = baseINV.selecionar(query)

    fundos = [fundo['codigo'] for fundo in fundos]
    fundos = formatarLista(fundos)

    dados = buscarPrices(fundos)

    for dado in dados:
        codigo = dado.get('symbol')
        price = dado.get('regularMarketPrice')
        atualizarPrice(codigo, price)


if __name__ == "__main__":
    inicio = time.time()
    gerarPrices()
    fim = time.time()

    tempoDecorrido = fim - inicio
    print(f"Execução realizada em {tempoDecorrido}")
