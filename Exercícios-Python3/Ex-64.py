n = cont = soma = 0
while True:
    n = int(input('Digite um número. [aperte 999 para parar o programa]: '))
    soma += n
    cont += 1
    if n == 999:
        print('Você parou o programa.')
        break
print('Números digitados {} \nSoma de todos os números digitados {}'.format(cont, soma-999))