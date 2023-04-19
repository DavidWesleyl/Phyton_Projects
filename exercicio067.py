# FAÇA UM PROGRAMA QUE JOGUE PAR OU IMPAR COM O COMPUTADOR. O
# JOGO SERÁ INTERROMPIDO QUANDO O JOGADOR PERDER!
# MOSTRANDO O TOTAL DE VITÓRIAS CONSECUTIVAS QUE ELE CONQUISTOU DURANTE O JOGO #
# O USUÁRIO IRÁ DIGITAR UM VALOR, E O COMPUTADOR OUTRO. A SOMA SERÁ PAR OU IMPAR E O VENCEDOR DECLARADO #


from random import randint
cont = 0
while True:
    print('='*35)
    print(' VAMOS JOGAR PAR OU ÍMPAR ')
    print('='*35)
    print(' ')

    tot = 0
    computer = randint(0, 10)
    user = int(input('Digite um número:'))
    perg = int(input('Você quer PAR OU ÍMPAR >> P press - { 1 } / I - press { 2 } << (?):'))
    total = computer + user
    print('-'*35)

    if perg == 1:
        print(f'** Você escolheu PAR **')
    if perg == 2:
        print(f'** Você escolheu ÍMPAR **')

    print(f'Você jogou {user} e O computador escolheu {computer}. O total é {total}')

    if total % 2 == 0 and perg == 1:
        print(f'>> O número {total} é PAR! <<')
        print('Você Venceu!!')
        cont += 1

    elif total % 1 == 0 and perg == 2:
        print(f' >> O número {total} é ÍMPAR <<')
        print('Você Venceu!!')
        cont += 1

    elif total % 2 == 0 and perg == 2:
        print(f'>> O número {total} é PAR! <<')
        print('Você Perdeu!!')

        break

    elif total % 1 == 0 and perg == 1:
        print(f'>> O número {total} é ÍMPAR <<')
        print('Você Perdeu!!')

        break
print('-'*35)
print(f'VOCÊ VENCEU {cont} VEZES!')










