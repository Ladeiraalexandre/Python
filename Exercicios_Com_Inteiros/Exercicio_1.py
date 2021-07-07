#Dada uma seqüência de números inteiros não-nulos, seguida por 0, imprimir seus quadrados. 


def main():
    
    print("Calculo do quadrado de um sequencia de numero")
    print("O programa termina quando informado o numero 0")
    print()
    n = int(input("Informe um numero inteiro: "))

    while n != 0:
        n = n ** 2
        print(n)
        n = int(input("Informe um numero inteiro: "))

main()