import numpy as np
import pandas as pd

df = pd.read_csv(r'Stores.csv')
df = df.rename(columns={'Store ID': 'Identificador', 'Store_Area': 'Área', 'Items_Available': 'Disponiveis',
                   'Daily_Customer_Count': 'Clientes', 'Store_Sales': 'Vendas'})

disponiveis = df['Disponiveis'].tolist()

print(f'Coluna Disponiveis')
print(f'Valor Minímo = {min(disponiveis)}')
print(f'Valor Médio = {sum(disponiveis) / len(disponiveis)}')
print(f'Valor Máximo = {max(disponiveis)}')
print(f'Desvio Padrão = {np.std(disponiveis)}')
print('\n')

clientes = df['Clientes'].tolist()

print(f'Coluna Clientes')
print(f'Valor Minímo = {min(clientes)}')
print(f'Valor Médio = {sum(clientes) / len(clientes)}')
print(f'Valor Máximo = {max(clientes)}')
print(f'Desvio Padrão = {np.std(clientes)}')
print('\n')

vendas = df['Vendas'].tolist()

print(f'Coluna Vendas')
print(f'Valor Minímo = {min(vendas)}')
print(f'Valor Médio = {sum(vendas) / len(vendas)}')
print(f'Valor Máximo = {max(vendas)}')
print(f'Desvio Padrão = {np.std(vendas)}')