import os

venda = 0
dia = 1
diaSalvo = 1

while dia <= 30:
    n = int(input(f"Informe a venda do {dia} dia: "))

        
    if venda < n:
        venda = n
        diaSalvo = dia
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    dia+=1

print(f"A maior venda foi no dia {diaSalvo} com o total de : {venda} discos vendidos") 