import pandas as pd

precos_notas = pd.DataFrame([[5.29, 5.5], [6.49, 7.0], [7.49, 7.5], [7.99, 8.5],
               [8.49, 9.5], [9.99, 9.0], [11.99, 9.5]], columns=['Preço', 'Nota'])

print(precos_notas)

precos_notas['DataColeta'] = pd.date_range(start='2022-01-01', freq='M', periods=len(precos_notas))

print(precos_notas)

precos_notas['Ano'] = precos_notas['DataColeta'].dt.year
precos_notas['Dia'] = precos_notas['DataColeta'].dt.day
precos_notas['DiaSemana'] = precos_notas['DataColeta'].dt.weekday
precos_notas['Proporcao'] = precos_notas['Preço']/precos_notas['Nota']

precos_notas.describe()

precos_notas.corr(method='spearman')

print(precos_notas)