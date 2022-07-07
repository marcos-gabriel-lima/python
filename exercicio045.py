from random import randint
print('''
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura
''')
lista = ['Pedra', 'Papel', 'Tesoura']
computador = randint(1,3)
jogador = int(input('Escolha: '))
if computador == 1 and jogador == 1:
    print(f'Computador escolheu {lista[0]}\nJogador escolheu {lista[0]}\nEMPATE!!!')

elif computador == 1 and jogador == 2:
    print(f'Computador escolheu {lista[0]}\nJogador escolheu {lista[1]}\nJogador Ganhou!!!')

elif computador == 1 and jogador == 3:
    print(f'Computador escolheu {lista[0]}\nJogador escolheu {lista[2]}\nComputador Ganhou!!!')

# computador escolheu 2

if computador == 2 and jogador == 1:
    print(f'Computador escolheu {lista[1]}\nJogador escolheu {lista[0]}\nComputador Ganhou!!!')

elif computador == 2 and jogador == 2:
    print(f'Computador escolheu {lista[1]}\nJogador escolheu {lista[1]}\nEMPATE!!!')

elif computador == 2 and jogador == 3:
    print(f'Computador escolheu {lista[1]}\nJogador escolheu {lista[2]}\nJogador Ganhou!!!')
#Computador escolheu 3

if computador == 3 and jogador == 1:
    print(f'Computador escolheu {lista[2]}\nJogador escolheu {lista[0]}\nComputador Ganhou!!!')

elif computador == 3 and jogador == 2:
    print(f'Computador escolheu {lista[2]}\nJogador escolheu {lista[1]}\nEMPATE!!!')

elif computador == 3 and jogador == 3:
    print(f'Computador escolheu {lista[2]}\nJogador escolheu {lista[2]}\nJogador Ganhou!!!')

