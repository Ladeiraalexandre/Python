largura = int(input())
altura = int(input())

'''a = 1
while a <= altura:
    if a == 1 or a == altura:
        print('#' * largura, end='\n')
    else:
        l = largura-4
        print('#',(' ' * l),'#')
    a = a + 1

largura = int(input())
altura = int(input())'''

a = 1
while a <= altura:
    print('#', end="")
    coluna = 2
    while coluna < largura:
        if a == 1 or a == altura:
          print('#', end="")
        else:
          print(end=" ")

        coluna = coluna + 1
    
    print("#")
    a = a + 1