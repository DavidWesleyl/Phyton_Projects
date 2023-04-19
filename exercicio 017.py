import math

angulo = float(input('Digite o valor do Angulo'))

sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print('O angulo de {}, tem como seno: {:.2f}, coseno {:.2f} e tangente {:.2f}.'.format(angulo, sen, cos, tan))


''' PARA CALCULAR O SENO, COSSENO E TANGENTE DE QUALQUER GRAU, PRECISA CONVERTER PARA RADIANOS '''