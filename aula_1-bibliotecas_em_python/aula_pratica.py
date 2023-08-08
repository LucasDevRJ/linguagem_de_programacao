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

#consumindo no máximo até 8 bits armazenados no array
array_perfomance = np.zeros(numeros_elementos, dtype= np.int8)
print(f'{array_perfomance}')

#gerando números randomicos
rng = np.random.default_rng()
print(rng.random(10))

rng = np.random.default_rng()
vetor = rng.random(4)
print(f'Array de uma dimensão randômico: {vetor}')

matriz = rng.random([4,4])
print(f'Array de duas dimensões randômicas: {matriz}')

tensor = rng.random([4,4,4])
print(f'Array de três ou mais dimensões randômicas: {tensor}')

rng = np.random.default_rng()
array_sem_ordenacao = rng.random([2,3])
print(f'Array sem ordenação: {array_sem_ordenacao}')

arra_com_ordenacao = np.sort(array_sem_ordenacao, axis= None)
print(f'Array com ordenação: {arra_com_ordenacao}')

#concatenação
array2 = rng.random([2,2])
array3 = rng.random([2,2])
array_concatenado = np.concatenate([array2, array3])
print(array_concatenado)

#propriedades do array
rng = np.random.default_rng()
array_teste4 = rng.random([23, 43,17])
print(f'Quais são duas dimensões: {array_teste4.ndim}')
print(f'Qual é o seu formato: {array_teste4.shape}')
print(f'Quantos elementos possui: {array_teste4.size}')

