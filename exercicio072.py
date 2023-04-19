# CRIE UMA TUPLA PREENCHIDA COMS OS 20 PRIMEIROS COLOCADOS PELA TABELA DO CAMPEONATO BRASILEIRO DE FUTEBOL
# NA ORDEM DE COLOCAÇÃO E DEPOIS MOSTRE:
# A - OS 5 PRIMEIROS COLOCADOS
# B - OS 4 ULTIMOS COLOCADOS DA TABELA
# C - UMA LISTA COM OS TIMES EM ORDEM
# D - EM QUE POSIÇÃO DA TABLA ESTÁ O JUVENTUDE #

list = (' ', 'palmeiras', 'internacional', 'fluminense', 'corinthians', 'flamengo', 'athelico-PR', 'atlético-PR', 'Fortaleza',
 'São Paulo', 'América MG', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará SC', 'Atlético-GO',
 'Avaí', 'Juventude'.lower())

ordem = sorted(list)
juve = list.index('juventude')

print(f"lista do BRASILEIRASSO: {list[1:]}")
print('-'*30)
print(f"Os 5 primeiros colocados da lista, são: {list[1:6]}")
print('-'*30)
print(f"Os 4 últimos colocados da lista, são: {list[-4:]}")
print('-'*30)
print(f"Os times em ordem alfabética, ficam: {ordem[1:]}")
print('-'*30)
print(f'O Juventude está na Posição {juve}')
print('-'*30)

