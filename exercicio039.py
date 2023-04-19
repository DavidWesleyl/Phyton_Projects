#MÉDIA DO ALUNO
print('                            *VOCÊ PRECISA OBTER MAIS DE 7.0 PARA PASSAR*     ')
m1 = float(input('Digite a primeira nota'))
m2 = float(input('Digite a segunda nota'))

soma = (m1+m2) / 2

if soma < 5.0:
    print('Sua média foi {:.1f} infelizmente não obteve os pontos para prosseguir.. Não desista! :('.format(soma))
elif soma < 6.9:
    print('Sua média foi {:.1f}, Você está de recuperação. Estude mais!'.format(soma))
elif soma > 7.0:
    print('Sua média foi {:.1f}. Parabéns, você foi aprovado! :)'.format(soma))
