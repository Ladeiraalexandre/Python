def maximo(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    print(maximo(a, b, c))