from time import sleep

def maior(* núm):
    cont = maior = 0
    print('Analizando os valoores passados...')
    for valor in núm:
        print(f'{valor} ', end='', flush=True)
        sleep(0.2)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
            cont += 1
        print(f'Foram informados {cont} valores.')
        print(f'O maior valor informado foi {valor}')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)