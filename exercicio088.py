# CRIE UM POGRAMA QUE LEIA NOME E DUAS NOTAS DE VÁRIOS ALUNOS E GUARDE TUDO EM UMA LISTA COMPOSTA.
# NO FINAL, MOSTRE O BOLETIM CONTENDO A MÉDIA DE CADA UM E
# PERMITA QUE O USUÁRIO POSSA MOSTRAR AS NOTAS DE CADA ALUNO INDIVIDUALMETE #

dados = []
lista = []

while True:
    nome = str(input('Nome: '))
    lista.append(nome)
    n1 = float(input('1ª Nota: '))
    lista.append(n1)
    n2 = float(input('2ª Nota: '))
    lista.append(n2)
    media = (n1 + n2) / 2
    lista.append(media)
    dados.append(lista[:])
    lista.clear()

    perg = str(input('Continue? s / n: '))
    if perg in 'Nn':
        break
print('='*50)

for posicao, valor in enumerate(dados):
    print(f'POSIÇÃO: {posicao} | ALUNO(A): {valor[0]} | MÉDIA: {valor[3]}')
    print('-'*50)

while True:
    pergunta = int(input('Qual aluno deseja ver de forma individual? [ Pressione 999 para encerrar ]'))
    if pergunta != 999:
        print(f'>> Aluno {dados[pergunta][0]}: Primeira Nota: {dados[pergunta][1]}. Segunda nota: {dados[pergunta][2]}')
        print('-' * 50)
    else:
        break


