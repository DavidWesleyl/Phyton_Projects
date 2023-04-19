# CRIE UM PROGRAMA QUE LEIA O NOME E O PREÇO DE VÁRIOS PRODUTOS. O PROGRAMA DEVERÁ PERGUTAR
# SE O USUÁRIO QUER CONTINUAR. NO FINAL MOSTRE:
# O VALOR TOTAL DA COMPRA, QUANTOS PRODUTOS CUSTAM MAIS DE 1000 REAIS, QUAL O RODUTO MAIS BARATO. #

soma = mil = maior = menor = cont = preco = 0
while True:

    print('='*35)
    print('SUPER   LOJÃO')
    print('='*35)

    prod = str(input(">> Digite o nome do produto:")).upper

    preco = float(input('>> R$ Preço:'))
    soma += preco
    cont += 1
    if preco > 1000:
        mil += 1

    if cont == 1:
        menor = preco
    else:
        if preco < menor:
            menor = preco

    op = int(input('Quer continuar? SIM - press { 1 } | Não - press { 2 }'))
    if op == 2:
        break



print(' ')
print('------------- FIM DO PROGRAMA -------------------')

print(f'O total da compra foi: {soma}')
print(f'Quantidade de produtos com mais de R$ 1000: {mil}')
print(f'Preço do produto mais barato: {menor:.2f}')