import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Socket crado com sucesso!!!')

host = 'localhost'
port = 5432

#bind - faz a ligação entre cliente/servidor através do host e da porta
s.bind((host, port))
mensagem = '\nServidor: Olaaaa cliente e ai? Blz?'
#se houver essa ligação, o bind retorna True

while 1: #ou True
    dados, end = s.recvfrom(4096)

    if dados:
        print('Servidor enviando mensagem...')
        s.sendto(dados + (mensagem.encode()), end)