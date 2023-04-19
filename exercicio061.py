# PROGRESSÃO ARITMÉTCA COM WHILE & DIGITAR QUANTAS DESEJA VER, ATÉ O USUÁRIO DIGITAR 0

from time import sleep

print('=-'*20)
print('SUPER GERADOR DE P.A')
print('=-'*20)

primeiro_termo = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a razao:'))
cont = 1
prog = primeiro_termo
op = 10
total = 0

while op != 0:
    total = total + op
    while cont <= total:
        print('{} - '.format(prog), end=' ')
        cont += 1
        prog += razao
    print('PAUSA')
    op = int(input('Quantos termos a mais você deseja ver? '))
print('FINALIZANDO.. ')
sleep(1)
print('Você digitou no total {} números'.format(cont))
























