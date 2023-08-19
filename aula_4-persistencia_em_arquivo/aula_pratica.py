import pandas as pd
from pyspark.sql import SparkSession

arquivo = open('exemplo.txt', 'w+') #w+ cria novo arquivo ou o substitui
arquivo.write('Ola Mundo!\nEsta e a segunda linha\nEsta e a terceira linha\n')
arquivo.seek(0) #a partir do índice 0
conteudo = arquivo.read()
print(conteudo)

quantidade_caracteres_arquivo = arquivo.tell()
print(quantidade_caracteres_arquivo)

arquivo.close()

with open('exemplo.txt', 'a+') as arquivo:
    arquivo.write('Quarta linha é feita com uso de gerenciamento de contexto\n'+\
                  'Esta e a quinta linha e foi feita da mesma forma\n')

    arquivo.seek(0)
    conteudo = arquivo.read()
    print(conteudo)
