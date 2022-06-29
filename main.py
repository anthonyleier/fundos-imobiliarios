import requests
import bs4
import pandas as pd
from bs4 import BeautifulSoup


def buscarPagina(url):
    html = requests.get(url).text
    pagina = BeautifulSoup(html, 'html.parser')
    return pagina


def buscarTabela(pagina):
    tabela = pagina.find_all('tr')
    tabela = tabela[1:]
    return tabela


def encontrarDado(item):
    if isinstance(item, bs4.element.Tag):
        conteudoTagPrincipal = item.contents
        if conteudoTagPrincipal:
            conteudoTagPrincipal = conteudoTagPrincipal[0]

            if isinstance(conteudoTagPrincipal, bs4.element.Tag):
                conteudoTagSecundaria = conteudoTagPrincipal.contents[0]
                return conteudoTagSecundaria

            else:
                return conteudoTagPrincipal

        else:
            return 'N/A'


def buscarDados(linha):
    listaItens = linha.children
    dados = []

    for item in listaItens:
        dado = encontrarDado(item)
        if dado:
            dados.append(dado)

    return dados


def montarFundo(dados):
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


if __name__ == "__main__":
    url = "https://www.fundsexplorer.com.br/ranking"

    listaFundos = []
    pagina = buscarPagina(url)
    tabela = buscarTabela(pagina)

    for linha in tabela:
        dados = buscarDados(linha)
        fundo = montarFundo(dados)
        listaFundos.append(fundo)

    for (i, fundo) in enumerate(listaFundos):
        print(f"{i} - {fundo['Código']}")
        #  df.to_excel('caminho_do_arquivo.xlsx')
