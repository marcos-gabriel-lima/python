print('| [ \c ] -> Traduzir | \n| [ \# ] -> Codifica |')
while True:
    from tradutor import tradutor as t
    f = str(input('[ \c ] ou [ \# ]: ')).strip().lower()
    while f != '\c' and f != '\#':
        print('ERROR, escolha [ \c ] ou [ \# ]')
        f = str(input('[ \c ] ou [ \# ]: ')).strip().lower()
    if f == '\c':
        escreva = str(input('Digite a frase: ')).strip().lower()
        t.tradutor(escreva)
    elif f == '\#':
        escreva = str(input('Digite o codigo: ')).lower()
        t.codigo(escreva)
        print(escreva)
