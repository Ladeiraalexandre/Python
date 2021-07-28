n = int(input('Digite o valor de n: '))

contador = 1
fatorial = 1 
anterior = 1 

if n != 0:
    while contador <= n:
        anterior =  fatorial * contador
        fatorial = anterior
        contador+=1
    print(fatorial)
else:
    print(1)



