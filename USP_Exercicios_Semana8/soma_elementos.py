def soma_elementos(lista):
    
    soma = 0

    for i in range(len(lista)):
        soma = soma + lista[i]
        

    return soma

'''
if __name__ == '__main__':
    lista = [int(s) for s in input('Informe a lista de numeros: ').split(',')]
    print(soma_elementos(lista))
''' 