import socket #chama api do SO para comunicar com a placa de rede
import sys

def main():
    #tenta criar o socket para depois fazer a conexão
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) #codigo do protcolo TCP = 0
    except socket.error as ex:
        print('A conexão falhou: {}'.format(ex))
        sys.exit()

    print('Socket criado com sucesso')

    hostAlvo = input('Informe o host ou IP a ser conectado')
    portaAlvo = input('Informe a porta para conexão: ')

    #fazendo a conexão
    try:
        s.connect((hostAlvo, int(portaAlvo)))
        print(f'Cliente TCP conectado com Sucesso  no host: {hostAlvo} e porta {portaAlvo}')
        s.shutdown(2)
    except socket.error as ex:
        print('Conexão falhou: {}'.format(ex))
        sys.exit()

if __name__ == '__main__':
    main()






