import re

# texto que usaremos na busca
texto_busca = '3 placas devem ser selecionadas: UNI0100, NTE-0a00 eRRR9876. A JJ2070 é inválida.'

print(texto_busca)

# regex a ser usado
texto_regex = '[A-Za-z]{3}\-?\d[A-Ja-j\d]\d{2}'

print(texto_regex)

# procurando
resultados = re.findall(texto_regex, texto_busca)

print(resultados)