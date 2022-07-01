from scraping import buscarPagina, buscarTabela, buscarDados
from tools import montarFundo
from analysis import gerarDataFrame


if __name__ == "__main__":
    url = "https://www.fundsexplorer.com.br/ranking"

    listaFundos = []
    pagina = buscarPagina(url)
    tabela = buscarTabela(pagina)

    for linha in tabela:
        dados = buscarDados(linha)
        fundo = montarFundo(dados)
        listaFundos.append(fundo)

    gerarDataFrame(listaFundos)
