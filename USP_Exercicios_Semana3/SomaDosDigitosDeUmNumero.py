#Programa que realiza a soma dos digitos de um numero inteiro
print('Programa que realiza a soma dos digitos de um numero inteiro')
numeroInteiro = int(input('Informe um numero inteiro: '))

somadigitos = 0

while numeroInteiro > 0:
    ultimoDigito = numeroInteiro % 10 #o resto da divisão por 10 é sempre o ultimo digito de um número
    somadigitos+= ultimoDigito
    numeroInteiro = numeroInteiro // 10 #pego a parte inteira da divisao por 10 para ir fracionando o numero de 10 em 10 até zerar

print('A soma dos digitos do numero informado é:', somadigitos) 