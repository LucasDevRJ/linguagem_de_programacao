import pandas as pd

df = pd.read_csv('combustivel.csv', sep=';', encoding='ISO-8859-1')
dados = df.head()
print(dados)
valores_colunas = df.columns.values
print(valores_colunas)
df_colunas = ['Regiao - Sigla', 'Estado - Sigla', 'Produto']
df_filtrado = df.filter(items=df_colunas)
df_filtrado = df.rename(columns={'Regiao - Sigla': 'Região', 'Estado - Sigla': 'Estado'})
print(df_filtrado)

colunas_estados = df_filtrado['Estado']
print(colunas_estados)