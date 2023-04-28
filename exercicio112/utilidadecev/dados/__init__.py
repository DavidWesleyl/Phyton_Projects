def leiadinheiro(valor):

    '''

    :param valor: é o valor a ser passado como input!
    :return: vai retornar o float do valor que vai ser passao em perg
    '''

    valido = False
    while not valido:  # Enquanto o número não for válido #

        perg = str(input(valor)).replace(',', '.').strip()
        if perg.isalpha() or perg == '':
            print(f'\033[31mO valor "{perg}" não é um valor válido! \033[m')
        else:
            # Qundo for válido! #
            numero = True
            return float(perg)

