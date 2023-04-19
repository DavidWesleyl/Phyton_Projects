#TODOS OS NUMEROS PARES ENTRE 1 E 50
cont = 0
print('Todos os numeros pares entre 1 e 50')
for pares in range(2, 51, 2):
    print(pares)
    cont+=1
print('\033[31m Ao todo foram contabilizados {} numeros pares, entre 1 e 50'.format(cont))