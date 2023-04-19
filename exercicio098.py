# FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA MAIOR(), QUE RECEBA VÁRIOS PARAMETROS COM VALORES INTEIROS.
# SEU PROGRAMA TEM QUE ANALISAR TODOS OS VALORES E DIZER QUAL DELES É O MAIOR. #


def valor(* valores):
    maior = 0
    print('\nAnalisando os valores..')
    for numeros in valores:
        if numeros > maior:
            maior = numeros
        print(f'{numeros}', end=' ')
    print(f'Foram informados {len(valores)} valores')
    print(f'\nO maior valor lido foi [ {maior} ]')
    print('='*30)


valor(2, 9, 4, 5, 7, 1)
valor(4, 7, 0)
valor(1, 2)
valor(6)
valor()