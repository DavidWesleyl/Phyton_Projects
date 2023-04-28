# CRIE UM, PEQUENO SISTEMA MODULARIZADO QUE PERMIE CADASTRAR PESSOAS PLEO NOME E IDADE EM UM ARQUIVO DE
# TEXTO SIMPLES. O SISTEM SÓ VAI TER 2 OPÇÕES: CADASTRAR UMA NOVA PESSOA E LISTAR TODAS AS PESSOAS CADASTRADAS #

from exercicio115.bilbioteca.interface import *
from exercicio115.bilbioteca.arquivos import *
from time import sleep
arquivo = 'lista_de_pessoas.txt'

if not Arquivo_existe(arquivo):
    Criar_documento(arquivo)

while True:

        interface('\033[33m SISTEMA DE CADASTRO V1.0 \033[m')
        opcoes(['Ver usuários cadastrados', 'Cadastrar usuário', 'Sair'])
        print('-' * 45)
        resposta = int(input('Sua opção: '))

        if resposta == 1:
            Ler_arquivo(arquivo)
            sleep(1)

        elif resposta == 2:

            interface('\033[33m NOVO CADASTRO \033[m')
            nome = str(input('Digite o nome: '))
            idade = int(input('Digite a idade: '))
            Cadastrar_pessoas(arquivo, nome, idade)

        elif resposta == 3:

            interface('\033[35mSaindo do sistema aguarde..\033[m')
            sleep(2)
            break

        else:
            print('\033[31mErro! Digite uma opção válida\033[m')







