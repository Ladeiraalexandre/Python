import random, string

tamanho = int(input('Digite o tamanho de senha que você deseja: ')) #senha com 16 caracteres

#metodo que envolve uper e lower case, gerando letras maiusculas e minusculas na seha,
#depois adicionamos digitos e caracteres especiais para poder formar uma senha forte
chars = string.ascii_letters + string.digits + '!@#$%*()-=+'

#utiliza da biblioteca OS a classe urandom, que gera numeros aleatorios a partir de fontes fornecidas pelo SO
rnd = random.SystemRandom()

#esse for faz um join onde utiliza a função randomica e escolha um dos atributos de chars
# a cada passada na variavel tamanho. Sendo assim, vai para cada digto de 16 randomizar com o que esta em chars
print(''.join(rnd.choice(chars) for i in range(tamanho)))