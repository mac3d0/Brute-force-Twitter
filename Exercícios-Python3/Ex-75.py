par = impar = 0
n = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')))
print('Você digitou os valores {}'.format(n))
print('O número 9 aparece {} vezes'.format(n.count(9)))
if 3 in n:
    print('O valor 3 apareceu na posição {}ª posião'.format(n.index(3)+1))
else:
    print('O valor não 3 não apareceu em nenhum lugar')
print('Os valores digitados foram', end=' ')
for ns in n:
    if ns % 2 == 0:
        print(n, end=' ')