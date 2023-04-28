# FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA FICHA(), QUE RECEBA DOIS PARAMETROS OPCIONAIS: O NOME DE
# UM JOGADOR E A QUANTIDADE DE GOLS QUE ELE MARCOU.
# O PROGRAMA DEVERÁ SER CAPAZ DE MOSTRAR A FICHA DE UM JOGADOR, EMSMO QUE ALGUM DADO NÃO TENHA SIDO INFORMADO #


def jogador(nome='Descinhecido', gols=0):
    print(f'O jogador {nome} marcou {gols} gol(s) no campeonato')
nome = str(input('Nome do jogador: '))
gols = str(input('Quantos gols marcados? '))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if len(nome) == 0:
    nome = '< Desconhecido >'



jogador(nome, gols)
