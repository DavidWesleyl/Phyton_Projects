# CRIE UM PROGRAMA ONDE O USUÁRIO POSSA DIGITAR VÁRIOS NÚMEROS E ARMAZENA-LOS EM UM LISTA
# AO FINAL MOSTRE A LISTA DIGITADA, UMA LISTA SÓ COM NÚMEROS PARES E MA LISTA SÓ COM NÚMEROS IMPARES #

lista = []
lista_pares = []
lista_impar = []

while True:
    num = int(input('>> Digite um valor para adicionar a lista: '))
    lista.append(num)
    if num % 2 == 0:
        lista_pares.append(num)
    else:
        lista_impar.append(num)
    perg = int(input('# Deseja continuar? [SIM - press (1) NÃO - press (2) ]: '))
    if perg == 2:
        break
    elif perg > 2:
        print('# OPÇÃO INVÁLIDA! #')
        perg = int(input('# Deseja continuar? [SIM - press (1) NÃO - press (2) ]: '))
        if perg == 2:
            break
print('-'*40)
print(f'Sua lista ciada foi: {lista}')
print(f'Sua lista com os números pares: {lista_pares}')
print(f'Sua lista com os números impares: {lista_impar}')

