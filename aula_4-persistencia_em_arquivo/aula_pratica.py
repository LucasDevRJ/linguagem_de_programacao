arquivo = open('exemplo.txt', 'w+') #w+ cria novo arquivo ou o substitui
arquivo.write('Ola Mundo!\nEsta e a segunda linha\nEsta e a terceira linha')
arquivo.seek(0) #a partir do índice 0
conteudo = arquivo.read()
print(conteudo)

quantidade_caracteres_arquivo = arquivo.tell()
print(quantidade_caracteres_arquivo)

arquivo.close()