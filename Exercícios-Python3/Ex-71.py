
print('=' * 30)
print('{:^30}'.format('BANCO VLA'))
print('=' * 30)
valor = float(input('Quanto você quer saca: '))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        print('Total de {} cédulas de R$:{}'.format(totcéd, céd))
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre no banco VLA! Tenha um bom dia!')
