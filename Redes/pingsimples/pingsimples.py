import os #biblioteca 'os' integra os programas e recursos do SO

print('#' * 40) #imprime o # 40 vezes

ip_host = input('Informe o ip ou host a ser verificado: ')
print('-' * 40)
print(os.system('ping -n 6 {}'.format(ip_host)))
print('-' * 40)