from random import randint

v = 0

while True:

    computador = randint(0, 10)

    n = int(input('Digite um número: '))
    op = str(input('Ímpar ou Par [I/P]: ')).upper()[0]
    tot = n + computador
    if op == 'P':
        print('Par escolhido')
        if n % 2 == 0:
            v += 1
            print('{} é par, você ganhou!'.format(tot))
        else:
            print('{} é ímpar, você perdeu!'.format(tot))
            break
    elif op == 'I':
        print('Ímpar escolhido')
        if n % 2 == 1:
            v += 1
            print('{} é ímpar, você ganhou!'.format(tot))
        else:
            print('{} é par, você perdeu!'.format(tot))
            break

print('=-=' * 15)
print('GAME OVER')
print('Número de vitórias {}'.format(v))
print('=-=' * 15)