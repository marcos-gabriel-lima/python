def ficha(jogador):
    print(f'O jogador ', end='')
    if jogador == '':
        jogador = "< desconhecido >"
        print(f'{jogador} ', end='')
    else:
        print(f'{jogador} ', end='')
    print(f'fez ', end='')
    if gol.isalnum():
        print(f'{gol}', end='')
    else:
        print('0', end='')
    print(' no campeonato.')


nome = str(input('Informe o nome do jogador: ')).strip().capitalize()
gol = str(input('Números de gol(s): ')).strip()
ficha(nome)
