from func_fatorial import fatorial

def testa_fatorial():
    if fatorial(1) == 1:
        print('Teste para 1 ok')
    else:
        print('Teste para 1 falhou')
    if fatorial(2) == 2:
        print('Teste para 2 ok')
    else:
        print('Teste para 2 falhou')
    if fatorial(0) == 1:
        print('Teste para 0 ok')
    else:
        print('Teste para 0 falhou')
    if fatorial(5) == 120:
        print('Teste para 5 ok')
    else:
        print('Teste para 5 falhou')
    
if __name__ == '__main__':
    testa_fatorial()
    