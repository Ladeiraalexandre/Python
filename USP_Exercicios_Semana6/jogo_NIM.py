def calcula_jogada(n, m):

    pc_retirar = 0

    for i in range(1, m + 1):
        if (n - i) % (m + 1) == 0:
            pc_retirar = i
    return pc_retirar

def computador_escolhe_jogada(n, m):
    if n < m:
        print(f"O computador tirou{n} peças. ")
        print(f"Agora restam {n - n} peças no tabuleiro.\n")
        prox_jogada = n

    elif calcula_jogada(n, m) != 0:
        prox_jogada = calcula_jogada(n, m)
        print(f"O computador tirou {prox_jogada} peças. ")
        print(f"Agora restam {n - prox_jogada} peças no tabuleiro.\n")

    else:
        print(f"O computador tirou {m} peças. ")
        print(f"Agora restam {n - m} peças no tabuleiro.\n")
        prox_jogada = m 

    return prox_jogada


def usuario_escolhe_jogada(n, m):
    jogada = int(input("Informe sua jogada: "))

    while jogada <= 0 or jogada > n or jogada > m:
        print(f"Valor incorreto. O valor deve estar entre 1 e {n}, ou ser menor que a quantidade de peças disponíveis {m}")
        jogada = int(input("Informe sua jogada: "))   
    
    print(f"\nVocê tirou {jogada} peças.")
    print(f"Agora resta {n - jogada} peças no tabuleiro.")
    return jogada

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    
    vencedor = 2 # variável de controle para quem venceu. 1 para cpu, 0 para usuário.
    
    peças_restantes = n
    
    if n % (m + 1) == 0: # caso que o computador deixa o usuário começar
        print("Você começa!\n")
        proxima_jogada = 0
        
        while peças_restantes > 0:
            # jogada usuaŕio
            peças_retiradas = usuario_escolhe_jogada(peças_restantes, m)
            peças_restantes = peças_restantes - peças_retiradas

            if peças_restantes == 0:
                vencedor = 0
                break
            # jogada computador
            peças_retiradas = computador_escolhe_jogada(peças_restantes, m)
            peças_restantes = peças_restantes - peças_retiradas

            if peças_restantes == 0:
                vencedor = 1
                break
                
    else:  # caso que o computador começa a partida
        print("Computador começa!\n")
        while peças_restantes > 0:

            # jogada computador
            peças_retiradas = computador_escolhe_jogada(peças_restantes, m)
            peças_restantes = peças_restantes - peças_retiradas

            if peças_restantes == 0:
                vencedor = 1
                break

            # jogada usuaŕio
            peças_retiradas = usuario_escolhe_jogada(peças_restantes, m)
            peças_restantes = peças_restantes - peças_retiradas

            if peças_restantes == 0:
                vencedor = 0
                break
    
    if vencedor == 1:
        print("Fim de jogo! O computador ganhou!\n")
        return 1
    elif vencedor == 0:
        print("Fim de jogo! Você ganhou!\n")
        return 0


def campeonato():
    
    rodada = 1
    
    partidas_ganhas_cpu = 0
    partidas_ganhas_usuario = 0
    
    while rodada <= 3:
        print("**** Rodada %d ****" % rodada)
        vencedor = partida()
        if vencedor == 1:
            partidas_ganhas_cpu += 1
        elif vencedor == 0:
            partidas_ganhas_usuario += 1
        rodada += 1
    
    print("**** Final do campeonato! ****\n")
    print("Placar: Você %d x %d Computador" % (partidas_ganhas_usuario, partidas_ganhas_cpu))





def main():
    
    print("Bem-vindo ao jogo do NIM! Escolha:\n")
    
    escolha = int(input("1 - para jogar uma partida isolada\n2 - para jogar um campeonato"))
    
    if escolha == 1:
        print("Você escolheu uma partida isolada!")
        partida()
    elif escolha == 2:
        print("Você escolheu um campeonato!")
        campeonato()


if __name__ == '__main__':
    main()
    
