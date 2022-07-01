import os
import pandas as pd
from structure import buscarRanking, buscarRating


arquivoDataFrame = 'dataframe.csv'


def buscarDataFrame():
    arquivoExiste = os.path.isfile(arquivoDataFrame)

    if arquivoExiste:
        dataframe = pd.read_csv(arquivoDataFrame)
        return dataframe
    else:
        listaRanking = buscarRanking()
        listaRating = buscarRating()
        dataframe = gerarDataFrame(listaRanking, listaRating)
        return dataframe


def gerarDataFrame(listaRanking, listaRating):
    df1 = pd.DataFrame(listaRanking)
    df2 = pd.DataFrame(listaRating)

    with pd.ExcelWriter('ranking.xlsx') as writer:
        df1.to_excel(writer)

    with pd.ExcelWriter('rating.xlsx') as writer:
        df2.to_excel(writer)

    dataframe = pd.merge(df1, df2, how='left')
    dataframe.to_csv(arquivoDataFrame)
    return dataframe
