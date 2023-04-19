#FÓRMULA = A² + B² = C²
import math

catop = float(input('Digite o valor do Cateto Opsoto'))
catadj = float(input('Digite o valor do Cateto Adjacente'))

cat1 = catop ** 2
cat2 = catadj **2
form3 = cat1+cat2
#form4 = math.sqrt(form3) ''' Outra forma e fazer '''
n = math.hypot(catop, catadj)

print('A Hipotenusa vai medir {:.2f}'.format(n))