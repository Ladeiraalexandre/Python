n = int(input('Digite um número inteiro: '))

metade = n / 2; #Nenhum número possui qualquer divisor maior que metade do seu valor.
contador = 2 #quaquer numero é divisível por 1, sendo assim vamos iniciar o contador, que vai ser o dividor, em 2  
nprimo = 0
    

while contador <= metade:
    if((n % contador) == 0): 
        nprimo+=1
        break
    
    contador+=1

if (nprimo > 0) or (n == 1) or (n == 0):
    print('não primo')
else:
    print('primo')

