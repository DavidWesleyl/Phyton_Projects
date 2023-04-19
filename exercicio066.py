# FAÇA UM PROGAA QE LEIA A TABUADA DE VÁRIOS NÚMEROS, UM DE CADA VEZ, PARA CADA VALOR DIGITADO PELO #
# USUÁRIO. O PROGRAMA SERÁ ENCERRADO QUANDO UM VALOR NEGATIVO FOR SOLICITADO. #

from time import sleep
while True:

    num = int(input('Digite um número para ver a tabuada:'))
    print('-'*35)
    if num < 0:
        break
    for c in range(1, 11):
        multi = num * c
        print(f'{num} x {c} = {multi}')
    print('-'*35)

print('ENCERRANDO PROGRAMA..')
sleep(2)
print('PROGRAMA ENCERRADO. VOLTE SEMPRE!!')


