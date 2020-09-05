cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezeseis',
      'dezesete', 'dezoito', 'dezenove', 'vinte')

while True:
    n = int(input('Digite um número: '))
    if 0 <= n <= 20:
        break
    print('Tente novamente', end=' ')
print(f'Você digitou o número {cont[n]}')