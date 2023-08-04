import pandas as pd

df = pd.read_csv(r'Stores.csv')
df = df.rename(columns={'Store ID': 'Identificador', 'Store_Area': 'Área', 'Items_Available': 'Disponiveis',
                   'Daily_Customer_Count': 'Clientes', 'Store_Sales': 'Vendas'})

disponiveis = df['Disponiveis'].tolist()
print(disponiveis)

print(f'Valor Minímo = {min(disponiveis)}')