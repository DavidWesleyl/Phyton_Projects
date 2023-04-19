# FAÇA UM PROGRAMA QUE AJUDE O USUÁRIO A CRIAR PALPITES DA MEGA SENA. O PROGRAMA VAI PERGUNTAR :
# QUANTOS JOGOS SERÃO GERADOS E VAI SORTEAR 6 NÚMEROS ENTRE 1 E 60 PARA CADA JOGO, CADASTRANDO TUDO EM UMA LISTA #
from random import sample

for valores in range(1):
    num = int(input('Quantos números você quer gerar? '))
    for numeros in range(num):
        print(sample(range(1, 60), 6))




