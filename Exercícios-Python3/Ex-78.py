lista = []


for números in range(0, 4+1):
    números = lista.append(int(input(f'Digite um número na posição {números}: ')))

    maior = max(lista)
    menor = min(lista)

print('=-' * 25)
print('Os números digitados foram {}'.format(lista))
print('O maior número da lista é {} e se econtra na posição'.format(maior), end=' ')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}... ', end=' ')
print('\nO menor número da lista é {} e se encontra na posição'.format(menor), end=' ')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}... ', end=' ')