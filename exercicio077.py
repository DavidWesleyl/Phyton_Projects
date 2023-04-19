# FAÇA UM PROGRAMA QUE LEIA 5 VALORES NUMÉRICOS E GUARDE-OS EM UMA LISTA. NO FINAL, MOSTRE QUAL FOI O MAIOR E MENOR VALOR
# DIGITADOR E SUAS RESPECTIVAS POSIÇÕES NA LISTA. #

lista = []

for valor in range(0, 5):
    lista.append(int(input('Digie um valor para adicionar a lista: ')))
for pos, valor in enumerate(lista):
    if valor == max(lista):
        print(f'O maior valor digitado foi {max(lista)}, na posição {pos}')
    if valor == min(lista):
        print(f'O menor valor digitado foi {min(lista)}, na posição {pos}')




























