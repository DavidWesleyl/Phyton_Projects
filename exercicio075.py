#CRIE UM PROGRAMA QUE TENHA UMA ÚNICA TUPLA COM NOMES DE PRODUTOS
# E SEUS RESPCTIVOS PREÇOS NA SEQUENCIA.
# NO FINAL MOSTRE UMA LISTAGEM DE PREÇOS ORGANIZADOS DE FORMA TABULAR #
from time import  sleep

produtos = ('Gabinete Gamer com rgb', '3,500', 'Monitor AOC curvado 27"', '1650,00', 'Kit Teclado + Mouse', '100,00',
            'Bola NBA', '160,00', 'Impressora HP Deskjet', '450,00', '')
print('-'*15, 'LISTAGEM DE PREÇOS', '-'*15)

print(produtos[0].upper(),'...................R$', produtos[1])
sleep(1)
print(produtos[2].upper(),'..................R$', produtos[3])
sleep(1)
print(produtos[4].upper(),'......................R$', produtos[5])
sleep(1)
print(produtos[6].upper(),'.................................R$', produtos[7])
sleep(1)
print(produtos[8].upper(),'....................R$', produtos[9])
sleep(1)

print('-'*55)
sleep(0.5)
