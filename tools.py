from scraping import formatarDados


def montarFundo(linha):
    dados = formatarDados(linha)
    fundo = {}
    fundo['Código'] = dados[0]
    fundo['Setor'] = dados[1]
    fundo['Preço Atual'] = dados[2]
    fundo['Liquidez Diária'] = dados[3]
    fundo['Dividendo'] = dados[4]
    fundo['Dividend Yield'] = dados[5]
    fundo['DY (3M) Acumulado'] = dados[6]
    fundo['DY (6M) Acumulado'] = dados[7]
    fundo['DY (12M) Acumulado'] = dados[8]
    fundo['DY (3M) Média'] = dados[9]
    fundo['DY (6M) Média'] = dados[10]
    fundo['DY (12M) Média'] = dados[11]
    fundo['DY Ano'] = dados[12]
    fundo['Variação Preço'] = dados[13]
    fundo['Rentab. Período'] = dados[14]
    fundo['Rentab. Acumulada'] = dados[15]
    fundo['Patrimônio Líq.'] = dados[16]
    fundo['VPA'] = dados[17]
    fundo['P/VPA'] = dados[18]
    fundo['DY Patrimonial'] = dados[19]
    fundo['Variação Patrimonial'] = dados[20]
    fundo['Rentab. Patr. no Período'] = dados[21]
    fundo['Rentab. Patr. Acumulada'] = dados[22]
    fundo['Vacância Física'] = dados[23]
    fundo['Vacância Financeira'] = dados[24]
    fundo['Quantidade Ativos'] = dados[25]
    return fundo


def montarAvaliacao(linha):
    avaliacao = {}
    avaliacao['codigo'] = linha['data-symbol']
    avaliacao['score'] = linha['data-score']
    avaliacao['tipo'] = linha['data-type']
    return avaliacao
