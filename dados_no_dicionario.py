import random
from time import sleep as s
from operator import itemgetter as it
print(f'Valores sorteados', end='')
for c in range(0, 3):
    s(1)
    print(f'.', end='')
print()
jogo = {'jogador1': random.randint(1, 6),
        'jogador2': random.randint(1, 6),
        'jogador3': random.randint(1, 6),
        'jogador4': random.randint(1, 6)}
jogadores = list()
jogadores.append(jogo)
for k, v in jogo.items():
    print(f'o {k} tirou {v}')
    s(1)
jogadores = sorted(jogo.items(), key=it(1), reverse=True)
print('LISTA DO RANK: ')
for pos, num in enumerate(jogadores):
    s(1)
    print(f'O {jogadores[pos][0]} ficou em {pos + 1} lugar com o número {num[1]} sorteados')