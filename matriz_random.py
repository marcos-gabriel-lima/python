from random import randint as rt
from time import sleep as s
matriz = list()
lista = list()
linha = int(input('Informe quantidade de linha: '))
coluna = int(input('Informe quantidade de colunas: '))
jessica = pares = soma = maior = 0
for i in range(linha):
    for j in range(coluna):
        valor = rt(0, 9)
        s(0.3)
        print(f'Informe o valor para [{i}, {j}]: {valor}')
        s(0.3)
        if valor % 2 == 0:
            pares += valor
        if j == 2:
            soma += valor
        if i == 1:
            if maior == 0:
                maior = valor
            if valor > maior:
                maior = valor
        lista.append(valor)
        matriz.append(lista[:])
        lista.clear()
for m in matriz:
    s(0.6)
    print(f'{m}', end='')
    jessica += 1
    if jessica == coluna:
        print()
        jessica = 0
s(0.6)
print(f'A soma dos valores pares é {pares}')
s(0.6)
print(f'A soma dos valores da terceira coluna é {soma}')
s(0.6)
print(f'O maior valor da segunda linha {maior}')