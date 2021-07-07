#Programe que lê um inteiro positivo n e imprime os n 
#primeiros inteiros positivos.
#Exemplo de execução:
#Informe um numero inteiro: 3
#saida:
#1
#3
#5

def main():
    print("Gerador do n primeiros números ímpares positivos\n")
    n = int(input("Informe um numero inteiro: "))
    impar = 1
    contador = 0
    while contador < n:
        print(impar)
        contador = contador + 1
        impar += 2    
main()
