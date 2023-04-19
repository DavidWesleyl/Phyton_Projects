#RADAR ELETRÔNICO

velocidade = float(input('Em que velocidade você estava? (Digite apenas números)'))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print('Você excedeu o limite de velocidade que é 80KM/H')
    print('De acordo com a Lei estadual Nª 500 e blau, você deverá pagar uma multa de R$ 7,00 por KM ultrapassado')
    print('Totalizando R$: {:.2f}'.format(multa))

else: print('Dirija com cuidado, bom dia!')
