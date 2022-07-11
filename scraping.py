import requests
import bs4
from bs4 import BeautifulSoup


def abrirArquivoHTML(caminho):
    with open(caminho, 'r', encoding='UTF-8') as arquivo:
        pagina = BeautifulSoup(arquivo, 'html.parser')
    return pagina


def buscarPagina(url):
    html = requests.get(url).text
    pagina = BeautifulSoup(html, 'html.parser')
    return pagina


def buscarTabela(pagina):
    tabela = pagina.find_all('tr')
    tabela = tabela[1:]
    return tabela


def buscarItensFII(pagina):
    tijolo = pagina.find_all("div", {"class": "fii-item", "data-type": "fundo de tijolo"})
    papel = pagina.find_all("div", {"class": "fii-item", "data-type": "fundo de papel"})
    fundos = pagina.find_all("div", {"class": "fii-item", "data-type": "fundo de fundos"})
    desenvolvimento = pagina.find_all("div", {"class": "fii-item", "data-type": "fundo de desenvolvimento"})
    itensFII = tijolo + papel + fundos + desenvolvimento
    return itensFII


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
