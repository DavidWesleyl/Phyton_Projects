larg = float(input('Largura da Parede'))
alt = float(input('Altura da Parede'))
area = alt * larg

#Cada litro pinta uma área de 2m².

litro = area / 2

print('Sua parede tem a dimensão de {} x {} e sua área é {}m²'.format(larg, alt, area))
print('Para pintar a parede, será necessário {} litro(s) de tinta'.format(litro))
