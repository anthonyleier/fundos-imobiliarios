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
    return dataframe[colunas]


def aplicarFiltros(dataframe):
    # Nota maior que 4
    seloQualidade = dataframe['score'] > 4
    dataframe = dataframe[seloQualidade]

    # Ordernar por liquidez
    dataframe = dataframe.sort_values(by=['liquidez'], ascending=False)
    dataframe.to_csv('files/relatorio.csv', index=False)
    return dataframe
