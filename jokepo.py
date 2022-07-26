print("//" * 20)
print("Brincadeira do Jokepô")
print("//" * 20)
n = str(input("para participar me informe seu nome: ")).strip().capitalize()
v = empt = d = p = 0
while True:
    from random import randint
    from time import sleep
    print("//"*20)
    print("Brincadeira do Jokepô")
    print("//"*20)
    computador = randint(0, 2)
    opcoes = ['Pedra', 'Papel', 'Tesoura']
    print("""Escolha
        \033[36;7m[ 0 ]\033[m\033[30m Pedra
        \033[36;7m[ 1 ]\033[m\033[30m Papel
        \033[36;7m[ 2 ]\033[m\033[30m Tesoura""")
    e = int(input("escolha a sua opção: "))
    print("JO")
    sleep(.5)
    print("KEM")
    sleep(.5)
    print("PO")
    print("O computador escolheu {} ".format(opcoes[computador]))
    if computador == 0:
        if e == 0:
                print("O jogador escolheu {}".format(opcoes[e]))
                print("\033[35mEMPATE")
                empt += 1
        elif e == 1:
                print("O jogador escolheu {}".format(opcoes[e]))
                print("{:=^20} \033[32mVENCEU ".format(n))
                v += 1
        elif e == 2:
                print("O jogador escolheu {}".format(opcoes[e]))
                print("\033[31mPERDEU\033[30m, não foi desse vez {:=^20}".format(n))
                d += 1
        else:
                print("\033[31mOPCÃO INVÁLIDA !!!")
    elif computador == 1:
        if e == 0:
                print("O jogador escolheu {}".format(opcoes[e]))
                print("\033[31mPERDEU\033[30m, não foi desse vez {:=^20}".format(n))
                d += 1
        elif e == 1:
                print("O jogador escolheu {}".format(opcoes[e]))
                print("\033[35mEMPATE")
                empt += 1
        elif e == 2:
                print("O jogador escolheu {}".format(opcoes[e]))
                print("{:=^20} \033[32mVENCEU".format(n))
                v += 1
        else:
                print("\033[31mOPCÃO INVÁLIDA !!!")
    elif computador == 2:
        if e == 0:
                print("O jogador escolheu {:=^20}".format(opcoes[e]))
                print("{:=^20} \033[32mVENCEU".format(n))
                v += 1
        elif e == 1:
                print("O jogador escolheu {:=^20}".format(opcoes[e]))
                print("\033[31mPERDEU\033[30m, não foi desse vez {}".format(n))
                d += 1
        elif e == 2:
                print("O jogador escolheu {:=^20}".format(opcoes[e]))
                print("\033[35mEMPATE")
                empt += 1
        else:
                print("\033[31mOPCÃO INVÁLIDA !!!")
    opc = str(input('Deseja continuar: [ S / N ] ')).strip().capitalize()
    while opc != "S" and opc != "N":
        print('ERROR, digite apenas S ou N')
        opc = str(input('Deseja continuar: [ S / N ] ')).strip().capitalize()
    if opc == 'N':
        break
print(f'Número de partidas foi de {p}\n\033[32mVocê ganhou {v}\n\033[31mPerdeu {d}\n\033[35mEmpatou {empt}')
