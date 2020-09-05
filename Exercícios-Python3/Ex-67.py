
while True:
    n = int(input('Digite um número para saber a sua taboada: '))
    if n <= 0:
        print('Programa encerrado!')
        break
    print('-=' * 15)
    for c in range(1, 11):
        print(f'{n} x {c} x {n * c}')
    print('=-' * 15)