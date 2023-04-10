# fundos-imobiliarios

Este projeto é uma ferramenta de coleta e análise de dados de fundos imobiliários (FIIs) no Brasil. Suas principais funcionalidades são:

- Buscar informações sobre FIIs no [FundsExplorer](https://www.fundsexplorer.com.br/)
- Extrair e formatar informações relevantes sobre os FIIs encontrados (como código, setor, preço, rentabilidade, etc.)
- Armazenar as informações extraídas em um banco de dados PostgreSQL
- Gerar rankings e ratings de FIIs com base nas informações coletadas e armazenadas

Este projeto pode ser útil para investidores em FIIs que desejam tomar decisões de investimento com base em dados atualizados e precisos sobre o mercado.

# Web Scraping

Scraping é a técnica de extrair dados de um website de forma automatizada, utilizando um programa de computador que envia requisições HTTP para o website, processa o HTML resultante e extrai as informações relevantes. Neste projeto, o scraping é realizado por meio da biblioteca BeautifulSoup em conjunto com a biblioteca requests. O processo de scraping é executado em diversas funções que recebem uma URL ou um arquivo HTML como entrada e retornam uma lista de objetos contendo informações de fundos imobiliários.

![FundsExplorer](https://i.imgur.com/8mNN2qu.png)

Nesse caso, o site utilizado é o [FundsExplorer](https://www.fundsexplorer.com.br/). O FundsExplorer é um site brasileiro que disponibiliza informações sobre fundos de investimentos, permitindo aos usuários realizar pesquisas e comparar diversos fundos. Ele é uma ferramenta útil para quem deseja investir em fundos de investimentos, pois apresenta dados e informações relevantes sobre o desempenho dos fundos, as taxas cobradas pelos gestores, os ativos em que os fundos investem, entre outros.

No site, é possível fazer buscas por nome ou código do fundo, tipo de fundo, categoria e gestor. Além disso, o FundsExplorer oferece uma seção de análise, com gráficos e tabelas que ajudam a entender o desempenho histórico dos fundos e a comparar diferentes opções.
