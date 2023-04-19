# Faça um programa que leia um numero X inteiro qualquer
# e mostre na tela os X primeiros elementos da sequencia fibonacci

# EX - 0 - 1 - 1 - 2 - 3 - 5 - 8 - 13 - 21

print('=-'*20)
print('SEQUÊNCIA FIBONACCI')
print('=-'*20)

num = int(input('Quantos termos você deseja ver?'))

def fibo(termo_1, termo_2):
    print(termo_1, termo_2, end=' ')
    for i in range(3, num+1):
        termo_3 = termo_1 + termo_2
        termo_1 = termo_2
        termo_2 = termo_3
        print(termo_3, end=' ')

x = 0
y = 1
fibo(x, y)