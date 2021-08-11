def vogal(c):
    if c.lower() == 'a' or c.lower() == 'e' or c.lower() == 'i' or c.lower() == 'o' or c.lower() == 'u':
       return True
    else:
        return False

print(vogal(input()))
     