# CRIE UM PROGRAMA QUE TENHA UMA TUPLA TOTALMENTE PREENCHIDA  COM UMA CONTAGEM  POR EXTENSO
# DE 0 Á 20, SEU PROGRAMA DEVERÁ LER O NÚMERO E MOSTRA-LO POR EXTENSO (ESCRITO)#
# SE O VALOR DIGITADO FOR MAIOR QUE 20, PEÇA PRA DIGITAR NOVAMENTE!

n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
    'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
    'dezenove', 'vinte')

numero = int(input('Digite um número entre 0 e 20:'))

while True:
    if numero >= 21 or numero < 0:
        print('Opção inválida!')
        numero = int(input('Digite novamente:'))
    else:
        print(f'O número {numero} por extenso, é {n[numero].upper()}')
        break