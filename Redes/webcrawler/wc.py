#retorna as plavras chaves com maior ocorrencia no site informado e n final um resumo das palavras
#e sua quantidade
import requests #requisições http
from bs4 import BeautifulSoup #para trabalhar com xlm, html
import operator #para trabalhar com operdores + = - and or
from collections import Counter #ajuda a manipular listas tuplas

#função que define o webcrowlrr
def start(url):
    wordlist = [] #nicia uma lista vazia e o conteudo do site que vamos passar vai para ela
    source_code = requests.get(url).text

    soup = BeautifulSoup(source_code, 'html.parser') #transforma em html


    #tudo que achar no html com div e classe transforma em string
    for each_text in soup.findAll('div', {'class': 'entry-content'}):
        content = each_text.text

        words = content.lower().split() #aqui passa tudo para letra minuscula, e corta deixando cada conteudo em uma linha

        for each_word in words:
            wordlist.append(each_word)
        clean_wordlist(wordlist)

def clean_wordlist(wordlist): #remove qualquer simbolo indesejado conforme o que esta em symbols, fazendo replace
    clean_list = []
    for word in wordlist:
        symbols = '!@#$%^&*()_-+{[}]|\;;"<>?/,. '

        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], '')

        if len(word) > 0:
            clean_list.append(word) #adciona o conteudo limpo na lista

    create_dictionary(clean_list)


def create_dictionary(clean_list):
    word_count = {}

    for word in clean_list: #conta as palavras e faz um top 20 das palavras
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    #contador das palavras mais citadas no site
    for key, value in sorted(word_count.items(),
                             key = operator.itemgetter(1)):
        print('% s : % s ' % (key, value))

    c = Counter(word_count) #counter do Colletions

    top = c.most_common(10)
    print(top)

if __name__ == '__main__':
    #consulta = input('Informe o site a ser pesquisado: ')
    start('https://www.geeksforgeeks.org/python-programming-language/?ref=leftbar')
