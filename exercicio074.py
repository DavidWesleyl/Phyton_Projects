# DESENVOLVA UM PROGRAMA QUE LEIA 4 VALORES PELO TECLADO E GUARDE-OS EM UMA TUPLA. NO FINAL MOSTRE:
# A - QUANTAS VEZES APARECEU O VALOR 9
# B - EM QUE POSIÇÃO FOI DIGITADO O VALOR 3
# C - QUAIS FORAM OS NUMEROS PARES #

n = 0
n1 = int(input('Digite o primeiro valor:'))
n2 = int(input('Digite o segundo valor:'))
n3 = int(input('Digite o penúltimo valor:'))
n4 = int(input('Digite o último valor:'))

tupla = (n, n1, n2, n3, n4)

print(f'O número 9 foi  visto {tupla.count(9)}x')
if 3 in tupla:
    print(f'O número 3 apareceu pela primeira vez na {tupla.index(3)} posição')
else:
    print('O número 3 não foi digitado!')
for p_ou_i in tupla[1:]:
    if p_ou_i % 2 == 0:
        print(f'Números pares: {p_ou_i}')













