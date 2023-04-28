# FAÇA UM PROGRAMA QUE TENHAA UM FUNÇÃO CHAMADA NOTAS() QUE PODE RECEBER VÁRIAS NOTAS DE ALUNOS E VAI
# RETORNAR UM DICIONÁRIO COM AS SEGUINTES INFORMAÇÕES: - A QUANTIDADE DE NOTAS / A MAIOR NOTA / A MENOR NOTA /
# A MÉDIA DA TURMA / A  SITUAÇÃO(OPCIONAL). ADICIONE TAMBÉM AS DOCSTRINGS DA FUNÇÃO #


def notas(* valores, situacao=False):
    """
     -> BOLETIM
    :param valores: ** Recebe os valoresdas notas;
    :param situacao: ** Vai mostrar se a situação do aluno é boa ou ruim **
    :return: Vai mostrar o boletim com ou sem a situação
    """
    media = sum(valores) / len(valores)
    if situacao:
        if media < 6:
            situacao = 'RUIM'
        if media >=  6 and media < 7:
            situcao = 'BOA'
        if media > 7:
            situacao = 'EXCELENTE'

        boletim = {'Total': len(valores),
                   'Maior': max(valores),
                   'Menor': min(valores),
                   'Media': media,
                   'Situacao': situacao
                    }
        return boletim
    else:
        boletim = {'Total': len(valores),
                   'Maior': max(valores),
                   'Menor': min(valores),
                   'Media': media,
                   }
        return boletim



n = notas(5.5, 2.5, 1.5)
help(notas)
