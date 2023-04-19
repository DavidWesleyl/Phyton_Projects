# CRIE UM PROGRAMA QUE LEIA DOIS VALORES E MOSTRE UM MENU NA TELA:
# 1. SOMAR, 2. MULTIPLICAR, 3. MAIOR NUMERO, 4. NOVOS VALORES, E 5. SAIR #
# SEU PROGRAMA DEVERÁ REALIZAR UMA OPERAÇÃO SOLICITADA EM CASA CASO. #

from time import sleep

soma = maior = c = 0

     #     P R I M E I R O   B L O C O      #

v1 = int(input('Digite o primeiro valor:'))
v2 = int(input('Digite o segund valor: '))


print('>>> OLÁ, O QUE VOCÊ DESEJA?')
print('-'*27)
print('''1 - SOMAR
2 - MULTIPLICAR
3 - VER O MAIOR NÚMERO
4 - NOVOS VALORES
5 - SAIR''')
print('-'*27)
op = int(input('Digite sua opção: '))
print('-'*27)


while op == 1:
   print('A soma dos valores, é {}'.format(v1+v2))
   break

while op == 2:
   print('A multiplicação dos valores, é {}'.format(v1*v2))
   break

while op == 3 and v1 > v2:
   print('O maior número digitado, foi {}'.format(v1))
   break

while op == 3 and v1 < v2:
   print('O maior número digitado foi {}'.format(v2))
   break
while op == 3 and v1 == v2:
    print('Não existe valor maior, pois ambos são iguais!')
    break
print(' ')

            #      S E G U N D O  B L O C O       #


while op == 4:
    v1 = int(input('Digite o primeiro valor:'))
    v2 = int(input('Digite o segund valor: '))

    print('>>> OLÁ, O QUE VOCÊ DESEJA?')
    print('-' * 27)
    print('''1 - SOMAR
2 - MULTIPLICAR
3 - VER O MAIOR NÚMERO
4 - NOVOS VALORES
5 - SAIR''')
    print('-' * 27)
    op = int(input('Digite sua opção: '))
    print('-' * 27)

    while op == 1:
        print('A soma dos valores, é {}'.format(v1 + v2))
        break

    while op == 2:
        print('A multiplicação dos valores, é {}'.format(v1 * v2))
        break

    while op == 3 and v1 > v2:
        print('O maior número digitado, foi {}'.format(v1))
        break

    while op == 3 and v1 < v2:
        print('O maior número digitado foi {}'.format(v2))
        break
    while op == 3 and v1 == v2:
        print('Não existe valor maior, pois ambos são iguais!')
        break
print(' ')


while op != 5:


    #   T E R C E I R O   B L O C O   #
    v1 = int(input('Digite o primeiro valor:'))
    v2 = int(input('Digite o segund valor: '))

    print('>>> OLÁ, O QUE VOCÊ DESEJA?')
    print('-' * 27)
    print('''1 - SOMAR
2 - MULTIPLICAR
3 - VER O MAIOR NÚMERO
4 - NOVOS VALORES
5 - SAIR''')
    print('-' * 27)
    op = int(input('Digite sua opção: '))
    print('-' * 27)

    while op == 1:
        print('A soma dos valores, é {}'.format(v1 + v2))
        break

    while op == 2:
        print('A multiplicação dos valores, é {}'.format(v1 * v2))
        break

    while op == 3 and v1 > v2:
        print('O maior número digitado, foi {}'.format(v1))
        break

    while op == 3 and v1 < v2:
        print('O maior número digitado foi {}'.format(v2))
        break
    while op == 3 and v1 == v2:
        print('Não existe valor maior, pois ambos são iguais!')
        break
print(' ')

#     F I N A L I Z A N D O    #

print('SAINDO..')
sleep(2)


















