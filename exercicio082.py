# CRIE UM PROGRAMA ONDE O USUÁRIO DIGITE UMA EXPESSÃO QUALQUER QUE USE PAÊNTESES, SEU APLICATIVO DEVERÁ ANALISAR
# SE A EXPRESSÃO ESTÁ COM OS PARENTESES ABERTOS E FECHADOS NA ORDEM CORRETA! #

expressao = str(input('Digite a expressão:  '))
cont = 0
lista = []

for simbolo in expressao:
    if simbolo == '(':
        cont += 1
    if simbolo == ')':
        cont -= 1
    if cont < 0:
        break
if cont == 0:
    print('A expressão está correta!')
else:
    print('A expressão está incorreta!')
