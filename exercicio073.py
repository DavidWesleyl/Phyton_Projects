#  CRIE UM PROGRAMA QUE VAI GERAR CINCO NÚMEROS ALEATÓRIOS E COLOCAR EM UMA TUPLA
#  NO FINAL MOSTRE A LISTAGEM DOS NUMERO E QUAL FOI O MENOR E O MAIOR NÚMERO QUE ESTÃO NA TUPLA #
from random import randint
from time import sleep

a = randint(1, 5)
b = randint(5, 10)
c = randint(10, 15)
d = randint(15, 20)
e = randint(20, 30)
list = (a, b, c, d, e)

print("Gerando números..")
sleep(2)
print(list)

# MAIOR VALOR #

if a > b and a > c and a > d and a > e:
    print(f'O maior valor lido, foi {a}')
elif b > a and b > c and b > d and b > d:
    print(f'O maior valor lido, foi foi {b}')
elif c > a and c > b and c > d and c > e:
    print(f'O maior valor lido, foi {c}')
elif d > a and d > b and d > c and d > e:
    print(f'O maior valor lido, foi {d}')
elif e > a and e > b and e > c and e > d:
    print(f'O maior valor lido, foi {e}')

if a < b and a < c and a < d and a < e:
    print(f'O menor valor lido, foi {a}')
elif b < a and b < c and b < d and b < e:
    print(f'O menor valor lido, foi {b}')
elif c < a and c < b and c < d and c < e:
    print(f'O menor valor lido, foi {c}')
elif e < a and e < b and e < c and e < d:
    print(f'O menor valor lido, foi {e}')

