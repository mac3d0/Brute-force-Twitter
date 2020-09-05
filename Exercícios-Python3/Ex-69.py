tot18 = totH = totF = 0

while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totF += 1
    resp = '  '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break

print('Total de pessoas maior de 18: {}'.format(tot18))
print('Ao todo temos {} homens cadastrados'.format(totH))
print('E temos {} mulher com menos de 20 anos de idade'.format(totF))
