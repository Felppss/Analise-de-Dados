# Informações gerais
print(dados.info())

# Total de linhas e colunas
print(f"Total de linhas: {len(dados)}")
print(f"Total de colunas: {len(dados.columns)}")

# Dados nulos
print(dados.isnull().sum())

# Uso de memória
print(dados.memory_usage())