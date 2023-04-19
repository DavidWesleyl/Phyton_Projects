# LER 4 PESSOAS E MOSTRAR:
# NOME DO HOMEM MAIS VELHO, QUANTAS MULHERES TEM MENOS DE 20 ANOS E  MÉDIA DE IDADE #

contf = maior = cont = soma = menor = 0
maior_idade = str

for i in range(1, 5):
    sexo = int(input('Digite seu sexo = 1 - MASCULINO  2 - FEMININO:'))
    nome = str(input('Digite seu nome:')).upper()
    idade = int(input('Digite sua idade:  '))
    soma += idade
    media = soma / 4
    print('-='*25)

    if sexo == 2 and idade < 20:
        contf += 1

    if sexo == 1 and idade > maior:
        maior = idade
        maior_idade = nome

print('-='*25)
print('O total de mulheres com menos de 20 anos, é {}'.format(contf))
print('O nome do homem mais velho, é {}'.format(maior_idade))
print('A média de idade do grupo,  {}'.format(media))
