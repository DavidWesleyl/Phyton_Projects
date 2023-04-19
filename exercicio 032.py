#AUMENTO DE SALÁRIO

salario = float(input('Digite o salário e veja o valor do aumento'))

s1 = (10/100) * salario/1
s2 = s1+salario

sal1 = (15/100) * salario/1
sal2 = sal1 + salario

if salario >= 1250.00:
    print('Com o aumento de 10% para salarios acima de R$ 1250,00. Seu salário será {:.2f}'.format(s2))
if salario < 1250.00:
    print('Com o aumento de 15% para salários menores que 1250,00. Seu salário será {:.2f}'.format(sal2))


