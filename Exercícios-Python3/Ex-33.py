n1 = int(input('Digite um valor: '))
n2 = int(input('Digite mais um valor: '))
n3 = int(input('Digite outro valor: '))
#Verificando o menor número
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
#Verificando o maior número
maior = n1
if n2 > n1 and n2 > n3:
    maior = 0
if n3 > n1 and n3 > n2:
    maior = n3
print('O menor valor digitado foi o {}'.format(menor))
print('O maior valor digitado foi o {}'.format(maior))