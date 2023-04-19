#FAÇA UM PROGRAMA QUE LEIA A DATA DE NASCIMENTO DE 7 PESSOAS E DIGA QUANTAS DELAS SÃO MAIORES E MENOS DE IDADE!
#CONSIDERE A MAIORIDADE 21 ANOS.
from datetime import date
data = date.today().year
cont1 = 0
cont2 = 0
cont3 = 0

for p in range(1, 8):
    nasc = int(input('Digite seu ano de nascimento:'))
    cont3 += 1
    ano = data - nasc
    if ano >= 21:
        cont1 += 1
    if ano < 21:
        cont2 += 1
print('De {} pessoas lidas'.format(cont3))
print('{} são maiores de idade'.format(cont1))
print('{} são menores de idade'.format(cont2))




