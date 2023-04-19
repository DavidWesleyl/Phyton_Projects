# CRIE UM PROGRAMA ONDE O USUÁRIO POSSA DIGITAR 7 VALALORES NUMÉRICOS EM UMA ÚNICA LISTA QUE MANTENHA SEPARADOS
# OS NÚMEROS PARES E ÍMPARES. NO FINAL MOSTRE OS VALORES PARES E IMPARES EM ORDEM CRESCENTE #

lista = [[], []]
for valores in range(0, 8):
    num = int(input('Digite o valor:'))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
    lista[0].sort()
    lista[1].sort()

print(f'Pares: {lista[0]}')
print(f'Impares: {lista[1]}')


