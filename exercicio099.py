# FAÇA UM PROGRAMA QUE TENHA UMA LISTA CHAMADA NUMEROS E DUAS FUNÇÕES CHAMADAS: SORTEIA E SOMA PARES
# A PRIMEIRA FUNÇÃO VAI SORTEAR 5 NUMEROS E VAI COLOCA-LOS DENTRO DA LISTA E A SEGUNDA FUNÇÃO VAI MOSTRAR A SOMA ENTRE
# TODOS OS VALORES PARES SORTEADOS PELA FUNÇÃO ANTERIOR #


from random import randint

pares = []


def numeros_sorteados():
    print(f'Sorteando 5 numeros..')
    for valores in range(5):
        sorteio = randint(1, 20)
        if sorteio % 2 == 0:
            pares.append(sorteio)
        print(f'{sorteio}', end=' ')
    print(f'\nNumeros pares: {pares}')
    print(f'A soma dos pares é {sum(pares)}')


numeros_sorteados()