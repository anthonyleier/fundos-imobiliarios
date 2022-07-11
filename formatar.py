from scraping import buscarConteudoTag


def formatarTexto(texto):
    texto = str(texto)
    texto = texto.lower()
    texto = texto.replace("fundo de ", "")
    texto = 'títulos' if texto == 'títulos e val. mob.' else texto
    texto = texto.title()
    texto = None if texto.upper() == 'N/A' else texto
    return texto


def formatarValor(valor):
    valor = valor.replace("R$", "")
    valor = valor.replace("%", "")
    valor = valor.replace(".", "") if ',' in valor else valor
    valor = valor.replace(",", ".")
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
    fundo = {}
    fundo['codigo'] = linha[0]
    fundo['setor'] = formatarTexto(linha[1])
    fundo['preco'] = formatarValor(linha[2])
    fundo['liquidez'] = formatarValor(linha[3])
    fundo['dividendo'] = formatarValor(linha[4])
    fundo['dividend_yield'] = formatarValor(linha[5])
    fundo['dividend_yield_3'] = formatarValor(linha[6])
    fundo['dividend_yield_6'] = formatarValor(linha[7])
    fundo['dividend_yield_12'] = formatarValor(linha[8])
    fundo['dividend_yield_media_3'] = formatarValor(linha[9])
    fundo['dividend_yield_media_6'] = formatarValor(linha[10])
    fundo['dividend_yield_media_12'] = formatarValor(linha[11])
    fundo['dividend_yield_ano'] = formatarValor(linha[12])
    fundo['variacao'] = formatarValor(linha[13])
    fundo['rentabilidade_periodo'] = formatarValor(linha[14])
    fundo['rentabilidade_acumulada'] = formatarValor(linha[15])
    fundo['patrimonio_liquido'] = formatarValor(linha[16])
    fundo['VPA'] = formatarValor(linha[17])
    fundo['P/VPA'] = formatarValor(linha[18])
    fundo['dividend_yield_patrimonial'] = formatarValor(linha[19])
    fundo['variacao_patrimonial'] = formatarValor(linha[20])
    fundo['rentabilidade_patrimonial_periodo'] = formatarValor(linha[21])
    fundo['rentabilidade_patrimonial_acumulada'] = formatarValor(linha[22])
    fundo['vacancia_fisica'] = formatarValor(linha[23])
    fundo['vacancia_financeira'] = formatarValor(linha[24])
    fundo['quantidade_ativos'] = formatarValor(linha[25])
    return fundo


def formatarFundoRating(linha):
    fundo = {}
    fundo['codigo'] = linha['data-symbol']
    fundo['score'] = formatarValor(linha['data-score'])
    fundo['tipo'] = formatarTexto(linha['data-type'])
    return fundo
