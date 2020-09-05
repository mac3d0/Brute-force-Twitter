n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = n1 + n2 / 2
print('Tirando {} e {}, a média do aluno é {}'.format(n1, n2, m))
if m >= 6.0:
    print('Aprovado!', end='')
elif m <= 5.0 or m >= 5.9:
    print('Recuperação')
elif m < 6.0:
    print('Reprovafo', end='')