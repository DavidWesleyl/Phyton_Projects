''' ELABORE UM PROGRAMA QUE CALCULA O VALOR A SER PAGO POR UM PRODUTO. CONSIDEARANDO SEU PREÇO NORMAL E CONDIÇÕES
DE PAGAMETO '''
# À VISTA: DINEHIRO/CHEQUE 10% DE DESCONTO
# À VISTA NO CARTÃO: 5% DE DESCONTO
# EM ATÉ 2X NO CARTÃO: PREÇO NORMAL
# 3X OU MAIS NO CARTÃO: 20% DE JUROS



print('=================== PLACE DAVID MARKET ======================')
valor = float(input('Digite o valor a ser pago: R$'))
print('Escolha a opção de pagamento')
print('=-'*50)
print('* Dinheiro ou Cheque: [ Digite 1 ]')
print('    ')
print('* À vista no cartão: [ Digite 2 ]')
print('    ')
print('* Em até 2x no cartão de crédito: [ Digite 3 ]')
print('    ')
print('* Em 3x ou mais, no cartão: [ Digite 4 ]')
print('    ')

pergunta = int(input('Digite apenas números:'))

din = valor - (valor*10/100)
car = valor - (valor*5/100)
total = valor + (valor*20/100)


if pergunta == 1:
    print('O produto com valor {:.2f}, sairá por {:.2f}, com 10% de desconto'.format(valor, valor - valor * (10/100))) #OK
elif pergunta == 2:
    print('O produto {:.2f}, sairá por {:.2f}, com 5% de desconto'.format(valor, valor - valor * (5/100))) #OK
elif pergunta == 3:
    print('O produto sairá pelo preço normal R$ {:.2f} em até 2X'.format(valor)) #OK
elif pergunta == 4:
    ask = int(input('Em quantas vezes você quer parcelar?')) #10
    if ask > 3:
        print('O valor do produto R$ {:.2f}, ficará por {}x de R${:.2f}'.format(valor, ask, valor/ask + (valor/ask) * 20/100)) #ok
        print('Ficando no valor total de R$ {:.2f}'.format(valor + valor * (20/100)), end= ' ')
        print('Com 20% de Juros!')



















