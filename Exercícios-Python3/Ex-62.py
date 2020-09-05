primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
cont = 1
termo = primeiro
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mais: '))
print('Progressão finalizada com {} termos mostrados'.format(total))



#arquivo = open('maior.txt', 'w')
#arquivo.write('Existe esse número de maiores {}'.format(maior))
