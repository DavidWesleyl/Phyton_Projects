#Leitor de pesos #MAIOR E MENOR
maior = 0
menor = 0
for peso in range(1, 3+1):
    kg = float(input('Digite o peso da {}º pessoa:'.format(peso)))
    if kg > maior:
        maior = kg
    else:
        if kg < maior:
            menor = kg

print('O maior peso lido, foi {}kg'.format(maior))
print('O menor peso lido foi {}kg'.format(menor))










