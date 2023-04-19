#CONDIÇÃO DE EXISTENCIA DE  UM TRIANGULO

#FÓRMULA:

#A + B > C
#B + C > A
#C + A > B

a = float(input('Digite o primeiro lado do triangulo'))
b = float(input('Digite o segundo lado do triangulo'))
c = float(input('Digite o terceiro lado do triangulo'))

if a < b+c and b < a+c and c < b+a:
    print('Os seguimentos acima PODEM formar um triangulo')
else: print('Os seguimentos acima NÃO podem formar um triangulo')
