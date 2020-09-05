soma = maiorP = maior = menor = tot = 0
barato = ' '
while True:
    produto = str(input('Digite um produto: '))
    preço = float(input('Preço do produto R$: '))
    tot += 1
    if preço >= 1000:
        maiorP += 1
    soma += preço
    if tot == 1:
        maior = menor = preço
    else:
        if preço > maior:
            maior = preço
        if preço < menor:
            menor = preço
            barato = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('O total da compra foi de {}'.format(soma))
print('Tem {} produtos maior do que R$:1000 Reais'.format(maiorP))
print('O produto mais barato foi {} e custa {}'.format(barato, menor))
