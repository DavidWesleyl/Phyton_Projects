# FAÇA UM PROGRAMA QUE TENHA A FUNÇÃO PRINT() QUE RECEBE UM TEXTO QUALQUER COMO PARÂMENTRO E MOSTRE UMA MENSAGEM
# COM TAMANHO ADAPTÁVEL. EX: "OLÁ, MUNDO" - OUTPUT ------------
#                                                   OLÁ, MUNDO
#                                                 -------------#
def frases():
    for frase in range(3):
        palavras = str(input('Digite uma frase: '))
        print('-'*len(palavras))
        print(palavras)
        print('-'* len(palavras))

frases()