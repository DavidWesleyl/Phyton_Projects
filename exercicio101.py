# CRIE UM PROGRAMA QUE TENHA UMA FUNÇÃO FATORIAL() QUE RECEBA DOIS PARÂMETROS: O PRIMEIRO, QUE INDIQUE O NUMERO
# A CALCULAR, E OUTRO CHAMADO "SHOW" QUE SERÁ UM VALOR LÓGICO (OPCIONAL) INDICANDO SE SERÁ OU NÃO MOSTRADO NA TELA
# O PROCESSO DO FATORIAL #
import math


def fatorial(valor, show=False):
    """
     > Calcula o fatorial de um número
    :param valor: É O VALOR DO FATORIAL QUE VAI SER CALCULADO;
    :param show: É O VALOR OPCIONAL QUE MOSTRA OU NÃO O CALCULO;
    :return: É O VALOR DO FATORIAL (valor) JÁ CALCULADO
    """
    print('-'*25)
    fat = math.factorial(valor)
    if show:
        for c in range(valor, 0, -1):
            print(f'{c} *', end=' ')
        return fat
    else:
        return fat


# PROGRAMA PRINCIPAL #

print(fatorial(5, show=True))

#help(fatorial)





