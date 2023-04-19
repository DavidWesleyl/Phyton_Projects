# FAÇA UM PROGRAMA QUE LEIA O SEXO DE UMA PESSOA E DIGA SE É M OU F, SE FOR DIFERENTE DESCONSIDERE #
# E PERGUNTE ATÉ O USUÁRIO DIGITAR CERTO. #



gen = 0
while gen != 3:
    gen = int(input('Digite 1º para ( MASCULINO ) ou 2º para ( FEMININO ):'))
    print('-'*15, 'AGUARDE', '-'* 15)

    if gen == 1:
        print('Você escolheu o gênero MASCULINO...')
        break
    elif gen == 2:
        print('Você escolheu o gênero FEMININO...')
        break

while gen >= 3:

    print(' >> OPÇÃO INVÁLIDA')
    print(' >> TENTE NOVAMENTE')
    print('-'*30)
    gen = int(input('Digite 1º para ( MASCULINO ) ou 2º para ( FEMININO ):'))

    if gen == 1:
        print('Você escolheu o gênero MASCULINO...')
        break
    elif gen == 2:
        print('Você escolheu o gênero FEMININO...')
        break









