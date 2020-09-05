n = int(input('Digite um número: '))

u = n // 1 % 100
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print('Analizando o número: {}'.format(n))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))