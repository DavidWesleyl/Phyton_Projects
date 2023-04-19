# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar: O valor da casa, o salário do comprador e em quantos anos ele vai pagar.

# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário
# Ou então o emprestimo será NEGATIVADO

valor = float(input('Qual o valor da casa?'))
salario = float(input('Quanto você ganha?'))
tempo = int(input('Em quanto tempo você quer pagar?'))
prestação = valor / (tempo*12)
minimo = (30/100) * (salario/1)
#print('30% do salário: {}'.format(sal1))
#print('Parcelas R$ {:.2f}'.format(prestação))
print('Para pagar uma casa de {} Reais em {} ano(s), a prestação será {:.2f}'.format(valor, tempo, prestação))
print('Disponibilizamos o limite de acordo com 30% do seu salário, sem exceder')
print('Verificamos que 30% do seu ganho é de R$ {}'.format(minimo))
if prestação <= minimo:
    print('O Empréstimo pode ser concedido! :)')
else: print('infelizmente você não atingiu os requisitos :(')

