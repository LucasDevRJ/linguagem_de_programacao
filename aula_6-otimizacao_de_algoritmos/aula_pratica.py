import time
import pandas as pd
import seaborn as sns

#tempo constante
#realizar comparação com outros tipos de funções
def take_first(my_list):
    return my_list[0]

#é uma lista restrita com apenas três elementos
sort_list = [5, 15, 20]
tic = time.perf_counter()  #inciando a contagem do tempo computacional
comando = take_first(sort_list)
toc = time.perf_counter()

print(comando)

tempo_computacional = toc - tic
print(f'Tempo Computacional = {tempo_computacional}')

#reformulando a lista - tamanho
long_list = [15] * 10**8
len_lista = len(long_list)
print(f'Tamanho da lista = {len_lista}')