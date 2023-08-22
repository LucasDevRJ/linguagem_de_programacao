import time
import pandas as pd
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
