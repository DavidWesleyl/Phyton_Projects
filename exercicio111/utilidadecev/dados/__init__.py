def leiadinheiro(valor):
    numero = False
    while not numero:
        perg = str(input(valor))
        if perg.strip():
            print(f'O valor {perg} não é um valor válido! ')


     