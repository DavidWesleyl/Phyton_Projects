# CRIE UM MÓDULO CHAMADO MOEDA.PY QUE TENHA AS FUNÇÕES INCORPORADAS AUMENTAR() DIMINNUI() DOBRO() E
# METADE(). FAÇA TAMBÉM UM PROGRAMA QUE IMIORTE E USE ALGUMAS DESSAS FUNÇÕES#
import moeda

from exercicio107 import *

numero = float(input('Digite o preço R$: '))

print(f'A metade de {numero} é {moeda.metade(numero)}')
print(f'O dobro de {numero} é {moeda.dobro(numero)}')
print(f'O valor {numero} com 10% de aumento será {moeda.aumento(numero, 10)}')
print(f'Reduzindo 14% de {numero} o resultado será {moeda.reducao(numero, 14)}')