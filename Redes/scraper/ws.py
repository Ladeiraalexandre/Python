#importando a biblioteca bs4
from bs4 import BeautifulSoup

import requests

#objeto site recebendo conteudo da requisição http do site...
site = requests.get('https://www.climatempo.com.br').content #pegar todo conteudo do site

#objeto soup esta baixando do site o html, transformando a requisição
soup = BeautifulSoup(site, 'html.parser')

#prettify transforma toda estrutura em html em string
print(soup.prettify())

#para pegar um conteudo especifico, devemos passar a tag(neste caso a span) e a classe
temperatura = soup.find("span", class_="_blo _margin-b-5 -gray")
#com o find vc pode procurar informações relevantes a respeito de senha e outras coisas
#exemplo:
#print(soup.find('admin'))

#print(temperatura.string)

print(soup.title.string)