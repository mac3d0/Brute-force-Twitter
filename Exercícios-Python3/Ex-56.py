média_de_idade = 0 #Média de idade
soma_idade = 0 #Somar para depois divídir
mulher20 = 0 #Total de mulheres menor que 20
nome_velho = '' #Nome do homem mais velho
maior_idade = 0 #Idade mais velha entre os homens

for i in range(1, 5):
    print('-----{}ª-----'.format(i))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma_idade += idade
    if i == 1 and sexo in 'Mm':
        maior_idade = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade:
        maior_idade = idade
        nome_velho = nome
    elif sexo in 'Ff' and idade < 20:
            mulher20 += 1

média_de_idade = soma_idade / 4 #Para saber a média de idade do grupo
print('A média de idae do grupo é {}'.format(média_de_idade))
print('O homem mais velho tem {} anos e se chama {}'.format(maior_idade, nome_velho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulher20))


'''
Soma todas a idades e depois divídir pelo número de idades digitadas.
'''