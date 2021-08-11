import os
import time

with open('hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()#quebra em linhas para poder utilizar no for

    for ip in dump:
        print('Verificando o ip: ', ip)
        print('-' * 40)
        os.system('ping -n 3 {}'.format(ip))
        print('-' * 40)
        time.sleep(6)
