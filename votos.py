def voto(ano):
    '''
    -> usa outra função só para mostrar na tela o ano e a idade
    -> importa o ano atual
    -> se for menor, que o 16 print: NÃO VOTA
    -> se for maior ou igual a 16, e, menor que 65 mostra: VOTO OBRIGATÓRIO
    -> se for mior que 65, mostra: VOTO OPICIONAL
    CÓDIGO DA DEF:
            def frase():
        print(f'Nascido em {ano}, a idade é de {idade}: ', end='')
    from datetime import date as a
    idade = a.today().year - ano
    if idade < 16:
        frase()
        return print(f'NÃO VOTA!!!')
    elif 65 > idade >= 16:
        frase()
        return print(f'VOTO OBRIGATÓRIO!!!')
    else:
        frase()
        return print(f'VOTO OPCIONAL!!!')
    '''
    def frase():
        '''-> Mostra o ano e a idade
        CÓDIGO DA DEF:
            print(f'Nascido em {ano}, a idade é de {idade}: ', end='')
        '''
        print(f'Nascido em {ano}, a idade é de {idade}: ', end='')
    from datetime import date as a
    idade = a.today().year - ano
    if idade < 16:
        frase()
        return print(f'NÃO VOTA!!!')
    elif 65 > idade >= 16:
        frase()
        return print(f'VOTO OBRIGATÓRIO!!!')
    else:
        frase()
        return print(f'VOTO OPCIONAL!!!')


ano = int(input('Em que ano você nasceu: '))
voto(ano)
help(voto)

