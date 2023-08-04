#importando bibliotecas
import numpy as np
import pandas as pd
import plotly.express as px

#lendo o arquivo
df = pd.read_csv(r'Stores.csv')
df = df.rename(columns={'Store ID': 'Identificador', 'Store_Area': 'Área', 'Items_Available': 'Disponiveis',
                   'Daily_Customer_Count': 'Clientes', 'Store_Sales': 'Vendas'})

#armazenando dados da categoria Disponiveis
disponiveis = df['Disponiveis'].tolist()

#exibindo dados com seus calculos
print(f'Coluna Disponiveis')
print(f'Valor Minímo = {min(disponiveis)}')
print(f'Valor Médio = {sum(disponiveis) / len(disponiveis)}')
print(f'Valor Máximo = {max(disponiveis)}')
print(f'Desvio Padrão = {np.std(disponiveis)}')
print('\n')

#armazenando dados da categoria Clientes
clientes = df['Clientes'].tolist()

#exibindo dados com seus calculos
print(f'Coluna Clientes')
print(f'Valor Minímo = {min(clientes)}')
print(f'Valor Médio = {sum(clientes) / len(clientes)}')
print(f'Valor Máximo = {max(clientes)}')
print(f'Desvio Padrão = {np.std(clientes)}')
print('\n')

#armazenando dados da categoria Clientes
vendas = df['Vendas'].tolist()

#exibindo dados com seus calculos
print(f'Coluna Vendas')
print(f'Valor Minímo = {min(vendas)}')
print(f'Valor Médio = {sum(vendas) / len(vendas)}')
print(f'Valor Máximo = {max(vendas)}')
print(f'Desvio Padrão = {np.std(vendas)}')

#construindo e exibindo gráfico da categoria Disponiveis
data = pd.DataFrame({'x': disponiveis, 'y': disponiveis})
fig = px.scatter(data_frame=data, x='x', y='y', title='Coordenadas X e Y do plano cartesiano',
                 labels={"x": "X", "y": "Y"})
fig.show()

#construindo e exibindo gráfico da categoria Clientes
data = pd.DataFrame({'x': clientes, 'y': clientes})
fig = px.scatter(data_frame=data, x='x', y='y', title='Coordenadas X e Y do plano cartesiano',
                 labels={"x": "X", "y": "Y"})
fig.show()

#construindo e exibindo gráfico da categoria Vendas
data = pd.DataFrame({'x': vendas, 'y': vendas})
fig = px.scatter(data_frame=data, x='x', y='y', title='Coordenadas X e Y do plano cartesiano',
                 labels={"x": "X", "y": "Y"})
fig.show()