from tools import montarFundo
from analysis import gerarDataFrame
from scraping import buscarPagina, buscarTabela


if __name__ == "__main__":
    url = "https://www.fundsexplorer.com.br/ranking"

    listaFundos = []
    pagina = buscarPagina(url)
    tabela = buscarTabela(pagina)

    for linha in tabela:
        fundo = montarFundo(linha)
        listaFundos.append(fundo)

    gerarDataFrame(listaFundos)
