# FAÇA UM PROGRAMA QUE TEHA UMA FUNÇÃO CHAMADA ÁREA() QUE RECEBA AS DIMENSÕES DE UM TERRENO RETANGULAR
# ( LARGURA E COMPRIMENTO ) E MOSTRE A ÁREA DO TERRENO #

def terreno(largura, comprimento):
    largura = float(input('Largura: '))
    comprimento = float(input('Comprimento: '))
    area = largura * comprimento
    print(f'O terreno de {largura}x{comprimento} tem uma área de {area}m²')


terreno(0, 0)
