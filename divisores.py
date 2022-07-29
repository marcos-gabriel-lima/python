from time import sleep as sl
def leiaint(msg):
    msg = str(input(msg)).strip()
    while True:
        if msg.isnumeric():
            return int(msg)
        else:
            print('ERROR, digite um número inteiro!')
            msg = str(input('Informe um número inteiro: ')).strip()


number = leiaint('Informe um número inteiro: ')
print(f'Divisor(s) da cor verde', end='')
sl(2)
print('e o(s) não divisor(s) da cor vermelha:')
sl(2)
for c in range(1, number + 1):
    sl(0.5)
    if number % c == 0:
        print(f'\033[1;32m{c}', end='')
        print('-' if c != number else '', end='')
    else:
        print(f'\033[1;31m{c}', end='')
        print('-' if c != number else '', end='')