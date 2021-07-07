#Dado um número inteiro positivo n, calcular a soma dos n primeiros números inteiros positivos.
def main():
    print("Calculo da soma dos n primeiros inteiros positivos")
    print()
    
    n = int(input("Informe um número inteiro positivo: "))
    
    contador = 1
    soma = 0
    
    while contador <= n:
        soma = soma + contador
        contador = contador + 1

    print("A soma dos", n, "primeiros inteiros positivos é ", soma)

main()