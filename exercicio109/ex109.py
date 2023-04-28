# MODIQFIQUE AS FUNÇÕES QUE FORAM CRIADAS NO DESAFIO 107 PARA QUE ELAS POSSAM RECEBER UM PARAMETRO A MAIS
# INFORMANDO SE O VALOR RETORNADO POR ELAS VAI SER OU NÃO FORMATADO PELA FUNCAO MOEDA() DESENOLVIDA NO DESAFIO 108#

from exercicio109 import formatacao

numero = float(input('Digite o preço R$: '))

print(f'A metade de {formatacao.formatacao (numero)} é {formatacao.metade(numero, True)}')
print(f'O dobro de {formatacao.formatacao(numero)} é {formatacao.dobro(numero, True)}')
print(f'O valor {formatacao.formatacao(numero)} com 10% de aumento será {formatacao.aumento(numero, 10, True)}')
print(f'Reduzindo 14% de {formatacao.formatacao(numero)} o resultado será {formatacao.reducao(numero, 14, True)}')