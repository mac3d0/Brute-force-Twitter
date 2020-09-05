lista = []

while True:
    n = int(input('Digite um número: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Error, tente novamente')
    resp = str(input('[S/N]: '))
    if resp in 'Nn':
        break
lista.sort()
print('Você digitou os valores {}'.format(lista))
