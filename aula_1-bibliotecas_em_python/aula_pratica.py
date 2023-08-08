import numpy as np

#lista normal
numeros_elementos = 100000000
lista_elementos = []
for x in range(numeros_elementos):
    lista_elementos.append(x)

print(lista_elementos[-1])

#lista com numpy
#mais rápida
#menos consumo de hardware
array_elementos = np.arange(numeros_elementos)
print(array_elementos[-1])