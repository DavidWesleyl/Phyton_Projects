nome = str(input('Digite seu nome completo')).strip()
print('Analisando seu nome...')
print('seu nome em maiúsculas, é',  nome.upper())
print('Seu nome em minúsculas, é', nome.lower())
# Nome sem espaços
nome1 = len(nome)-nome.count(' ')
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

print('Seu  nome ao todo, tem {} letras'.format(nome1))