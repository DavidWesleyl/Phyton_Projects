# DIGITE UM NUMERO QUALQUER E MOSTRE O FATORIAL

f = 1
num = int(input('Digite um numero:'))
for i in range(num, 0, -1):
    f = f * i
print('{}! é {}'.format(num, f))






