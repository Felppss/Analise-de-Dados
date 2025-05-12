import pandas as pd

def main():
    # 1. Ler o arquivo CSV
    print("1. Lendo o arquivo CSV...")
    dados = pd.read_csv('dados.csv', sep=';', engine='python', encoding='utf-8')
    
    # 2. Verificar a importação
    print("\n2. Verificando dados importados:")
    print("Informações gerais:")
    print(dados.info())
    print("\nPrimeiras 5 linhas:")
    print(dados.head())
    print("\nÚltimas 5 linhas:")
    print(dados.tail())
    
    # 3. Criar cópia do dataframe
    print("\n3. Criando cópia dos dados para tratamento...")
    dados_tratados = dados.copy()
    
    # 4. Substituir valores nulos na coluna Calories por 0
    print("\n4. Substituindo valores nulos em 'Calories' por 0...")
    dados_tratados['Calories'].fillna(0, inplace=True)
    print("Valores nulos após substituição:")
    print(dados_tratados.isnull().sum())
    
    # 5. Substituir valores nulos na coluna Date por '1900/01/01'
    print("\n5. Substituindo valores nulos em 'Date' por '1900/01/01'...")
    dados_tratados['Date'].fillna('1900/01/01', inplace=True)
    print("Valores nulos após substituição:")
    print(dados_tratados.isnull().sum())
    
    # 6. Tentativa de converter para datetime (irá falhar)
    print("\n6. Tentando converter 'Date' para datetime...")
    try:
        dados_tratados['Date'] = pd.to_datetime(dados_tratados['Date'], format='%Y/%m/%d')
    except ValueError as e:
        print(f"Erro encontrado: {e}")
    
    # 7. Corrigir o valor '1900/01/01' para NaN
    print("\n7. Corrigindo valor '1900/01/01' para NaN...")
    dados_tratados['Date'] = dados_tratados['Date'].replace('1900/01/01', pd.NaT)
    
    # 8. Tentar novamente a conversão (ainda irá falhar)
    print("\n8. Tentando converter novamente para datetime...")
    try:
        dados_tratados['Date'] = pd.to_datetime(dados_tratados['Date'], format='%Y/%m/%d')
    except ValueError as e:
        print(f"Novo erro encontrado: {e}")
    
    # 9. Corrigir o valor "20201226"
    print("\n9. Corrigindo formato da data '20201226'...")
    dados_tratados['Date'] = dados_tratados['Date'].replace('20201226', '2020/12/26')
    
    # 10. Converter toda a coluna para datetime
    print("\n10. Convertendo 'Date' para datetime com tratamento de erros...")
    dados_tratados['Date'] = pd.to_datetime(dados_tratados['Date'], format='%Y/%m/%d', errors='coerce')
    
    # 11. Remover registros com valores nulos
    print("\n11. Removendo registros com valores nulos...")
    dados_tratados = dados_tratados.dropna()
    
    # 12. Verificar o resultado final
    print("\n12. Resultado final:")
    print("\nDataFrame tratado:")
    print(dados_tratados)
    print("\nInformações finais:")
    print(dados_tratados.info())
    
    # 13. Salvar dados tratados
    print("\n13. Salvando dados tratados em 'dados_tratados.csv'...")
    dados_tratados.to_csv('dados_tratados.csv', index=False, sep=';')
    print("Processo concluído com sucesso!")

if __name__ == "__main__":
    main()