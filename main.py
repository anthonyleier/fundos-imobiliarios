from config import baseINV
from estrutura import criarTabelas, unirTabelas
from buscadores import gerarRanking, gerarRating, gerarPrices

if __name__ == "__main__":
    criarTabelas()
    gerarRanking()
    gerarRating()
    unirTabelas()
    gerarPrices()
    baseINV.fecharConexao()
