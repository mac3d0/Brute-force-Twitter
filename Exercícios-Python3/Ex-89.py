ficha = list()
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    média = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], média])
    resp = str(input('Quer continuar ? [S/N]: '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10} {"MÈDIA":<8} {"STATUS":<11}')
print('_' * 35)
for i, a in enumerate(ficha):
    if a[2] > 6.0:
        status = 'Aprovado'
    else:
        status = 'Reprovado'
    print(f'{i:<4}{a[0]:<10}{a[2]:<8.1f}{status:<11}')
while True:
    print('_' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<<Volte sempre>>>')
