print('-' * 60)
print('Porgama que calcula a potência do número informado')
print('-' * 60)
x = int(input('Informe a base: '))
n = int(input('Informe o expoente >= 0: '))
print('-' * 60)
potencia = x ** n

indice = 0
x_indice = x ** indice

while indice < n:
    indice += 1
    x_indice *= x

print('-' * 60)
print(f'O numero {x} elevado a potencia {n} é {potencia}.')
print('-' * 60)
print('Calculo pelo segundo método')
print()
print(f'O numero {x} elevado a potencia {n} é {potencia}.')