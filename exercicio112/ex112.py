# DENTO DO PACCOTE UTILIDADES CEV QUE CRIAMOS NO DESAFIO 111 TEMOS UM MÓDULO CHAMADO DADOS. CRIE UMA
# FUNÇÃO CHAMADA LEIADINHIEIRO() QUE SEJA CAPAZ DE FUNCIONAR COO A FUNÇÃO INPUT() MAS COM UMA VALIDAÇÃO DE DADOS
# PARA ACEITAR APENAS VALORES QUE SEJAM MOENTÁRIOS#
from exercicio112.utilidadecev import dados, moedas

valor = dados.leiadinheiro('Digite o preço R$: ')
moedas.resumo(valor, 80, 35)
