valor_casa = float(input('Valor da casa R$:'))
salário = float(input('Seu salário R$:'))
anos = int(input('Anos a pagar'))

prestação = valor_casa / (anos * 12) #Prestação
mínimo = salário * 30 / 100 #30% do salário

print('Para pagar uma casa de R$:{:.2f} em {} anos '.format(valor_casa, anos), end='')
print('A prestação será de R$:{:.2f}'.format(prestação))
if prestação <= mínimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')