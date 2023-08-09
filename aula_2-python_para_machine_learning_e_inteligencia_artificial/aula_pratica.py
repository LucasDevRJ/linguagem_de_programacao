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

coluna_estado = df_filtrado['Estado']
estado_conta = coluna_estado.value_counts()
print(estado_conta)

estados = [100 * sigla / estado_conta.sum() for sigla in estado_conta]
print(estados)

df_colunas2 = ['Estado', 'Produto', 'Valor de Venda']
df_gasolina = df_filtrado.filter(items=df_colunas2)
print(df_gasolina)
df_gasolina = df_gasolina.loc[df_gasolina['Produto'] == 'Gasolina']
print(df_gasolina)