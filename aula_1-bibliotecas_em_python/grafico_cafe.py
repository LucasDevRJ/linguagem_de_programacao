import plotly.express as px

preco = [5.29, 6.49, 7.49, 7.99, 8.49, 9.99, 11.99]
nota = [5.5, 7.0, 7.5, 8.5, 9.5, 9.0, 9.5]

fig = px.scatter(x = preco, y = nota, title = "Comparação entre preço e nota de cafés", labels={"x":"preco", "y": "Nota"})
fig.show()