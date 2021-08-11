import hashlib

arquivo1 = 'a.txt'
arquivo2 = 'b.txt'

hash1 = hashlib.new('ripemd160') #no construtor do modulo haslib, vc passa o tipo  de hash que vc quer, Sha1m MD5, ripemd160 entre outros...

#no objeto hash1, como a comparação esta em um arquivo, fazemos o update, depois damos um open no arquivo e fazemos a leitura
hash1.update(open(arquivo1, 'rb').read()) #r=read e b=binary(abertura(open) em modo binario

hash2 = hashlib.new('ripemd160')

hash2.update(open(arquivo2, 'rb').read())

#digest = resume os dados passado pelo metodo update
if hash1.digest() != hash2.digest():
    print(f'O arquivo: {arquivo1} é diferente do arquivo: {arquivo2}.')
    print('O hash do arquivo a.txt é: ', hash1.hexdigest())
    print('O hash do arquivo b.txt é: ', hash2.hexdigest())
else:
    print(f'O arquivo: {arquivo1} é igual ao arquivo: {arquivo2}.')
    print('O hash do arquivo a.txt é: ', hash1.hexdigest())
    print('O hash do arquivo b.txt é: ', hash2.hexdigest())
