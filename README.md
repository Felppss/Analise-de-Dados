# Missão Prática - RPG0033
Tratando a Imensida o dos Dados

1- Introdução
Este documento descreve o passo a passo da execuça o da missa o pra tica da disciplina RPG0033,
seguindo todas as orientaço es do roteiro fornecido. O objetivo foi realizar o tratamento de dados
em um arquivo CSV utilizando Python e a biblioteca Pandas, preparando o conjunto de dados
para futuras ana lises e mineraça o de conhecimento.

2- Etapas Realizadas

1. 1. Leitura do arquivo 'dados.csv' com separador ';', utilizando a engine 'python' e encoding
'utf-8'.
2. 2. Exibiça o das informaço es gerais do conjunto de dados (info), primeiras e u ltimas linhas
(head, tail).
3. 3. Criaça o de uma co pia do DataFrame original para tratamento.
4. 4. Substituiça o de valores nulos da coluna 'Calories' por 0.
5. 5. Substituiça o de valores nulos na coluna 'Date' por '1900/01/01'.
6. 6. Tentativa de conversa o da coluna 'Date' para datetime (gera erro esperado).
7. 7. Substituiça o de '1900/01/01' por valor nulo (NaT).
8. 8. Nova tentativa de conversa o para datetime (erro ainda ocorre por conta do valor
20201226).
9. 9. Correça o do valor 20201226 na coluna 'Date' para '2020/12/26'.
10. 10. Conversa o completa da coluna 'Date' para datetime, com tratamento de erros.
11. 11. Remoça o de todas as linhas com valores nulos (incluindo a linha 22).
12. 12. Exibiça o final dos dados tratados (DataFrame e info).
13. 13. Exportaça o do DataFrame final para 'dados_tratados.csv'.

3- Conclusão
Com a execuça o das etapas descritas acima, foi possí vel realizar com sucesso a limpeza e o
preparo do conjunto de dados, garantindo que ele esteja pronto para aplicaço es futuras de
ana lise ou mineraça o de dados. O processo utilizou pra ticas comuns em cie ncia de dados e
demonstrou domí nio da biblioteca Pandas.
