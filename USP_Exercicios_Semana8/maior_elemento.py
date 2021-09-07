def maior_elemento(lista):
    
    
    maiorValor = max(lista)


    ''' Outra forma de fazer, sem utilizar a função max
    for i in lista:
        if(maiorValor == None or i > maiorValor):
            maiorValor = i
    '''
    return maiorValor

'''
if __name__ == '__main__':
    lista = [int(s) for s in input('Informe a lista de numeros: ').split(',')]
    print(maior_elemento(lista))
'''