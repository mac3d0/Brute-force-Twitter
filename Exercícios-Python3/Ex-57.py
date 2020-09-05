sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe o sexo: '))
print('O sexo {} resistrado com sucesso'.format(sexo))
