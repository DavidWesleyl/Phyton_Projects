# CRIE UM PROGRAMA ONDE 4 JOGADORES JOGUEM UM DADOS E TENHAM UM RESULTADO ALEATÓRIOS. GUARDE ESSES RESULTADOS EM
# UM DICIONÁRIO. NO FINAL, COLOQUE ESSE DICIONÁRIO EM ORDEM SABENDO QUE O VENCEDOR TIROU O MAIOR NÚMERO #

from random import randint
from time import sleep
lista = []
cont = 0
jogador = { 'Jogador_01': randint(1, 6),
            'Jogador_02': randint(1, 6),
            'Jogador_03': randint(1, 6),
            'Jogador_04': randint(1, 6)
            }

for jogo, dado in jogador.items():
    print(f'{jogo} tirou {dado} no dado.')
    sleep(1)
print(' === RANKING ===')

for jogadores, ranking in sorted(jogador.items(), key=lambda item: item[1], reverse=True):
    print(f'{cont+1}º lugar > {jogadores} com {ranking} pontos')
    cont += 1
    sleep(1)
