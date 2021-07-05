numero = int(input("Digite um número inteiro: "))

milhar = numero % 1000
centena = milhar % 100
dezena = centena // 10

print("O dígito das dezenas é", dezena)
