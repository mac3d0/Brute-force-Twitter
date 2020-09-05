from datetime import date

atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
if idade == 18:
    print('Deve se alistar imediatamente.')
elif idade < 18: #Menor que 18
    falta = 18 - idade #Para saber quanto tempo falta
    print('Falta {} anos para o alistamento'.format(falta))
    ano = atual + falta #Saber o ano que é para se alistar
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18: #Maior que 18
    falta = idade - 18 #Saber quanto tempo se passou do seu alistamento
    print('Você deveria ter se alistado há {} anos atrás'.format(falta))
    ano = atual - falta #O ano que você deveria se alistar
    print('Seu alistamento foi em {}'.format(ano))

'''
Variável "falta" calcula quanto tempo falta para o alistamento.
Variável "ano" calcuça quando tenho que me alistar
'''