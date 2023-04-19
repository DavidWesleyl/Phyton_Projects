#REFAZENDO OS 10 PRIMEIROS TERMOS DE UMA PROGRESSÃO ARITMÉTICA, COM WHILE

'''t1 = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a razão:'))
pro = t1 + (11-1) * razao
for c in range(t1, pro, razao):
    print(c, end=' - ')'''

primeiro_termo = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a razão: '))
cont = 1
progress = primeiro_termo
while cont <= 10:
    print('{} -'.format(progress), end=' ')
    cont += 1
    progress += razao
print('FIM', end=' ')








