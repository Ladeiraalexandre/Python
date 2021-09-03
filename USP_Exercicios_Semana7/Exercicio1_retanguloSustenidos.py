largura = int(input())
altura = int(input())

while altura > 0:
    coluna = 1
    while coluna <= largura:
        print('#', end='')
        coluna = coluna + 1
    print()
    altura = altura - 1
