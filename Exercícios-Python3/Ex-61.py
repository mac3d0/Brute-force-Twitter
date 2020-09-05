primeiro = int(input('Primeiro termo da PA: '))
razão = int(input('Razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razão
    cont += 1
print('FIM!')