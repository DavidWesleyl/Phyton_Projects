# REESCREVA AFUNÇÃO LEIAINT() QUE FIZEMOS NO DESAFIO 104, INCLUINDO AGORA A POSSIBILIDADE DA DIGITAÇÃO DE UM
# NUMERO INVÁLIDO. APROVEITE E TAMBÉM CRIE UMA FUNÇÃO LEIAFLOAT() COM  MESMA FUNCIONALIDADE #

def leia_inteiro():
    while True:
        try:
            inteiro = int(input('Digite um numero inteiro: '))
            return inteiro
        except ValueError :
            print('\033[31mErro! Digite um número inteiro válido!\033[m')
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não digitar o valor!\033[m')
            return 0


def leia_float():
    while True:
        try:
            real = float(input('Digite um número real: '))
            return real
        except ValueError:
            print('\033[31mErro! Digite um númeor real válido!\033[m')
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não digitar o valor!\033[m')
            return 0


valor1 = leia_inteiro()
valor2 = leia_float()

print(f'>> O número inteiro digitado foi {valor1} e o numero real digitado foi {valor2}')