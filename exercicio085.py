# CRIE UM PROGRAMA QUE CRIE UMA MATRIZ ( CUBO ) 3X3 E PREENCHA COM OS VALORES LIDOS PELO TECLADO
# NO FINAL MOSTRE A MATRIZ CORRETA COM A FORMATAÇÃO NA TELA. #

lista = []

for lado in range(3):
    for linha in range(3):
        valor = int(input(f'Digite um valor na posição [ {lado}, {linha} ]: '))
        lista.insert(0, valor)

print('='*40)
print(f'[{lista[8]}] [{lista[7]}] [{lista[6]}]')
print(f'[{lista[5]}] [{lista[4]}] [{lista[3]}]')
print(f'[{lista[2]}] [{lista[1]}] [{lista[0]}]')