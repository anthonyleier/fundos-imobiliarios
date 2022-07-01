from analysis import gerarDataFrame
from tools import montarFundo, montarAvaliacao
from scraping import buscarPagina, buscarTabela, buscarItensFII, abrirArquivoHTML


def buscarRanking():
    url = "https://www.fundsexplorer.com.br/ranking"

    listaFundos = []
    pagina = buscarPagina(url)
    tabela = buscarTabela(pagina)

    for linha in tabela:
        fundo = montarFundo(linha)
        listaFundos.append(fundo)
        break

    df = gerarDataFrame(listaFundos)
    return df


def buscarAvaliacao():
    listaAvaliacoes = []
    pagina = abrirArquivoHTML('avaliacao.html')
    tabela = buscarItensFII(pagina)

    for linha in tabela:
        avaliacao = montarAvaliacao(linha)
        listaAvaliacoes.append(avaliacao)

    df = gerarDataFrame(listaAvaliacoes)
    return df


if __name__ == "__main__":
    # df1 = buscarRanking()
    df2 = buscarAvaliacao()
    print(df2)
