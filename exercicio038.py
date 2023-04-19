#ALISTAMENTO MILITAR
from datetime import date

'''print('# Alistamento Militar')
ano = int(input('Em que ano você nasceu?'))
a1 = 2022 - ano
p = str(input('De acordo com sua data de nascimento, você tem (irá completar) {} anos esse ano, correto?'.format(a1)))
p1 = a1 - 18
p2 = 18 - a1


if a1 < 18:
    print('Voce ainda não pode se alistar, falta/faltam {} ano(s)'.format(p2))
elif a1 > 18:
    print('Você já passou {} anos da época de se alistar'.format(p1))
elif a1 == 18:
    print('Você está no tempo de se alistar')'''


ano = date.today().year
idade = int(input('Em que ano você nasceu?'))
temp = ano - idade
passou = temp - 18
p2 = 18 - temp
str(input('De acordo com sua data de nascimento, você tem/irá completar {} anos, correto? s/n'.format(temp)))

if temp < 18:
    print('Você não está no tempo de se alistar, faltam {} ano(s)'.format(p2))
    ano1 = ano + temp
    print('Você irá se alistar no ano de {}'.format(ano1))
elif temp == 18:
    print('Você tem que se apresentar na junta de serviço militar obrigatório esse ano!')
elif temp > 18:
    print('Você deveria ter se alistado há {} ano(s)'.format(passou))
    ano1 = ano - passou
    print('Seu ano de alistamento foi em {}'.format(ano1))






