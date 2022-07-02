import os
import pandas as pd
from structure import buscarRanking, buscarRating


arquivoDataFrame = 'files/dataframe.csv'


def buscarDataFrame():
    arquivoExiste = os.path.isfile(arquivoDataFrame)

    if arquivoExiste:
        dataframe = pd.read_csv(arquivoDataFrame)
        return dataframe
    else:
        listaRanking = buscarRanking()
        listaRating = buscarRating()
        gerarDataFrame(listaRanking, listaRating)
        dataframe = pd.read_csv(arquivoDataFrame)
        return dataframe


def gerarDataFrame(listaRanking, listaRating):
    df1 = pd.DataFrame(listaRanking)
    df2 = pd.DataFrame(listaRating)

    df1.to_csv('files/ranking.csv', index=False)
    df2.to_csv('files/rating.csv', index=False)

    dataframe = pd.merge(df1, df2, how='left')
    dataframe.to_csv(arquivoDataFrame, index=False)


def formatarDataFrame(dataframe):
    colunas = ['codigo', 'setor', 'preco', 'liquidez', 'dividend_yield', 'dividend_yield_12', 'P/VPA', 'score', 'tipo']
    dataframe = dataframe[colunas]
    dataframe = pd.get_dummies(dataframe, columns=['tipo'])
    dataframe['preco'] = dataframe['preco'].astype('float64')
    dataframe['dividend_yield'] = dataframe['dividend_yield'].astype('float64')
    dataframe['dividend_yield_12'] = dataframe['dividend_yield_12'].astype('float64')
    dataframe['P/VPA'] = dataframe['P/VPA'].astype('float64')
    return dataframe


def aplicarFiltros(dataframe):
    seloQualidade = dataframe['score'] > 4
    dataframe = dataframe[seloQualidade]

    precoJusto = dataframe['P/VPA'] < 1.20
    dataframe = dataframe[precoJusto]

    liquidezAlta = dataframe['liquidez'] > 5000
    dataframe = dataframe[liquidezAlta]

    dividendYieldAnualBom = dataframe['dividend_yield_12'] > 5
    dataframe = dataframe[dividendYieldAnualBom]

    dataframe = dataframe.sort_values(by=['liquidez'], ascending=False)
    return dataframe


def gravarRelatorios(dataframe):
    caminho = "reports/relatorio_"

    desenvolvimento = dataframe[dataframe['tipo_desenvolvimento'] == 1]
    desenvolvimento.to_csv(caminho + "desenvolvimento.csv", index=False)

    fundos = dataframe[dataframe['tipo_fundos'] == 1]
    fundos.to_csv(caminho + "fundos.csv", index=False)

    papel = dataframe[dataframe['tipo_papel'] == 1]
    papel.to_csv(caminho + "papel.csv", index=False)

    tijolo = dataframe[dataframe['tipo_tijolo'] == 1]
    tijolo.to_csv(caminho + "tijolo.csv", index=False)

    return dataframe
