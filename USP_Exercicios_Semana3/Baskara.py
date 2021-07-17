import math

a = float(input('Informe um valor para a: '))
b = float(input('Informe um valor para b: '))
c = float(input('Informe um valor para c: '))

x1 = 0
x2 = 0

delta = pow(b,2) - (4*(a*c))

if delta >= 0:
    raiz_delta = math.sqrt(delta)
    
    x1 = (-b + (raiz_delta)) / (2*a)
    x2 = (-b - (raiz_delta)) / (2*a)
    
    if delta == 0:
          if x1 == x2:
              print(f'a raiz dupla desta equação é {x1}')
          else:
              print(f'a raiz desta equação é {x1}')
    else:
          if x1 < x2:
              print(f'as raízes da equação são {x1} e {x2}')
          else:
              print(f'as raízes da equação são {x2} e {x1}')
else:
    print('esta equação não possui raízes reais')