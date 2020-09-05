n1 = int(input('Reta 1: '))
n2 = int(input('Reta 2: '))
n3 = int(input('Reta 3: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n2 + n1:
    print('È possível fazer um triângulo')
else:
    print('Não é possível fazer um triângulo')