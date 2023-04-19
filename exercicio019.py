import random

n1 = input('Primeiro ALuno')
n2 = input('Segundo Aluno')
n3 = input('Terceiro Aluno')
n4 = input('Quarto Aluno')

l = [n1, n2, n3, n4]
random.shuffle(l)
print('A ordem da apresentação, será')
print(l)
