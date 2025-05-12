import pandas as pd

# Lendo o arquivo CSV
dados = pd.read_csv('dados.csv', sep=';', engine='python', encoding='utf-8')

# Exibindo os dados
print(dados)