print('NUMEROS PRIMOS')
num = int(input('Digite um numero para saber se ele é primo:'))
cont = 0
for c in range(1, num+1):
    if num % c == 0:
      print('\033[31m {}'.format(c, num), end =' ')
      cont += 1
    else:
        print('\033[32m {}'.format(c), end = ' ')
if cont == 2:
    print('\033[39m \n O numero foi divisível {} vezes, por isso ele é primo'.format(cont))
elif cont > 2:
    print('\033[34m \n O numero foi divisível {} vezes, por isso ele não é primo'.format(cont))




