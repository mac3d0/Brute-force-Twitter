dados = {}
dados['nome'] = str(input('Nome: '))
dados['média'] = float(input(f'Média de {dados["nome"]}: '))
if dados["média"] >= 7.0:
    status = 'Aprovado'
else:
    status = 'Reprovado'
print(f'Nome é igual a {dados["nome"]}')
print(f'Média é igual a {dados["média"]}')
print(f'Situação é igual a {status}')
