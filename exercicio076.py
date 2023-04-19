# CRIE UM PROGRAMA QUE TENHA VÁRIAS TUPLAS (NÃO USAR ACENTOS), DEPOIS DISSO, VOCÊ DEVE MOSTRAR
# PARA CADA PALAVRA QUAIS SÃO SUAS VOGAIS #


tupla = ('aprender', 'programação', 'phyton', 'curso', 'programador', 'futuro', 'automação',
         'big data', 'data science', 'back-end', 'meta', 'gamer', 'nova era')
for listagem in tupla:
    print(f'\n Na palavra {listagem.upper()} temos as vogais:', end=  ' ')
    for vog in listagem:
        if vog in 'aeiou'.lower():
            print(vog, end= ' ')