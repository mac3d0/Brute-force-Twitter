dias = int(input('Quantos dias você ficou com o carro: '))
kms = float(input('Kilômetros rodados com o carro: '))
diasap = dias * 60
kmsap = kms * 0.15
tot = diasap + kmsap
print('O total a pagar é R$:', tot)