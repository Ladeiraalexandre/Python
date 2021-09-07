def remove_repetidos(lista):
    lista2 = []

    for i in lista:
        if i not in lista2:
            lista2.append(i)

    lista2.sort()

    return lista2


'''
if __name__ == '__main__':
    lista = [int(s) for s in input('Lista de numeros: ').split(',')]
    print(remove_repetidos(lista))
'''
    
        

