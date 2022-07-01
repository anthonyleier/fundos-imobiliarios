import pandas as pd


def gerarDataFrame(lista):
    df = pd.DataFrame(lista)

    with pd.ExcelWriter("fundos.xlsx") as writer:
        df.to_excel(writer)
