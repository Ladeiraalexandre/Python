def main():
    n = int(input())

    contador = 1
    notaMaxima = 0
    notaMinima = 0

    while contador <= n:
    
        notas = int(input('Informe a %da. nota: ' %contador))
        if (notas > notaMaxima):
            notaMaxima = notas
            if contador == 1:
                notaMinima = notas
        else:
            notaMinima = notas    
      
        contador+=1

    print('A maior nota foi %d e a menor nota foi %d' %(notaMaxima, notaMinima)) 



main()
