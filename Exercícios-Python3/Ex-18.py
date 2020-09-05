import math

ang = float(input('Digite o ângulo que você deseja: '))

se1 = math.sin(math.radians(ang))
co1 = math.sin(math.radians(ang))
ta = math.tan(math.radians(ang))
print('O ângulo de {} tem o seno de {:.2f}'.format(ang, se1))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(ang, co1))
print('O ângulo de {} tem o tengente de {:.2f}.'.format(ang, ta))
