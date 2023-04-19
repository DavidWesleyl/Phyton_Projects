# FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA FICHA(), QUE RECEBA DOIS PARAMETROS OPCIONAIS: O NOME DO JOGADOR E
# QUANTOS GOLS ELE MARCOU. O PROGRAMA DEVERÁ SER CAPAZ DE MOSTAR "DESCONHECIDO" SE NÃO FOR INFORMADO O NOME E
# MOSTRAR ZERO GOLS SE NÃO FOR INFORMADO NENHUM GOL #


def ficha(jogador='Desconhecido', gols=0):
        print(f'** O jogador {jogador} marcou {gols} gol(s) no campeonato. **')


nome = str(input('Nome do jogador: '))
gol = str(input('Quantidade de gols marcados: '))
if gol.isnumeric():
        gols = int(gol)
else:
        gol = 0
if len(nome) == 0:
        nome= '< Desconhecido >'


ficha(nome, gol)













