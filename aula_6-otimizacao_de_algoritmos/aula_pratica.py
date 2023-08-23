import time

import geneticalgorithm
import pandas as pd
import pip
import seaborn as sns


# tempo constante
# realizar comparação com outros tipos de funções
def take_first(my_list):
    return my_list[0]


# é uma lista restrita com apenas três elementos
sort_list = [5, 15, 20]
tic = time.perf_counter()  # inciando a contagem do tempo computacional
comando = take_first(sort_list)
toc = time.perf_counter()

print(comando)

tempo_computacional = toc - tic
print(f'Tempo Computacional = {tempo_computacional}')

# reformulando a lista - tamanho
long_list = [15] * 10 ** 8
len_lista = len(long_list)
print(f'Tamanho da lista = {len_lista}')

tic = time.perf_counter()
comando2 = take_first(long_list)
toc = time.perf_counter()
tempo_computacional = toc - tic
print(f'Primeiro elemento = {comando2}')
print(f'Tempo Computacional = {tempo_computacional}')

lista_tamanho = [10 ** l for l in range(1, 5)]
print(lista_tamanho)

constante_tempo = []
for l in lista_tamanho:
    lista = [15] * l

tic = time.perf_counter()
y = take_first(lista)
toc = time.perf_counter()

constante_tempo.append(toc - tic)
print(constante_tempo)

# utlizando dataframe para vizualisação organizada
constante_df = pd.DataFrame(list(zip(lista_tamanho, constante_tempo)), columns=['N', 'tempo'])
print(constante_df)

_=sns.lmplot(x='N', y='tempo', data=constante_df, ci=None)

#tempo linear
#encontrando o valor máximo da lista
def find_max(m_lista):
    max_valor = m_lista[0]
    for i in range(len(m_lista)):
        if m_lista[i] > max_valor:
            max_valor = m_lista[i]
            return max_valor

tic = time.perf_counter()
maior = find_max(sort_list)
toc = time.perf_counter()
print(maior)
diferenca = tic - toc
print(diferenca)

#modificando a lista
linear_tempo = []
for l in lista_tamanho:
    lista = [16] * l

tic = time.perf_counter()
comando3 = find_max(lista)
toc = time.perf_counter()

linear_tempo.append(toc - tic)

#realizando o DataFrame
linear_df = pd.DataFrame(list(zip(lista_tamanho, linear_tempo)), columns=['N', 'tempo'])
print(linear_df)

_s = sns.lmplot(x='N', y='tempo', data=linear_df, ci=None)

#otimização com python
import numpy as np
import math
from geneticalgorithm import geneticalgorithm as ga

def f(x):
    dim = len(x)
    OF = 0
    for i in range(0, dim):
        OF += (x[i]**2)-10*math.cos(2*math.pi*x[i])+10
        return OF

varbound = np.array([[-50, 80]])
algoritmo = ga(function=f, dimension=1, variable_type='real', variable_boundaries=varbound)
algoritmo.run()