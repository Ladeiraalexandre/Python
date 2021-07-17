#Dado um número inteiro n, n > 0, e um dígito d (0 <= d <= 9), determinar quantas vezes d ocorre em n. 

n = int(input('Informe um número inteiro (maior que 0): '))
d = int(input('Informe um digito (maior/igual a 0 ou menor/igual a 9): '))

contador = 0
numero = n
while n > 0:
    digito = n % 10
    n = n // 10
    if digito == d:
        contador += 1

print(f'O digito {d} ocorre {contador} vezes no número {numero}')
