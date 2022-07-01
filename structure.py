from scraping import formatarDados
from scraping import buscarPagina, buscarTabela, buscarItensFII, abrirArquivoHTML


def montarRanking(linha):
    dados = formatarDados(linha)
    ranking = {}
    ranking['codigo'] = dados[0]
    ranking['setor'] = dados[1]
    ranking['preco'] = dados[2]
    ranking['liquidez'] = dados[3]
    ranking['dividendo'] = dados[4]
    ranking['dividend_yield'] = dados[5]
    ranking['dividend_yield_3'] = dados[6]
    ranking['dividend_yield_6'] = dados[7]
    ranking['dividend_yield_12'] = dados[8]
    ranking['dividend_yield_media_3'] = dados[9]
    ranking['dividend_yield_media_6'] = dados[10]
    ranking['dividend_yield_media_12'] = dados[11]
    ranking['dividend_yield_ano'] = dados[12]
    ranking['variacao'] = dados[13]
    ranking['rentabilidade_periodo'] = dados[14]
    ranking['rentabilidade_acumulada'] = dados[15]
    ranking['patrimonio_liquido'] = dados[16]
    ranking['VPA'] = dados[17]
    ranking['P/VPA'] = dados[18]
    ranking['dividend_yield_patrimonial'] = dados[19]
    ranking['variacao_patrimonial'] = dados[20]
    ranking['rentabilidade_patrimonial_periodo'] = dados[21]
    ranking['rentabilidade_patrimonial_acumulada'] = dados[22]
    ranking['vacancia_fisica'] = dados[23]
    ranking['vacancia_financeira'] = dados[24]
    ranking['quantidade_ativos'] = dados[25]
    return ranking


def montarRating(linha):
    rating = {}
    rating['codigo'] = linha['data-symbol']
    rating['score'] = linha['data-score']
    rating['tipo'] = linha['data-type']
    return rating


def buscarRanking():
    url = "https://www.fundsexplorer.com.br/ranking"

    listaFundos = []
    pagina = buscarPagina(url)
    tabela = buscarTabela(pagina)

    for linha in tabela:
        fundo = montarRanking(linha)
        listaFundos.append(fundo)

    return listaFundos


def buscarRating():
    listaFundos = []
    pagina = abrirArquivoHTML('rating.html')
    tabela = buscarItensFII(pagina)

    for linha in tabela:
        fundo = montarRating(linha)
        listaFundos.append(fundo)

    return listaFundos
