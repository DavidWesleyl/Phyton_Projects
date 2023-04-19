# CONFEDERAÇÃO DE NATAÇÃO (9 - MIRIM, 14 - INFANTIL , 19 - JUNIOR, 20 - SENIOR, ACIMA DE 25 - MASTER)

print('                                             NATAÇÃO ')
from datetime import date

nasc = int(input('Digite o ano que você nasceu, para vermos em que categoria se encaixa'))
ano = date.today().year  # 2022
a2 = ano - nasc
pergunta = str(input('De acordo com sua data de nascimeto, você tem (irá completar) {} anos, correto?'.format(a2)))

if a2 <= 9:
    print('De acordo com sua idade, você se encaixa na categoria MIRIM!')
elif a2 <= 4:
    print('De acordo com sua idade, você se encaixa na categoria INFANTIL!')
elif a2 <= 19:
    print('De acordo com sua idade, você se encaixa na categoria JUNIOR!')
elif a2 < 25:
    print('De acordo com sua idade, você se encaixa na categoria SENIOR!')
elif a2 >= 25:
    print('De acordo com sua idade, você se encaixa na categoria MASTER!')
