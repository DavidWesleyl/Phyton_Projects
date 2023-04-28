def metade(valor=0):
    metade = valor / 2
    return formatacao(metade)


def dobro(valor=0):
    dobro = valor * 2
    return formatacao(dobro)


def aumento(valor=0, porcentagem=0):
    aumento = (valor/100 * porcentagem/1) + valor
    return formatacao(aumento)

def reducao(valor=0, reduc=0):
    reducao = valor - (valor/100 * reduc/1)
    return formatacao(reducao)

def formatacao(valor=0):
    cifra = 'R$'
    return f"{cifra} {valor:.2f}".replace('.', ',')


