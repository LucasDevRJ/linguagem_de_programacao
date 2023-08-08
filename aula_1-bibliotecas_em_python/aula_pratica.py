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

#criar vetor com numpy
array_normal = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
array_de_um = np.ones([10])
array_de_zero = np.zeros([12])
array_de_vazio = np.empty([15])
array_de_ate = np.arange(23)
array_de_limite = np.linspace(0, 5, 6)

print(f'criação de array numpy utilizando o método .array: {array_normal}')
#eles exibem ponto depois do número porque são de ponto flutuante
print(f'criação de array numpy utilizando o método .ones: {array_de_um}')
print(f'criação de array numpy utilizando o método .zeros: {array_de_zero}')
print(f'criação de array numpy utilizando o método .empty: {array_de_vazio}')
print(f'criação de array numpy utilizando o método .arange: {array_de_ate}')
print(f'criação de array numpy utilizando o método .linspace: {array_de_limite}')