#JOGO DE ADIVINHAÇÃO
from random import randint
from time import sleep
computador = randint(0, 5) #Faz o computador pensar

n = int(input('Vou pensar  em um número entre 0 e 5, tente adivinhar. Digite o número: ')) #Jogador tenta adivinhar
print('\033[0:33m Processando...')
sleep(2)

if computador == n:
    print('\033[0:32m Parabéns, você ACERTOU!!')

else: print('\033[0:31m Você errou.. EU pensei no número {} e você no {}'.format(computador, n))