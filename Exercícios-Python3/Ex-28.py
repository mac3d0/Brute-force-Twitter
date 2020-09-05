from random import randint

print('-=-' * 20)
print('Tente acertar o número de 0 A 5')
print('-=-' * 20)
n = int(input('Digite um número entre 0 e 5: '))

s = randint(0, 5)
if s == n:
    print('Acertou!')
elif s != n:
    print('Você errou! Era o número {}'.format(s))