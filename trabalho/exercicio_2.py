#importando bibliotecas
import random
import pandas as pd
import plotly.express as px

#armazenando valores
print("Digite os três primeiros números do seu RU: ")
a = int(input())
b = int(input())
c = int(input())

#trocando valores de 0 para 5
if a == 0:
    a = 5
elif b == 0:
    b = 5
elif c == 0:
    c = 5

#gerando números aleátorios
coordenada_x = [random.randint(0, 10) for _ in range(10)]
#equação da coordenada Y
coordenada_y = [a * x + b * x - c for x in coordenada_x]

#gerando gráfico
data = pd.DataFrame({'x': coordenada_x, 'y': coordenada_y})
fig = px.scatter(data_frame=data, x='x', y='y', title='Coordenadas X e Y do plano cartesiano',
                 labels={"x": "X", "y": "Y"})
#exibindo gráfico
fig.show()