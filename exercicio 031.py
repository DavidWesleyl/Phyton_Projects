#LER TRÊS NÚMEROS E MOSTRAR QUAL É O MAIOR E O MENOR

a = int(input('Digite o primeiro número'))
b = int(input('Digite o segundo número'))
c = int(input('Digite o terceiro número'))

#MENOR

if a < b and a < c:
    print('O menor número é {}'.format(a))
if b < a and b < c:
    print('O menor número é {}'.format(b))
if c < a and c < b:
    print('O menor número é {}'.format(c))

#MAIOR

if a > b and a > c:
    print('O maior número é {}'.format(a))
if b > a and b > c:
    print('O maior número é {}'.format(b))
if c > a and c > b:
    print('O maior número é {}'.format(c))