n = int(input('Digite um número: '))
print('''
[1] conventer em binário
[2] converter em octal
[3] converter em hexadecimal
''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} em binário fica {}'.format(n, bin(n)[2:]))
elif opção == 2:
    print('{} em octal fica {}'.format(n, oct(n)[2:]))
elif opção == 3:
    print('{} em hexadecimal fica {}'.format(n, hex(n)[2:]))
else:
    print('Error')