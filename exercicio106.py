# FAÇA UM MINI SITEMA QUE UTILIZE O INTERACTIVE HELP DO PHYTON. O USUÁRIO VAI  DIGITAR O COMANDO
# E O MANUAL VAI APARECER. QUANDO O USUÁRIO DIGITAR A PALAVRA FIM, O PROGRAMA SE ENCERRARÁ. OBS:
# USE CORES #

# PROGRAMA PRINCIPAL #
from time import sleep


def sistema():
    print('\033[46m \033[34m \033[1m SISTEMA DE AJUDA INTERATIVA PYHELP')
    print('\033[46m \033[34m~'*33)
    pergunta = ''
    while True:
        pergunta = str(input('\033[0m>> Função ou biblioteca: '))
        if pergunta.upper() == 'FIM':
            print('OBRIGADO POR USAR O PYHELP :)')
            break
        else:
            print(f'\033[30m** Escaneando função {pergunta}..** \n\033[42m')
            sleep(1)
            help(pergunta)

sistema()
  