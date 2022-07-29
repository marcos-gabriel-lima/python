def leiaint(lendo):
    '''Tratamento de números
    para n:Recebe uma string
    While True: Para verificar se pode ser um número
    if n.isnumeric():se for numérico retorna n em inteiro
    else:continua se perguntando até digite um número
    CÓDIGO DA FUNÇÃO:
        n = str(input(lendo)).strip()
        while True:
            if n.isnumeric():
                print(f'Você acabou de digitar o número {n}')
                return int(n)
            else:
                print('ERROR, digite um número!')
                n = str(input(('Digite um número: '))).strip()
    '''
    n = str(input(lendo)).strip()
    while True:
        if n.isnumeric():
            print(f'Você acabou de digitar o número {n}')
            return int(n)
        else:
            print('ERROR, digite um número!')
            n = str(input(('Digite um número: '))).strip()


n = leiaint('digite um número: ')
help(leiaint)
