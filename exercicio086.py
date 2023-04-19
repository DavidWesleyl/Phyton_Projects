# APRIMORE O DESAFIO ANTERIOR, MOSTRANDO NO FINAL:
# A - A SOMA DE TODOS OS VALORES PARES DIGITADOS
# B - A SOMA DOS VALORES DA TERCEIRA COLUNA
# C - O MAIOR VALOR DA SEGUNDA LINHA #

lista = []
maior_valor = 0
pares = []

for coluna in range(3):
    for linha in range(3):
        num = int(input(f'Digite um valor na posição [ {coluna}, {linha} ]: '))
        lista.insert(0, num)
        if num % 2 == 0:
            pares.append(num)
            soma = sum(pares)

print('='*40)
print(f'[ {lista[8]} ] [ {lista[7]} ] [ {lista[6]} ]')
print(f'[ {lista[5]} ] [ {lista[4]} ] [ {lista[3]} ]')
print(f'[ {lista[2]} ] [ {lista[1]} ] [ {lista[0]} ]')
print('='*40)

print(f'A soma dos valores da terceira coluna é: [ {lista[2] + lista[1] + lista[0]} ]')

if lista[5] > maior_valor:
    maior_valor = lista[5]
if lista[4] > maior_valor:
    maior_valor = lista[4]
if lista[3] > maior_valor:
    maior_valor = lista[3]

print(f'O maior valor da segunda coluna, é: [ {maior_valor} ]')
print(f'A soma dos valores pares, é [ {soma} ]')









