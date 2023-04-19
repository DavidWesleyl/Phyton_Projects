#LEIA 6 NUMEROS INTEIROS E SOME APENAS OS PARES
soma = 0
cont = 0
for p in range(1, 7):
    num = int(input('Digite o {}º numero:'.format(p)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Foram digitados {} numeros pares'.format(cont))
print('E a soma deles é: {}'.format(soma))




