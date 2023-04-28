def resumo(valor=0, porcentagem=0, reduc=0):
    print('-'*30)
    print('     RESUMO DO VALOR     ')
    print('-'*30)
    print(f'Preço analisado: {formatacao(valor)}')

    metade = valor / 2
    print(f'Metade do preço: {formatacao(metade)}')

    dobro = valor * 2
    print(f'Dobro do preço:  {formatacao(dobro)}')


    aumento = (valor/100 * porcentagem/1) + valor
    print(f'{porcentagem}% de aumento:  {formatacao(aumento)}')

    reducao = valor - (valor/100 * reduc/1)
    print(f'{reduc}% de redução:  {formatacao(reducao)}')

def formatacao(valor=0):
    cifra = 'R$'
    return f"{cifra} {valor:.2f}".replace('.', ',')


