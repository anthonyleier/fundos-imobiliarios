from config import baseINV


def removerTabelaPrincipal():
    query = "DROP TABLE IF EXISTS fundos_imobiliarios;"
    baseINV.executar(query)


def criarTabelaPrincipal():
    query = """
    CREATE TABLE IF NOT EXISTS fundos_imobiliarios (
        id SERIAL PRIMARY KEY,
        codigo VARCHAR(20) NOT NULL,
        setor VARCHAR(50),
        preco FLOAT,
        liquidez FLOAT,
        dividendo FLOAT,
        dividend_yield FLOAT,
        dividend_yield_3 FLOAT,
        dividend_yield_6 FLOAT,
        dividend_yield_12 FLOAT,
        dividend_yield_media_3 FLOAT,
        dividend_yield_media_6 FLOAT,
        dividend_yield_media_12 FLOAT,
        dividend_yield_ano FLOAT,
        variacao FLOAT,
        rentabilidade_periodo FLOAT,
        rentabilidade_acumulada FLOAT,
        patrimonio_liquido FLOAT,
        VPA FLOAT,
        PVPA FLOAT,
        dividend_yield_patrimonial FLOAT,
        variacao_patrimonial FLOAT,
        rentabilidade_patrimonial_periodo FLOAT,
        rentabilidade_patrimonial_acumulada FLOAT,
        vacancia_fisica FLOAT,
        vacancia_financeira FLOAT,
        quantidade_ativos INT,
        score FLOAT,
        tipo VARCHAR(50),
        price FLOAT);
    """
    baseINV.executar(query)


def criarTabelaRanking():
    query = """
    CREATE TEMPORARY TABLE fundos_ranking (
        codigo VARCHAR(20) NOT NULL,
        setor VARCHAR(50),
        preco FLOAT,
        liquidez FLOAT,
        dividendo FLOAT,
        dividend_yield FLOAT,
        dividend_yield_3 FLOAT,
        dividend_yield_6 FLOAT,
        dividend_yield_12 FLOAT,
        dividend_yield_media_3 FLOAT,
        dividend_yield_media_6 FLOAT,
        dividend_yield_media_12 FLOAT,
        dividend_yield_ano FLOAT,
        variacao FLOAT,
        rentabilidade_periodo FLOAT,
        rentabilidade_acumulada FLOAT,
        patrimonio_liquido FLOAT,
        VPA FLOAT,
        PVPA FLOAT,
        dividend_yield_patrimonial FLOAT,
        variacao_patrimonial FLOAT,
        rentabilidade_patrimonial_periodo FLOAT,
        rentabilidade_patrimonial_acumulada FLOAT,
        vacancia_fisica FLOAT,
        vacancia_financeira FLOAT,
        quantidade_ativos INT);
    """
    baseINV.executar(query)


def criarTabelaRating():
    query = """
    CREATE TEMPORARY TABLE fundos_rating (
        codigo VARCHAR(20) NOT NULL,
        score FLOAT,
        tipo VARCHAR(50));
    """
    baseINV.executar(query)


def criarTabelas():
    removerTabelaPrincipal()
    criarTabelaPrincipal()
    criarTabelaRanking()
    criarTabelaRating()


def unirTabelas():
    query = """
    INSERT INTO fundos_imobiliarios
        SELECT
            nextval('fundos_imobiliarios_id_seq'), fundos_ranking.*,
            fundos_rating.score, fundos_rating.tipo FROM fundos_ranking
        LEFT JOIN fundos_rating
            ON fundos_rating.codigo = fundos_ranking.codigo;
    """
    baseINV.executar(query)
