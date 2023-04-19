preço  = float(input('Digite o valor do produto'))

desconto = (5/100) * preço/1    #PORCENTAGEM
desconto1 = preço - desconto

print('\033[0:31m O valor do Produto {}, com desconto de 5%, será: {:.2f}'.format(preço, desconto1))




