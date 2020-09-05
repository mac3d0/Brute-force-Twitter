from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')

print('''
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
''')

computador = randint(0, 2)

jogador = int(input('Qual é sua jogada: '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print('-=' * 11)
print('O jogador escolheu {}'.format(itens[jogador]))
print('O computador escolheu {}'.format(itens[computador]))
print('-=' * 11)

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Jogador vence:')
    elif jogador == 2:
        print('Computador vence')
    else:
        print('Jogadar inválida!')
elif computador == 1:
    if jogador == 0:
        print('Computador ganhou')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Jogador ganhou')
    else:
        print('Jogada inválida!')
elif computador == 2:
    if jogador == 0:
        print('Jogador ganhou')
    elif jogador == 1:
        print('Computador ganhou')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada inválida!')
else:
    print('Opção inválido')