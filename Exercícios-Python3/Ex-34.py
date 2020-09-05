salário = float(input('Digite seu salário R$:'))
if salário == 1250.00:
    aumento = salário + (salário * 15 / 100) #Para descontos é subistituir o + pelo -
else:
    aumento = salário + (salário * 10 / 100)
