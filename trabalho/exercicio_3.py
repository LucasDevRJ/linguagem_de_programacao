import numpy as np
import pandas as pd

df = pd.read_csv(r'Stores.csv')
df = df.rename(columns={'Store ID': 'Identificador', 'Store_Area': 'Área', 'Items_Available': 'Disponiveis',
                   'Daily_Customer_Count': 'Clientes', 'Store_Sales': 'Vendas'})

disponiveis = df['Disponiveis'].tolist()
print(disponiveis)

print(f'Valor Minímo = {min(disponiveis)}')
print(f'Valor Médio = {sum(disponiveis) / len(disponiveis)}')
print(f'Valor Máximo = {max(disponiveis)}')
print(f'Desvio Padrão = {np.std(disponiveis)}')