# TENTE ABRI O SITE PUDIM.COM.BR #

from urllib import request

site = 'http://pudim.com.br'
try:
    resposta = request.urlopen(site)
except:
    print('O site pudim.com.br está acessível')
else:
    print('O site pudim.com.br não está acessível')



