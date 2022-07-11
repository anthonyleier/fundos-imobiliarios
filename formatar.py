from scraping import buscarConteudoTag


def formatarValor(valor):
    valor = valor.replace("R$", "")
    valor = valor.replace("%", "")
    valor = valor.replace(".", "").replace(",", ".")
    valor = float(valor) if valor != 'N/A' else None
    return valor


def formatarLinha(linha):
    listaTags = linha.children
    dados = []

    for tag in listaTags:
        if tag != '\n':
            dado = buscarConteudoTag(tag)
            dados.append(dado)

    return dados


def formatarFundoRanking(linha):
    ranking = {}
    ranking['codigo'] = linha[0]
    ranking['setor'] = linha[1]
    ranking['preco'] = formatarValor(linha[2])
    ranking['liquidez'] = formatarValor(linha[3])
    ranking['dividendo'] = formatarValor(linha[4])
    ranking['dividend_yield'] = formatarValor(linha[5])
    ranking['dividend_yield_3'] = formatarValor(linha[6])
    ranking['dividend_yield_6'] = formatarValor(linha[7])
    ranking['dividend_yield_12'] = formatarValor(linha[8])
    ranking['dividend_yield_media_3'] = formatarValor(linha[9])
    ranking['dividend_yield_media_6'] = formatarValor(linha[10])
    ranking['dividend_yield_media_12'] = formatarValor(linha[11])
    ranking['dividend_yield_ano'] = formatarValor(linha[12])
    ranking['variacao'] = formatarValor(linha[13])
    ranking['rentabilidade_periodo'] = formatarValor(linha[14])
    ranking['rentabilidade_acumulada'] = formatarValor(linha[15])
    ranking['patrimonio_liquido'] = formatarValor(linha[16])
    ranking['VPA'] = formatarValor(linha[17])
    ranking['P/VPA'] = formatarValor(linha[18])
    ranking['dividend_yield_patrimonial'] = formatarValor(linha[19])
    ranking['variacao_patrimonial'] = formatarValor(linha[20])
    ranking['rentabilidade_patrimonial_periodo'] = formatarValor(linha[21])
    ranking['rentabilidade_patrimonial_acumulada'] = formatarValor(linha[22])
    ranking['vacancia_fisica'] = formatarValor(linha[23])
    ranking['vacancia_financeira'] = formatarValor(linha[24])
    ranking['quantidade_ativos'] = int(linha[25])
    return ranking


def formatarFundoRating(linha):
    rating = {}
    rating['codigo'] = linha['data-symbol']
    rating['score'] = formatarValor(linha['data-score'])
    rating['tipo'] = linha['data-type'].replace("fundo de ", "")
    return rating
