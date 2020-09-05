from datetime import date
atual = date.today().year

maior = 0
menor = 0

for pess in range(1, 7+1):
    nasc = int(input('Em que ano a {}ª pessoa nasceu: '.format(pess)))
    idade = atual - nasc
    if idade < 40:
        menor += 1
    else:
        maior += 1
print('O total de pessoas mais velhas é {}'.format(maior))
print('O total de pessoas jovens é {}'.format(menor))