#TABUADA

tabuada = int(input('Digite um numero para ver a tabuada'))
for tab in range(1, 11):
    resultado = tabuada * tab
    print('\033[32m{} x {} = {}'.format(tabuada, tab, resultado))