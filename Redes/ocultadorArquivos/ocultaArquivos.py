#programa para ocultar arquivos ou pastas
import ctypes

aSerOcultado = input('Informe o arquivo ou pasta a ser ocultado: ')
#definir o atributo do arquivo
atributo_ocultar = 0X02

#dll permite que arquivo seja mainpulado pelo SO e fique oculto atraves do SetFileAttributesW
retorno = ctypes.windll.kernel32.SetFileAttributesW(aSerOcultado, atributo_ocultar)

if retorno:
    print('Arquivo foi ocultado')
else:
    print('Arquivo não foi ocultado')