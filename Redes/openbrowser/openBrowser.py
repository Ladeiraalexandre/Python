import webbrowser
from tkinter import *

#objeto para representar o tkinter
root = Tk( )#quando tem o espço quer dizer que é none, não tem nome a tela

root.title('Abrir Browser')

#tamanho da janela do sistema
root.geometry('300x200')

def google():
    webbrowser.open('www.google.com')

#command chama a funcão google
mygoogle = Button(root, text='Abrir o Google', command=google).pack(pady=20)#posição do botão
root.mainloop()