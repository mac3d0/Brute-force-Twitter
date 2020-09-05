veloc = int(input('Qual é a velocidade atual do carro: '))
if veloc > 80:
    print('MULTADO! Você foi exedeu o limite de 80KM/H')
    multa = (veloc - 80) * 7
    print('Você deve pagar uma multa de {:.2f}'.format(multa))
print('Tenha um bom dia!')