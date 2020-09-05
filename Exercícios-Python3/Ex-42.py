n1 = int(input('Reta 1: '))
n2 = int(input('Reta 2: '))
n3 = int(input('Reta 3: '))
if n1 < n2 + n3 and n2 < n3 + n1 and n3 < n2 + n1:
    print('Triângulo formado')
    if n1 == n2 == n3:
        print('Equilátero')
    elif n1 != n2 != n3 != n1:
        print('Escaleno')
    else:
        print('Isóceles')
else:
    print('não foi possível fazer o triângulo')