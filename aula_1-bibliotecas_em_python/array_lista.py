import numpy as np

#código feito com lista
numero_elementos = 10000000
lista_elementos = []

for x in range(numero_elementos):
    lista_elementos.append(x)

print(lista_elementos[-1])

#código feito com Numpy
array_elementos = np.arange(numero_elementos)
print(array_elementos[-1])

#a diferença entre ambos é que o Numpy utiliza menos processamento de dados e memória