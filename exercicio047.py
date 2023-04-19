#A SOMA ENTRE NUMEROS IMPARES DIVISIVEIS POR 3, DE 1 A 500
soma_impares = 0
for impares in range(1, 500,2):
    if impares % 3 == 0:
        soma_impares += impares
        print(impares)
print('A soma dos numeros é {}'.format(soma_impares))