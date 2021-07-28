n = int(input('Digite um número inteiro: '))

soma = 0
inteiro = 0

while n !=0:
    inteiro = n % 10
    soma+= inteiro
    n = n // 10
print(soma)
