from itertools import permutations

lista = ['Ana', 'Beatriz', 'Camila']
for permutacao in permutations(lista, 2):
    print(permutacao)