maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}ª: '.format(p)))
    if p == 1: #Os dois são maiores!
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('A pessoa mais pesada tem {}Kg'.format(maior))
print('A pessoa mais leve tem {}Kg'.format(menor))