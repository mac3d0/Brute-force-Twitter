primeiro = int(input('Primeiro termo: '))
pular = int(input('Razão: '))
décimo = primeiro + (10 -1) * pular
for i in range(primeiro, décimo + pular, pular):
    print('{}'.format(i), end='~> ')
print('Acabou!')
