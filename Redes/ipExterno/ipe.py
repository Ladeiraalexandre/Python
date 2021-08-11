import re
import json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'

#abre a url
resposta = urlopen(url)

#o json vai carregar o jvascript e jogar no dados
dados = json.load(resposta)

#vai pegar do retorno a chave ip do json
ip = dados['ip']
org = dados['org']
cid = dados['city']
pais = dados['country']
regiao = dados['region']

print('Detalhes de seu IP Externo')
#imprimir em posições
print('IP:{4}\nRegiao:{1}\nPais:{2}\nCidade: {3}\nOrganizacao: {0}'.format(org, regiao, pais, cid, ip))