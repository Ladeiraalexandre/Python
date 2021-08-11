import ipaddress

#com a biblioteca ipaddress, conseguimos trasnformar uma string(ip) em ip para poder fazer calculos
ip = '192.168.0.2'
endereco = ipaddress.ip_address(ip)
print(endereco + 257)#calculando o numero de ips(lembrando que cada soma de 255, ele o muda de campo.


#verficando rede
ip_rede = '192.168.0.0/24'
rede = ipaddress.ip_network(ip_rede, strict=False)#modo scrict para desabilitar validações de rede, como por exemplo endereços

#mostrar a possibilidade de endereço de rede
for ip_rede in rede:
    print(rede)