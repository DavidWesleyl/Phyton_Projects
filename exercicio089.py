# FAÇA UM PROGRAMA QUE LEIA O NOME E A MÉDIA DE UM ALUNO E GUARDE EM UM DICIONÁRIO. NO FINAL, MOSTRE:
# A SITUAÇÃO SE O ALUNO ESTÁ OU NÃO APROVADO! MÉDIA 7, E EXIBA NA TELA #

aluno = dict()

for dados in range(1):
    aluno['nome'] = str(input('Nome do aluno: '))
    aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
    if aluno['media'] >= 7:
        print(f'** Com a média de {aluno["media"]} o aluno(a) {aluno["nome"]} está APROVADO, PARABÉNS E OBRIGADO POR NÃO DESISTIR!!')
    else:
        print(f'** Com a média de {aluno["media"]} o aluno(a) {aluno["nome"]} está REPROVADO.. Tente novamente, não desista.')
