import random
import plotly.express as px

print("Digite os três primeiros números do seu RU: ")
a = int(input())
b = int(input())
c = int(input())

if a == 0:
    a = 5
elif b == 0:
    b = 5
elif c == 0:
    c = 5

x = [13, 34, 11, 19, 45, 67, 43, 22, 98, 56]
y = [81, 43, 22, 29, 56, 77, 34, 21, 76, 44]

fig = px.scatter(x=x, y=y,
                 title='Coordenadas X e Y do plano cartesiano',
                 labels={"x": "X", "y": "Y"})
fig.show()