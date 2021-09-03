def é_hipotenusa(n):
    
    cateto1 = 0
    cateto2 = 0
    cont1 = 1
    cont2 = 1
    e_hipotenusa = False
    
    while cont1 <= n:
        while cont2 <= n:
            if ((cont1 ** 2) + (cont2 ** 2)) == n ** 2:
                cateto1 = cont1
                cateto2 = cont2
            cont2+=1
        cont1+=1
        cont2 = 1
    
    if cateto1 != 0 and cateto2 !=0:
        e_hipotenusa = True
    
    return e_hipotenusa


def soma_hipotenusas(n):

    contador = 1
    somaHipotenusa = 0

    while contador <= n:
        if é_hipotenusa(contador) == True:
            somaHipotenusa = somaHipotenusa + contador
        contador+=1
    
    return somaHipotenusa

if __name__ == '__main__':
    n = int(input())
    print(soma_hipotenusas(n))

    