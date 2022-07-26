def fatorial(n, show=False):
    '''Calcula o fatorial de um número.
    :para n:O número a ser calculado.
    :para show:(opcional) Mostrar ou não a conta.
    :return f: retorna a multicacao para formar a multiiplicacao
    -> CÓDIGO DA DEF:
        f = 1
        for c in range(n, 0, -1):
            if show:
                print(f'{c}', end="")
                print(f' x 'if c > 1 else ' = ', end='')
            f *= c
        return f'''
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(f'{c}', end="")
            print(f' x 'if c > 1 else ' = ', end='')
        f *= c
    return f


print(fatorial(5, show=True))
help(fatorial)
