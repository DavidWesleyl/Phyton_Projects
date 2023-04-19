# CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS PELO TECLADO. O PROGRAMA SÓ VAI PARAR QUANDO O USUÁRIO DIGITAR
# 999. NO FINAL, MOSTRE QUANTOS NÚMEROS FORAM DIGITADOS E QUAL FOI A SOMA ENTRE ELES. DESCONSIDERANDO O FLAG.


num = cont = soma = 0
while True:
    nome = int(input('Digite um número (999 para parar):'))
    if nome == 999:
        break
    cont += 1
    soma += nome

print(f'A soma dos {cont} valores, foi {soma}')