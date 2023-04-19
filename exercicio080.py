# CRIE UM PROGRAMA QUE VAI LER VÁRIOS VALORES E COLOCÁ-LOS EM UMA LISTA, DEPOIS DISSO, MOSTRE:
# A - QUANTOS NÚMEROS FORAM DIGITADOS
# B - A LISTA DE VALORES DE FORMA ORDENADA DECRESCENTE
# C - SE O VALOR 5 ESTÁ NA LISTA #

lista = []
cont = 0

while True:
    num = int(input('>> Digite um valor para adicionar a lista: '))
    cont += 1
    lista.append(num)
    lista.sort(reverse=True)
    pergunta = int(input('# Deseja continuar? [ SIM - press (1) | NÃO - press (2) ]: '))
    if pergunta == 2:
        break
    if pergunta > 2:
        print(f'# OPÇÃO INVÁLIDA! #')
        pergunta = int(input('# Deseja continuar? [ SIM - press (1) | NÃO - press (2) ]: '))
        if pergunta == 2:
            break
print('-'*50)
if 5 in lista:
    print('- O Número 5 foi digitado!')
else:
    print('- O número 5 não foi digitado!')
print(f'- A lista de forma decrescente é {lista}')
print(f'- Ao todo foram digitados {cont} números')

