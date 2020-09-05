from datetime import date

DataAtual = date.today().year

dados = dict()

dados['nome'] = str(input('Nome: '))
dados['idade'] = int(input('Ano de nascimento: '))
idade = DataAtual - dados["idade"]
dados['ctps'] = int(input('Carteira de trabalho: '))
if dados["ctps"] > 0:
    dados['contrato'] = int(input('Ano da contratação: '))
    ano_contrato = DataAtual - dados["contrato"]
#    print(ano_contrato)
    dados['aposentadoria'] = dados["idade"] + 35
    dados['salário'] = float(input('R$: '))
    print(dados)
    for k, v in dados.items():
        print(f'{k} tem o valor {v}')
else:
    print(dados)
    for k, v in dados.items():
        print(f'{k} tem o valor {v}')
print('Fim!')
