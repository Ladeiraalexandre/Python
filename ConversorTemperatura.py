def main():
    saida = input("Deseja realizar a conversão de temperatura de Fahrenheit para Celsius? S - Sim; N - Não :")
    while saida.upper() == 'S':
        temperaturaF = input("Digite uma temperatura em Fahrenheit : ")
        temperaturaC = (float(temperaturaF) - 32) * 5 / 9

        print("A temperatura em Celcius é:", temperaturaC)
        saida = input("Deseja continuar o programa? S - Sim; N - Não : ")
    print("Obrigado por utilizar nosso programa. Até mais!!!")
main()