from config import baseINV
from estrutura import criarTabelas, unirTabelas
from funcoes import gerarRanking, gerarRating

if __name__ == "__main__":
    criarTabelas()
    gerarRanking()
    gerarRating()
    unirTabelas()
    baseINV.fecharConexao()
