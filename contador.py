from time import sleep as sl


def contador(i, p, f):
    print(f'De {i} até {f}, de {p} em {p}:')
    if p < 0:
        p *= -1
    if i < f:
        for c in range(i, f + 1, p):
            sl(0.5)
            print(f'{c} ', end='')
        print('FIM!')
    else:
        for c in range(i, f, -p):
            sl(0.5)
            print(f'{c} ', end='')
        print('FIM!')

    for c in range(0, 30):
        sl(0.2)
        print('=', end='')
    print()


print('Faça agora a sua sequência: ')
inicio = int(input('INICIO: '))
fim = int(input('FIM: '))
pulando = int(input('PULANDO: '))
contador(1, 1, 10)
contador(2, 2, 10)
contador(inicio, pulando, fim)
