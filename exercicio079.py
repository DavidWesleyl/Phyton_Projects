# CRIE UM PROGRAMA ONDE O USUÁRIO POSSA DIGITAR 5 VALORES NÚMERICOS E CADASTRE-OS EM UMA LISTA
# JÁ NA POSIÇÃO CORRETA DE INSERÇÃO SEM USAR O SORT
# NO FINAL, MOSTRE A LISTA NA TABELA #

# PARA FAZERMOS ESTE EXERCICIO, USAREMOS A OPÇÃO "BISECT" #

import bisect

lista = []
for valor in range(0, 5):
    num = int(input('>> Digite um valor para adiconar a lista: '))
    bisect.insort(lista, num)
    print(f'# O valor {num} foi adicionado a posição {lista.index(num)} #')
print('-'*40)
print(f'Sua lista será: {lista}')








