import itertools


string = input('String a ser permutada: ')
#metodo permutations faz a permutação das palavras, dos caracteres
# e quantas permutações ele fara ou seja dara conjuntos de 3(combinrara as letras no tamanho de 3).
# Qunto maior a string e maior o numero, maior ficara as combinações
#resultado = itertools.permutations('abc', 3)

#pegando dinamicamente
resultado = itertools.permutations(string, len(string))

for i in resultado:
    print(''.join(i))