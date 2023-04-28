def metade(valor=0):
    valor = valor / 2
    return f"{valor:.2f}"


def dobro(valor=0):
    valor = valor * 2
    return f"{valor:.2f}"


def aumento(valor=0, porcentagem=0):
    aumento = (valor/100 * porcentagem/1) + valor
    return f"{aumento:.2f}"

def reducao(valor=0, reduc=0):
    reducao = valor - (valor/100 * reduc/1)
    return f"{reducao:.2f}"



