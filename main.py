from analysis import buscarDataFrame, formatarDataFrame, aplicarFiltros

if __name__ == "__main__":
    dataframe = buscarDataFrame()
    dataframe = formatarDataFrame(dataframe)
    dataframe = aplicarFiltros(dataframe)
    print(dataframe)
