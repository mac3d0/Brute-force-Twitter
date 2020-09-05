def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m²')


print('Controle de terrenos')
print('-=' * 30)

l = float(input('LARGURA: '))
c = float(input('COMPRIMENTO: '))

área(l, c)

'''
def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m²')

print('Controle de terrenos')
print('-' * 20)

l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l, c)
'''