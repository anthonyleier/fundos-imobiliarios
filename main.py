from analysis import buscarDataFrame, formatarDataFrame, aplicarFiltros, gravarRelatorios

if __name__ == "__main__":
    dataframe = buscarDataFrame()
    dataframe = formatarDataFrame(dataframe)
    dataframe = aplicarFiltros(dataframe)
    dataframe = gravarRelatorios(dataframe)
    print(dataframe)
