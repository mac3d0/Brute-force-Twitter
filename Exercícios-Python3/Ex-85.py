par_impar = [[], []]

for lugar in range(1, 7+1):
    n = int(input(f'Digite o {lugar}º. valor: '))
    if n % 2 == 0:
        par_impar[0].append(n)
    else:
        par_impar[1].append(n)
print('-=' * 20)
print(f'Os valores pares digitados foram {par_impar[0]}')
print(f'Os valores ímpares digitados foram {par_impar[1]}')
