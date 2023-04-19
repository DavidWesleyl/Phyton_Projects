# SIMULADOR DE CAIXA ELETRÔNICO
# NOTAS DISPONÍVEIS: R$ 1, 10, 20, 50 #

print('-'*15, 'BANCO 24H', '-'*15)
print('Notas Disponíveis: R$ 1, 10, 20, 50')
print('-'*45)
valor = int(input('Digite o valor que você quer sacar:'))
total = valor
cedula = 50
cont = 0

while True:
    if total >= cedula:
        total -= cedula
        cont += 1
    else:
        print(f'Total de {cont} cédulas de {cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        cont = 0
        if total == 0:
            break






