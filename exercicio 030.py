#CUSTO DA VIAGEM

distancia = float(input('\033[0:30m Quantos KM em distância? (Digite apenas números):'))

d1 = distancia * 0.50
d2 = distancia * 0.45

if distancia <= 200:
    print('O valor da passagem será R$ {:.2f}'.format(d1))
else: print('O valor da passagem será {:.2f}'.format(d2))
