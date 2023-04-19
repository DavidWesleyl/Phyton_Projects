#PEDRA PAPEL TESOURA

import random
from time import sleep
print('JOKENPO')
print('Suas Opções:')
print('''[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Digite um numero:'))
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = random.randint(0, 2)

print('JO..')
sleep(1)
print('KEN..')
sleep(1)
print('PO!')


print('-='*20)

#JOGADOR WINS

if jogador == 0 and computador == 2:
    print('O jogador escolheu: PEDRA')
    print('O computador escolheu: {}'.format(itens[computador]))
    print('=-'*20)
    print('*** JOGADOR É O VENCEDOR! ***')
elif jogador == 1 and computador == 0:
    print('O jogador escolheu: PAPEL')
    print('O computador escolheu: {}'.format(itens[computador]))
    print('=-'*20)
    print('*** JOGADOR É O VENCEDOR! ***')
elif jogador == 2 and computador == 1:
    print('O jogador escolheu: TESOURA')
    print('O computador escolheu: {}'.format(itens[computador]))
    print('=-'*20)
    print('*** Jogador é o vencedor! ***'.upper())
elif jogador == computador:
    print('EMPATE!')
    print('Jogador escolheu: {}'.format(itens[jogador]))
    print('Computador escolheu:{}'.format(itens[computador]))

#COMPUTADOR WINS

if computador == 0 and jogador == 2:
    print('O jogador escolheu: TESOURA')
    print('O computador escolheu: {}'.format(itens[computador]))
    print('=-'*20)
    print('*** COMPUTADOR É O VENCEDOR! ***')
elif computador == 1 and jogador == 0:
    print('O jogador escolheu: PEDRA')
    print('O computador escolheu: {}'.format(itens[computador]))
    print('=-'*20)
    print(' *** computador é o vencedor! ***'.upper())
elif computador == 2 and jogador == 1:
    print('O jogador escolheu: PAPEL')
    print('O computador escolheu: {}'.format(itens[computador]))
    print('=-'*20)
    print('*** COMPUTADOR É O VENCEDOR!! ***')






