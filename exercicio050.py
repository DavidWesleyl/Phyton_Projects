#PROGRESSÃO ARITMÉTICA

termo = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a razão'))
res = termo + (11 -1) * razao
for prog in range(termo, res, razao):
    print(prog, end = ' - ')
print('Acabou!', end= ' ')
