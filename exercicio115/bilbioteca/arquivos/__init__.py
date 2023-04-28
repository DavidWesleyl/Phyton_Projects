from exercicio115.bilbioteca.interface import *


def Arquivo_existe(arquivo):  # SE O ARQUIVO EXISTE #
    try:
        arquivo = open(arquivo, 'rt')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True


def Criar_documento(arquivo):  # CRIAR DOCUMENTO TXT #
    try:
        arquivo = open(arquivo, 'wt+')
    except:
        print('Houve ym erro ao criar o arquivo')
    else:
        print(f'Arquivo {arquivo} criado com sucesso.')


def Ler_arquivo(nome): # MOSTRAR PESSOAS CADASTRADAS #

    try:
        mensagem = open(nome, 'rt', encoding='utf-8')
    except:
        print('Houve um erro ao ler o arquivo')
    else:
        interface('\033[36mPESSOAS CADASTRADAS\033[m'.center(45))
        print(mensagem.read())
    finally:
        mensagem.close()


def Cadastrar_pessoas(arquivo, nome='Desconhecido', idade=0): # CADSTRAR PESSOAS #
    try:
        msg = open(arquivo, 'at', encoding='utf-8') # ENCODING UTF-8 SERVE PARA CORRIGIR BUGS DE ACENTO #
    except:
        print('Houve um erro na abertura do arquivo.')
    else:
        try:
            msg.write(f'Nome: \033[36m{nome}\033[m; Idade: \033[36m{idade}\033[m \n')

        except:
            print(f'Houve um erro ao cadastrar o usuário, mas não se preocupe, iremos resolver o mais rápido possível!')

        else:
            print(f'** Novo registro de \033[36m{nome}\033[m adicionado **')
            msg.close()








