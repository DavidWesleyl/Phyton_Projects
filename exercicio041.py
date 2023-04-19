#CONDIÇÃO DE EXISTENCIA DE UM TRIANGULO (DIZER SE O TRIANGULO É ISOSCELES, EQUILÁTERO, ESCALENO)
#FORMULA
# A < B+C
# B < C+A
# C < A+B

# EQUILÁTERO - TODOS OS LADOS IGUAIS
# ISÓSCELES - DOIS IGUAIS E UM DIFERENTE
# ESCALENO - TODOS DIFERENTES

a = float(input('Digite o primeiro lado'))
b = float(input('Digite o segundo lado'))
c = float(input('Digite o terceiro lado'))

if a < b+c and b < c+a and c < a+b:
    print('Os segmentos formam um triangulo:', end=' ')
    if a == b == c:
        print('EQUILÁTERO')
    if a != b != c != a:
        print('ESCALENO')
    if a == b != c:
        print('ISÓSCELES')

else: print('Os segmentos não formam um triangulo')








