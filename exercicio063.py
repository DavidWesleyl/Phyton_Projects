
#  T R A T A N D O        V A L O R E S        AL T O S   V1.0    #
# ---------------------------------------------------------------- #

# CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS PELO TECLADO. O PROGRAMA SÓ VAI PARAR
# QUANDO O USUÁRIO DIGITAR 999. NO FINAL MOSTRE QUANTOS NÚMEROS FORAM DIGITADOS E MOSTRE A SOMA ENTRE TODOS ELES
# DESCONSIDERANDO O FLAG #

contador = soma = 0
num = int(input('Digite um numero:'))
while num != 999:
    soma += num
    num = int(input('Digite um número:'))
    contador += 1

print('=-'*25)
print('Ao todo foram digitados {} números'.format(contador))
print('A soma dos números digitados, é {}'.format(soma))
