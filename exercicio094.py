# APRIMORE O DESAFIO 092 PARA QUE ELE FUNCIONE COM VÁRIOS JOGADORES, INCLUINDO UM SISTEMA DE VISUALIZAÇÃO ÚNICA
# PARA CADA JOGADOR #

dados_jogador = dict()
gols = list()
dados_totais = list()


while True:
    dados_jogador['nome'] = str(input('Digite o nome do jogador: '))
    dados_jogador['partidas'] = int(input(f'Quantas partidas {dados_jogador["nome"]} jogou? '))
    for partidas in range(dados_jogador['partidas']):
        gols.append(int(input(f'Quantos gols na {partidas}ª partida? ')))
        dados_jogador['gols'] = gols[:]
        dados_jogador['score'] = sum(gols)
    dados_totais.append(dados_jogador.copy())
    gols.clear()

    perg = str(input('Contiune? s/n: '))
    if perg in 'Nn':
        break
print('-'*60)
for time, jogadores in enumerate(dados_totais):
    print(f'ORDEM: {time} | NOME: {jogadores["nome"]} | GOLS: {jogadores["gols"]}  |  SCORE: {jogadores["score"]} ')
print('-'*60)

while True:
    pergunta = int(input('QUal jogador você deseja ver o aproveitamento de forma individual? (999 encerra)'))

    if pergunta == 999:
        print('< Obrigado por usar o programa >')
        break
    if pergunta >= len(dados_totais):
        print('# ESSE JOGADOR NÃO EXISTE! #')
    else:
        print(f'------- LEVANTAMENTO DO JOGADOR {dados_totais[pergunta]["nome"]} -------')
        for jogador, gols in enumerate(dados_totais[pergunta]['gols']):
            print(f' Na {jogador}ª partida fez {gols} gols')







