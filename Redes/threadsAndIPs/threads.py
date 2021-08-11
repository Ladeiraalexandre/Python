# da biblioteca threading importe o modulo Thread
import time
from threading import Thread

def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:#distancia definida aleatoriamente
        trajeto+= velocidade
        time.sleep(0.5)#aguardar para imprimir de um carro para outro
        print('Piloto: {} km: {} \n'.format(piloto, trajeto))



#cria um objeto e na função thread vc passa o nome do metodo e o o argumento(parametro).
#neste caso o metodo é o carro1 e o argumento é a velocidade, que esta sendo passado como 1
t_carro1 = Thread(target=carro, args=[1, 'Lucas'])
t_carro2 = Thread(target=carro, args=[1.5, 'Daniel'])

#iniciando o processo
t_carro1.start()
t_carro2.start()
