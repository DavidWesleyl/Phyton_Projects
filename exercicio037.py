#ESCREVA DOIS NUMEROS E MOSTRE QUAL O MAIOR E O MENOR. OU SE NÃO EXISTE MAIOR, POR SEREM IGUAIS

print('QUAL O MAIOR NUMERO?')
numero1 = int(input('Digite um numero'))
numero2 = int(input('Digite o segundo numero'))

if numero1 > numero2:
    print('O numero {} é maior que {}'.format(numero1, numero2))

elif numero2 > numero1:
    print('O numero {} é maior que {}'.format(numero2, numero1))

elif numero1 == numero2:
    print('Não existe número maior, pois os valores são iguais!')
