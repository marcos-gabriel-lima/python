pa = int(input('Digite o primeiro termo da progessão aritmética: '))
razao = int(input('Informe a razão da progressão aritmética: '))
c = 0
i = 0
continuar = 10
while continuar != 0:
    c = 0
    while c < continuar:
            i += 1
            c += 1
            pa += razao
            print(f'{pa}', end='')
            print(' => ' if c < continuar else ' |PAUSE|', end='')
    continuar = int(input('Quantos termos desejam ter mais: '))
print(f'O números de termos mostrado no foi de {i}')
