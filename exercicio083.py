# FAÇA UM PROGRAMA QUE LEIA O NOME E PESO DE VÁRIAS PESSOAS, GUARDANDO TUDO EM UMA LISTA:
# NO FINAL MOSTRE:
# A) QUANTAS PESSOAS FORAM CADASTRADAS
# B) UM LISTAGEM COM AS PESSOAS MAIS PESADAS
# C) UMA LISTAGEM COM AS PESSOAS MAIS LEVES

pessoas = []
dados = []
contador = 0
maior = menor = 0

while True:
    pessoas.append(str(input('Nome: ')))
    contador += 1
    pessoas.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < maior:
            menor = pessoas[1]
    dados.append(pessoas[:])
    pessoas.clear()

    perg = str(input('Continue? s / n: '))
    if perg in 'Nn':
        break

print('='*40)
print(f'Total de pessoas cadatradas: {contador}')

print(f'O maior peso lido foi {maior} de: ')

for pessoas in dados:
    if pessoas[1] == maior:
        print(f'>> [ {pessoas[0]} ]')

print(f'O menor peso lido foi {menor} de: ')
for pessoas in dados:
    if pessoas[1] == menor:
        print(f'>> [ {pessoas[0]} ]')




