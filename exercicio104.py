# CRIE UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA leiaInt() QUE VAI FUNCIONAR SEMELHANTE A FUNÇÃO INPUT()
# DO PHYTON, SÓ QUE FAZENDO A VALIDAÇÃO PARA ACEITAR APENAS UM VALOR NUMÉRICO #

def leiaInt(valor):
    while True:
        try:
            valor = int(input('\033[30m Digite um valor: '))
            if valor:
                valor = int(valor)
                return valor
        except:
            print(f'\033[31m Erro! Digite um número inteiro válido!')




num = leiaInt('Digite um valor: ')
print(f'Você digitou o valor {num}')