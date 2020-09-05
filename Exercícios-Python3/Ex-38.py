n1: int = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('{} é maior que {}'.format(n1, n2))
elif n1 < n2:
    print('{} é maior que {}'.format(n2, n1))
else:
    print('Os dois números são iguais')