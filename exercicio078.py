# CRIE UM PROGAMA ONDE O USUÁRIO POSSA DIGITAR VÁRIOS VALORES NUMÉRICOS E CADASTRE-OS EM UMA LISTA, CASO O NUMERO
# JÁ EXISTA, ELE NÃO SERÁ ADICIONADO. NO FINAL SERÃO EXIBIDOS TODOS OS VALORES UNICOS EM LISTA CRESCENTE #

lista = []

while True:
    num = int(input('>> Digite um valor para adicionar a lista: '))
    if num not in lista:
        lista.append(num)
    else:
        print(f'O número {num} já foi adicionado a lista.. ')
    pergunta = int(input('* Deseja continuar? [ SIM - press (1) | NÃO - press (2) ]: '))
    if pergunta == 2:
        break
    if pergunta > 2:
        print('# OPÇÃO INVÁLIDA #')
        pergunta = int(input('* Deseja continuar? [ SIM - press (1) | NÃO - press (2) ]: '))
        if pergunta == 2:
            break
print(f'Sua lista será: {sorted(lista)}.')

