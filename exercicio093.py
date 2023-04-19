# CRIE UM PROGRAMA QUE LEIA: NOME, IDADE, SEXO DE VÁRIAS PESSOAS, GUARDANDO OS DADOS DE CADA PESSOA EM UM DICIONÁRIO
# E TODOS OS DICIONÁIOS EM UMA LISTA, NO FINAL, MOSTRE:
# QUANTAS PESSOAS FORAM CADASTRADAS
# A MÉDIA DE IDADE DO GRUPO
# UMA LISTA SÓ COM MULHERES
# UMA LISTA COM TODAS AS PESSOAS COM IDADE ACIMA DA MÉDIA. #

dados = {}
cont = 0
mulheres = []
todos_os_dados = []
idade = []
while True:
    dados['nome'] = str(input('Nome: '))
    cont += 1
    dados['idade'] = int(input('Idade: '))
    idade.append(dados['idade'])
    media = sum(idade) / cont
    dados['sexo'] = str(input('Sexo [M ou F]: ')).upper()
    if dados['sexo'] == 'F':
        mulheres.append(dados["nome"])
    todos_os_dados.append(dados.copy())
    perg = str(input('Deseja continuar? s/n: '))

    if perg in 'Nn':
        break
print('='*50)
print(f'> Pessoas cadastradas: {cont}')
print(f'> Média de idade do Grupo: {media}')
print(f'> Mulheres cadastradas: ', end=' ')
for nomes in mulheres:
    print(f'{nomes}', end=' ')
print('\n > Pessoas com idade acima da média: ')

for pessoas in todos_os_dados:
    if pessoas['idade'] >= media:
        for keys, values in pessoas.items():
            print(f' ** {keys} = {values}* **', end=' ')



