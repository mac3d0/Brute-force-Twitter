lista = []

while True:
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar [S/N]: ')).upper().strip()
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente {lista}')
if 5 in lista:
    print('Os valore 5 faz parte da lista!')
else:
    print('Os valor 5 não foi encontrado na lista!')
