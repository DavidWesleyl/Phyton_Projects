#numero binário
#Numeros binários são formados por 2 números: 0 e 1
#Exemplo

numero = int(input('Digite um número'))
print('''Escolha a converção
1 == BINÁRIO
2 == OCTAL
3 == HEXADECIMAL''')
op = int(input('Qual sua opção?'))

if op == 1:
    print('O numero {}, convertido para BINÁRIO, será: {}'.format(numero, bin(numero)[2:]))
elif op == 2:
    print('O número {}, convertido para OCTAL, será: {}'.format(numero, oct(numero)[2:]))
elif op == 3:
    print('O número {}, convertido para HEXADECIAL, será: {}'.format(numero, hex(numero)[2:]))
else: print('Opção inválida!')