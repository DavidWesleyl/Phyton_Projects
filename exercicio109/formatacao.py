def metade(valor=0, sit=False):
    metade = valor / 2
    return formatacao(metade) if sit is True else float(metade)


def dobro(valor=0, sit=False):
    dobro = valor * 2
    return formatacao(dobro) if sit is True else float(dobro)


def aumento(valor=0, porcentagem=0, sit=False):
    aumento = (valor/100 * porcentagem/1) + valor
    return formatacao(aumento) if sit is True else float(aumento)

def reducao(valor=0, reduc=0, sit=False):
    reducao = valor - (valor/100 * reduc/1)
    return formatacao(reducao) if sit is True else float(reducao)

def formatacao(valor=0):
    cifra = 'R$'
    return f"{cifra} {valor:.2f}".replace('.', ',')


