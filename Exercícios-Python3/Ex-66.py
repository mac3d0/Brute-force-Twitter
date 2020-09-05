cont = soma = média = maior = menor = 0
resp = 'sS'
while resp in 'sS':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar [S/N]: ')).upper()
média = soma / cont
print('Você digitou quatro números {} e a média foi de {}'.format(cont, média))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
print('Acabou!')