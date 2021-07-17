#Programa que retorna quantidade de numeros pares e impares de uma sequencia de numeros passada
n = int(input('Informe o tamanho da sequencia: '))

while n <= 0:
    n = int(input('Informe o tamanho da sequência (maior que 0): '))

par = 0
impar = 0
i = 1

while i <= n:
    seq = int(input(f'Informe o {i} º numero da sequência: '))
    if seq % 2 == 0:
        par+=1
    i+=1
        
print(par, 'numero(s) par(es)')
print(n - par, 'numero(s) impar(res)')