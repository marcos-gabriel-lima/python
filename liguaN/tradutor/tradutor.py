def tradutor(liguagem):
    import tradutor.banco
    tradutor.banco.dados()
    b = i = 0
    while i < len(liguagem):
        for p, c in enumerate(tradutor.banco.banco()):
            if c in liguagem[b]:
                print(f'{c}', end='')
        i += 1
        b += 1
    b = i = 0
    print()
    while i < len(liguagem):
        for p, c in enumerate(tradutor.banco.banco()):
            if c in liguagem[b]:
                print(f'{tradutor.banco.dados()[p]}', end='')
        i += 1
        b += 1
    print()


def codigo(codificando):
    import tradutor.banco
    s = i = ''
    for c in codificando:
        s += c
        if s in tradutor.banco.dados():
            print(f'{tradutor.banco.banco()[tradutor.banco.dados().index(s)]}', end='')
            s = ''
            i = 'True'
    print()
    if i != 'True':
        print('CÓDIGO INCORRETO !!!')
