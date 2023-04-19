import random

nome1 = input('Primeiro Aluno')
nome2 = input('Segundo Aluno')
nome3 = input('Terceiro Aluno')
nome4 = input('Quarto Aluno')

list = random.choice([nome1, nome2, nome3, nome4])

print('O Aluno escolhido, é: {}'.format(list))