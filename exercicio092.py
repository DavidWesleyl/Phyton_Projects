# CRIE UM PROGRAMA QUE GERENCIE O APROVEITAMENTO DE UM JOGADOR DE FUTEBOL. O PROGRAMA VAI LER:
# NOME DO JOGADOR E QUANTAS PARTIDAS ELE JOGOU DEPOIS VAI LER A QUANTIDADE DE GOLS FEITOS EM CADA PARTIDA. NO FINAL,
# TUDO SERÁ GUARDADO EM UM DICIONÁRIO, INCLUINDO O TOTAL DE GOLS FEITOS DURANTE O CAMPEONATO #

dados = dict()
gols = list()
jogadores = list()
cont = 0

for listagem in range(1):
    dados['nome'] = str(input('Nome do jogador: '))
    dados['partidas'] = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    for partidas in range(dados['partidas']):
        gols.append(int(input(f'Quantos gols na {partidas+1}ª partida? ')))
    dados['gols'] = gols[:]
    dados['score'] = sum(gols)
    gols.clear()
    jogadores.append(dados.copy())

print('== RESULTADO == ')
print(f'o jogador {dados["nome"]}'.upper())
for jogo, gol in enumerate(dados["gols"]):
    print(f'Na {jogo+1}ª partida fez {gol} gol(s)')
print(f'{dados["nome"].upper()} Teve um aproveitamento de {dados["score"]} gols')












