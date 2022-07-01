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


def verificarTag(item):
    return isinstance(item, bs4.element.Tag)


def buscarConteudoTag(item):
    if verificarTag(item):
        conteudoTag = item.contents

        if conteudoTag:
            texto = conteudoTag[0]

            if verificarTag(texto):
                return buscarConteudoTag(texto)
            else:
                return texto

        else:
            return 'N/A'


def formatarDados(linha):
    listaTags = linha.children
    dados = []

    for tag in listaTags:
        if tag != '\n':
            dado = buscarConteudoTag(tag)
            dados.append(dado)

    return dados
