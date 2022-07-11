from config import baseINV
from formatar import formatarLinha, formatarFundoRanking, formatarFundoRating
from scraping import buscarPagina, buscarTabela, abrirArquivoHTML, buscarItensFII


def gerarRanking():
    fundos = buscarPaginaRanking()

    for fundo in fundos:
        query = """
        INSERT INTO fundos_ranking (
            codigo, setor, preco, liquidez, dividendo, dividend_yield, dividend_yield_3, dividend_yield_6,
            dividend_yield_12, dividend_yield_media_3, dividend_yield_media_6, dividend_yield_media_12,
            dividend_yield_ano, variacao, rentabilidade_periodo, rentabilidade_acumulada, patrimonio_liquido,
            VPA, PVPA, dividend_yield_patrimonial, variacao_patrimonial, rentabilidade_patrimonial_periodo,
            rentabilidade_patrimonial_acumulada, vacancia_fisica, vacancia_financeira, quantidade_ativos)
        VALUES (
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        info = list(fundo.values())
        baseINV.executar(query, info)


def gerarRating():
    fundos = buscarPaginaRating()

    for fundo in fundos:
        query = "INSERT INTO fundos_rating (codigo, score, tipo) VALUES (%s, %s, %s);"
        info = list(fundo.values())
        baseINV.executar(query, info)


def buscarPaginaRanking():
    url = "https://www.fundsexplorer.com.br/ranking"

    listaFundos = []
    pagina = buscarPagina(url)
    tabela = buscarTabela(pagina)

    for linha in tabela:
        linha = formatarLinha(linha)
        fundo = formatarFundoRanking(linha)
        listaFundos.append(fundo)

    return listaFundos


def buscarPaginaRating():
    listaFundos = []
    pagina = abrirArquivoHTML('data/rating.html')
    tabela = buscarItensFII(pagina)

    for linha in tabela:
        fundo = formatarFundoRating(linha)
        listaFundos.append(fundo)

    return listaFundos
