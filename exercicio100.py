# CRIE UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA VOTO() QUE VAI RECEBER COMO PARAMETRO O ANO DE NASCIMENTO DE UMA PESSOA
# RETORNANDO UM VALOR LITERAL, INDICANDO SE UMA PESSOA TEM VOTO "NEGADO, OPCIONAL OU OBRIGATÓRIO" NAS ELEIÇÕES #
from datetime import date


def voto(*valor):
    print('-'*25)
    valor = int(input('Em que ano você nasceu? '))
    ano = date.today().year
    opcao = ano - valor
    return opcao


anos = voto(0000)
print(f'No ano atual você tem / irá fazer: {anos} anos.')
if anos < 16:
    print(f'NÃO É OBRIGATÓRIO!')

elif anos > 16 and anos < 60:
    print(f'VOTO OBRIGATÓRIO!')

else:
    print(f'VOTO OPCIONAL!')

