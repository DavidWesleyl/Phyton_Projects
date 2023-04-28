def interface(menu):
    print('-'*45)
    print(menu.center(50))
    print('-'*45)


def opcoes(nome):
    try:
        print('\033[33mSUAS OPÇÕES: \033[m')
        print('-' * 45)
        for posicao, item in enumerate((nome)):
            print(f'\033[36m{posicao+1} - \033[35m{item}\033[m')

    except:
        print('Erro! Digite um valor válido')









