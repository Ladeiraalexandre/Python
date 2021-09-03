def n_primo(k):
    
    n_primo = 0
    contador = 2
    
    while contador <= k:
        if ehPrimo(contador) == True:
            n_primo = n_primo+1     
        contador+=1
    
    return n_primo


def ehPrimo(n):
    
    contador = 1
    divisor = 0 

    while contador <= n:
        if((n % contador) == 0): 
            divisor += 1
        contador+=1

    #se tiver mais de dois divisores não é primo, pois numeros primos sã divisiveis por 1 e por ele mesmo
    if divisor > 2:
        return False
    else:
        return True    


n = int(input()) 
print(n_primo(n))
