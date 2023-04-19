km = float(input('Quantos KM percorrido?'))
dias = float(input('Qual a quantidade de dias?'))

dias1 = dias * 60
kil = km * 0.15
total = dias1+kil


print('A quantidade total a pagar, será {}:'.format(total))