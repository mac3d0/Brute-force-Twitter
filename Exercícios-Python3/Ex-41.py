from datetime import date

atual = date.today().year

nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Sua idade é {}'.format(idade))
if idade <= 8:
    print('Pré-mirim')
elif idade <= 9:
    print('Mirim')
elif idade <= 12:
    print('Petiz')
elif idade <= 4:
    print('Infaltil')
elif idade <= 16:
    print('Juvenil')
elif idade <= 19:
    print('Junior')
elif idade >= 20:
    print('Sênio')