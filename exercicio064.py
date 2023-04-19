# CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS PELO TECLADO, NO FINAL DA EXECUÇÃO, MOSTRE: #
# A MÉDIA ENTRE TODOS OS VALORES E QUAL FOI O MAIOR E O MENOR NÚMERO LIDO. #
# O PROGRAMA DEVE PERGUNTAR AO USUÁRIO SE ELE QUER CONTINUAR OU NÃO A DIGITAR VALORES.

maior = 0
menor = 0
soma = 0
cont = 1
num = int(input('Digite um valor: '))

while num != 78432674863256931246723652437213748623:
    soma += num
    media = soma / cont
    op = int(input('Quer continuar? DIGITE: 1 - SIM | 2 - NÃO '))
    if num > maior:
        maior = num
    if num < maior:
        menor = num
    if op == 1:
        num = int(input('Digite um valor:'))
        cont += 1

    elif op == 2:
        break

print('=-'*35)
print('Voce digitou {} números.'.format(cont))
print('A soma dos valores, é {}'.format(soma))
print('A média dos valores, é {}'.format(media))
print('O maior númeeo lido, foi {}'.format(maior))
print('O menor número lido, foi {}'.format(menor))


