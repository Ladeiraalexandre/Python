def main():
    saida = input("Deseja realizar a conversão de segundos? S - Sim; N - Não: ")
    while saida.upper() == 'S':
        segundos_str = input("Informe o numero de segundos que deseja converter: ")
        total_segs = int(segundos_str)

        dias = (total_segs // 3600) // 24
        horas = (total_segs // 3600) % 24
        segs_restantes = total_segs % 3600
        minutos = segs_restantes // 60
        segs_restantes_final = segs_restantes % 60

        print("O resultado é ", dias, "dia(s), ", horas, "hora(s), ", minutos, "minuto(s) e", segs_restantes_final, "segundo(s)")
        saida = input("Deseja continuar o programa? S - Sim; N - Não : ")
    print("Obrigado por utilizar nosso programa. Até mais!!!")
main()