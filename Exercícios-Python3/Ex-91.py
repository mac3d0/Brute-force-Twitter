ficha = list()

while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], media])
    resp = str(input('Quer continuar ? [S/N]: '))
    if resp in 'Nn':
        break
print('Alunos cadastrados...')
print('-=' * 20)
print(f'{"No."}     {"NOME"}    {"Média":}     {"STATUS"}')
for i, a in enumerate(ficha):
    if a[2] >= 6.0:
        status = 'Aprovado'
    else:
        status = 'Reprovado'
    print(f'{i}      {a[0]}    {a[2]:<8.1f} {status}') #7
print('-=' * 20)
while True:
    opc = str(input('"No" do aluno que deseja buscar para sair aperte ou ctrl + c(000)'))
    print(f'O aluno {i} teve as notas {a[0]} e {a[1]}')
    if KeyboardInterrupt:
        break
    elif opc == 999:
        break
print('Fim do programa...!')
