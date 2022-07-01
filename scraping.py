import requests
import bs4
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
