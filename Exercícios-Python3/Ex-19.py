import random

nome1 = str(input('Digite o primeiro nome: '))
nome2 = str(input('Digite o segundo nome: '))
nome3 = str(input('Digite o terceiro nome: '))
nome4 = str(input('Digite o quarto nome: '))
lista = [nome1, nome2, nome3, nome4]
escolido = random.choice(lista)
print('A pessoa escolida foi {}'.format(escolido))