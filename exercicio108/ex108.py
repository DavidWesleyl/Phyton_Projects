# ADAPTE O CÓDIGO DO DESAFIO 107 CRIANDO UMA FUNÇÃO CHAMADA MOEDA() QUE CONSIGA MOSTRAR OS VALORES
# COMO UM VALOR MONETÁRIO FORMATADO #

from exercicio108 import format

numero = float(input('Digite o preço R$: '))

print(f'A metade de {format.formatacao (numero)} é {format.metade(numero)}')
print(f'O dobro de {format.formatacao(numero)} é {format.dobro(numero)}')
print(f'O valor {format.formatacao(numero)} com 10% de aumento será {format.aumento(numero, 10)}')
print(f'Reduzindo 14% de {format.formatacao(numero)} o resultado será {format.reducao(numero, 14)}')