# FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA CONTADOR() QUE RECEBA TRÊS PARAMETROS
# INICIO, FIM E PASSO E REALIZE A CONTAGEM. SEU PROGRAMA TEM QUE REALIZAR TRÊS CONTAGENS ATRAVES DA FUNÇÃO CRIADA
# DE 1 ATÉ 10, DE 1 EM 1
# DE 10 ATÉ 0, DE 2 EM 2
# E UMA CONTAGEM PERSONALIZADA PERGUNTANDO: O INICIO,O FIM E O PASSO. #
from time import sleep


def primeiro_contador():
    for valores in range(1, 11, 1):
        print(f'{valores}', end=' ')
        sleep(0.5)


def segundo_contador():
    for valores in range(10, -1, -2):
        print(f'{valores}', end=' ')
        sleep(0.5)


def terceio_contador():
    inicio = int(input('Digite o inicio: '))
    fim = int(input('Digite o fim: '))
    passo = int(input('Digite o passo: '))

    if passo == 0:
        passo = 1

    if passo < 0:
        passo = abs(passo)

    if inicio < fim:
        for valores in range(inicio, fim, passo):
            print(f'{valores}', end=' ')
            sleep(0.5)

    if inicio > fim:
        for valores in range(inicio, fim-1, -passo):
            print(f'{valores}', end=' ')
            sleep(0.5)



primeiro_contador()
print(' ')
segundo_contador()
print(' ')
terceio_contador()