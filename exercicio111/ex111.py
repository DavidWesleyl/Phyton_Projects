# DENTRO DO PACOTE UTILIDADECEV QUE CRIAMOS NO DESAFIO 111 TEMOS UM MÓDULO CHAMADO DADOS(). CRIE UMA FUNÇÃO
# CHAMADA LEIADINHEIRO() QUE SEJA CAPAZ DE FUNCIONAR COMO A FUNÇÃO INPUT() MAS COM UMA VALIDAÇÃO DE DADOS
# PARA ACEITAR APENAS VALORES MONETÁRIOS. #

from exercicio111.utilidadecev import moedas
valor = float(input('Digite o valor R$: '))

moedas.resumo(valor, 80, 35)