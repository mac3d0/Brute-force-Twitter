from random import randint

s = (randint(1, 10),randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10) )
print('Os valores sorteados foram: ', end='')
for n in s:
    print(n, end=' ')
print('\nO maior valor foi o {}'.format(max(s)))
print('O menor valor foi o {}'.format(min(s)))
