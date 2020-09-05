from time import sleep

def linhas():
    print('-=' * 20)


def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}')
    linhas()
    sleep(0.2)
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')

contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
linhas()
ini = int(input('Inicío: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)
