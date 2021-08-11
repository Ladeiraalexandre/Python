def maior_primo(k):
    
    maior = 1
    contador = 0
    
    while contador <= k:
        if éPrimo(contador) == True:
            maior = contador     
        contador+=1
    
    return maior


def éPrimo(n):

    contador = 2
    divisor = 0 

    while contador <= n:
        if((n % contador) == 0): 
            divisor += 1
        contador+=1

    if divisor >= 2:
        return False
    else:
        return True    


n = int(input()) 
print(maior_primo(n))

