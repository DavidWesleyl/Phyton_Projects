# MELHORE O JOGO DE ADIVINHAÇÃO, ONDE O COMPUTADOR VAI PENSAR EM UM NUMERO DE 0 à 10.
# SÓ QUE AGORA O JOGADOR VAI TENTAR ADIVINHAR ATÉ ACERTAR, MOSTRANDO NO FINAL, QUANTOS PALPITES FORAM NECESSÁRIOS
# PARA VENCER.

from random import randint

maquina = randint(0, 10)
print(maquina)
contador = 0

while contador != maquina:
    user = int(input('>> Digite um número e tente acertar:'))
    if user != maquina:
        print('Errado, tente novamente!')
    contador += 1
    if user == maquina:
        print('-------------------------------------------------')
        print('Eu pensei no número {}, parabéns'.format(maquina))
        print('Mas foram {} tentativas para você acertar'.format(contador))
        break


