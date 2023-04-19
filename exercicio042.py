#calculo de imc
# IMC = kg/m²

print('                             Cálculo de IMC (índice de massa corporal)')

peso = float(input('1 - Digite seu peso (KG):'))
altura = float(input('2 - Digite sua altura (apenas números):'))
imc = peso/(altura * altura)

if imc < 18.5:
    print('Seu IMC é {:.1f} está muito baixo, você está abaixo do peso!'.format(imc))
elif imc < 24.9:
    print('Seu IMC é {:.1f} e está normal, você está no peso ideal'.format(imc))
elif imc < 29.9:
    print('Seu IMC é {:.1f}, você está com sobrepeso, tome cuidado!'.format(imc))
elif imc < 34.9:
    print('Seu IMC é {:.1f}, você está com Obesidade grau 1, procure um médico'.format(imc))
elif imc < 39.9:
    print('Seu IMC é {:.1f}, você está com Obesidade grau 2, procure um médico URGENTE!'.format(imc))
elif imc > 40:
    print('Seu IMC é {:1f} você está com obesidade grau 3, procure um médico URGENTE! TENHA CUIDADO!'.format(imc))