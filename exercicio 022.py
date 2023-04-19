#Faça um programa que leia um número de 0 à 9999 e mostre na tela cada um dos dígitos separados
#Exemplo
#Digite um numero: 1834
#Unidade: 4
#Dezena: 3
#Cenena: 8
#Milhar: 1

numero = int(input('Digite um valor'))

uni = numero//1 % 10
dez = numero//10 % 10
cen = numero//100 % 10
milh = numero//1000 % 10

print('UNIDADE: {}'.format(uni))
print('DEZENA: {}'.format(dez))
print('CENTENA: {}'.format(cen))
print('MILHAR: {}'.format(milh))
