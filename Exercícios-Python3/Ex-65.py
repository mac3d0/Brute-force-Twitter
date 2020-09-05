soma = cont = média = maior = menor = quant = 0
resp = 'S'
while resp in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if quant == 1:
        maior = menor = n
    else:
        if n  > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar [S/N]: '))
média = soma / cont
print('Total de números digitados {} \nA soma de todos os números é {}'.format(cont, soma))
print('O maior número é {} e o menor {}'.format(maior, menor))
print('A média dos números é {}'.format(média))
