pessoa = dict()
banco_pessoa = list()
media = soma = mulhesres = 0
while True:
    pessoa['nome'] = str(input('Nome: ')).strip()
    sexo = str(input('SEXO: [ M / F ]  ')).strip().lower()
    while sexo != 'm' and sexo != 'f':
        print('ERRO!, por favor, digite apenas M ou F')
        sexo = str(input('SEXO: [ M / F ]  ')).strip().lower()
    pessoa['sexo'] = sexo
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    banco_pessoa.append(pessoa.copy())
    pessoa.clear()
    opc = str(input('Quer continuar? [ S / N ]: ')).strip().lower()
    while opc != 'n' and opc != 's':
        print('ERRO, responda somente com S ou N!')
        opc = str(input('Quer continuar? [ S / N ]: ')).strip().lower()
    if opc == 'n':
        break
media = soma / len(banco_pessoa)
print(f'Pessoas cadastradas foram {len(banco_pessoa)}')
print(f'A média de idades é {media}')
print(f'As mulheres cadastras foram: ', end='')
#print(banco_pessoa)
for p, m in enumerate(banco_pessoa):
    if m['sexo'] == 'f':
        print(f'{m["nome"]}, ', end='')
print()
for m in banco_pessoa:
    if m['idade'] >= media:
        for p, c in m.items():
            print(f"{p}:{c}; ", end='')
        print()


