# CRIE UM PROGRAMA QUE LEIA A IDADE E SEXO DE VÁRIAS PESSOAS. A CADA PESSOA CADASTRADA
# O PROGRAMA DEVERÁ PERGUNTAR SE QUER OU NÃO CONTIUAR. NO FINAL, MOSTRE:
# QUANTAS PESSOAS TEM MAIS DE 18 ANOS;
# QUANTOS HOMENS FORAM CADASTRADOS;
# QUANTAS MULHERES TEM MENOS DE 20 ANOS. #



cont = cont1 = cont2 = 0

while True:

    print('='*35)
    print('CADASTRE UMA PESSOA')
    print('='*35)

    idade = int(input('Digite sua idade:'))
    if idade > 18:
        cont += 1
    sexo = int(input('Você é Homem ou Mulher? M > press { 1 } | F press > { 2 }:'))
    if sexo == 1:
        cont1 += 1

    if sexo == 2 and idade < 20:
        cont2 += 1
    opcao = int(input('quer continuar:? (SIM - 1 | NÃO - 2):'))

    if opcao == 2:
        break

print('.'*40)
print('Analisando.. ')
print(f' Pessoas com mais de 18: {cont}.\n Total de Homens: {cont1}.\n Total de mulheres com menos de 20 Anos: {cont2}.')