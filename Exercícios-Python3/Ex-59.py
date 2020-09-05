from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
#opção = 0
while True:
    print('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa''')
    opção = int(input('>>> Qual é a sua opção: '))
    if opção == 1:
        s = n1 + n2
        print('{} + {} = {}'.format(n1, n2, s))
        print('=-' * 11)
        sleep(0.5)
    elif opção == 2:
        m = n1 * n2
        print('{} x {} = {}'.format(n1, n2, m))
        print('-=' * 11)
        sleep(0.5)
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        if n1 < n2:
            menor = n1
        else:
            menor = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
        print('Entre {} e {} o menor valor é {}'.format(n1, n2, menor))
        sleep(0.5)
    elif opção == 4:
        print('Informe os números novamente')
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
        sleep(0.5)
    elif opção == 5:
        print('Saindo do programa')
        break
    else:
        print('Opção inválida')