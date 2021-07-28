n = int(input('Digite um número inteiro: '))

anterior = n % 10
n = n // 10
vizinho_igual = False

while n > 0 and not vizinho_igual:
    atual = n % 10
    if atual == anterior:
        vizinho_igual = True
        
    anterior = atual
    n = n // 10

if vizinho_igual:
    print('sim')
else:
    print('não')


