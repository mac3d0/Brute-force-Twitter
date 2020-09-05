import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br')
except urllib.error.URLerror:
    print('Não foi possível acessar o site')
else:
    print('O site está no ar...')
    print(site.read())