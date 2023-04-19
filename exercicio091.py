# CRIE UM PROGRAMA QUE LEIA O NOME, ANO DE NASCIMENTO E A CARTEIRA D TRABALHO E CADASTRE-OS(COM A IDADE) EM UM DICIONÁRIO.
# SE FOR ACASO A CTPS FOR DIFERENTE DE 0(ZERO), O DICIONÁRIO RECEBERÁ TAMBÉM O ANO DE CONTRATAÇÃO E O SALÁRIO. CALCULE E
# ACRESCNTE ALÉM DA IDADE, COM QUANTOS ANOS A PESSOA VAI SE APOSENTAR CONSIDERANTO 35 ANOS DE CONTRIBUIÇÃO. #


dados = dict()
ano_atual = 2023
for pessoas in range(1):
    dados['nome'] = str(input('Nome: ')).capitalize()
    dados['nascimento'] = int(input('Ano de nascimento: '))
    dados['CTPS'] = int(input('Nº da Carteira de Trabalho: [ 0 - não tem ]: '))
    if dados['CTPS'] == 0:
        print('  ======= DADOS PESSOAIS =======')
        print(f'** NOME: {dados["nome"]}')
        print(f'** IDADE: Neste ano você tem / irá fazer {(dados["nascimento"]) - ano_atual}')
        print(f'CTPS: não tem')
        break
    else:
        dados['contratação'] = int(input('Ano de contratação: '))
        dados['salário'] = float(input('salário: '))
        dados["aposentadoria"] = (dados["contratação"] - dados["nascimento"]) + 35

        print('  ======= DADOS PESSOAIS =======')
        print(f'    ** NOME: {dados["nome"]}')
        print(f'    ** IDADE: Neste ano você tem / irá fazer {ano_atual - dados["nascimento"]}')
        print(f'    ** ANO DE CONTRATAÇÃO: {dados["contratação"]}')
        print(f'    ** SALÁRIO: {dados["salário"]}')
        print(f'    ** DE ACORDO COM O CALENDÁRIO ATUAL VOCÊ IRÁ SE APOSENTAR COM {dados["aposentadoria"]} ANOS')

