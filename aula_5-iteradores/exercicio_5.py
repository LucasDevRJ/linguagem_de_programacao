from itertools import permutations

lista = ['Ana', 'Beatriz', 'Camila']
for permutacao in permutations(lista, 3):
    print(permutacao)