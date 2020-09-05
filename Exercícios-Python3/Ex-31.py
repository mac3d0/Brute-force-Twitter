dis = int(input('Qual é a distância da viagem: '))
if dis <= 200:
    pagar = dis * 0.50
    print('Você viajou {}KMs \nO total a pagar é R$:{:.2f}'.format(dis, pagar))
elif dis > 200:
    pagar = dis * 0.45
    print('Você viajou {}KMs\nO total a pagar é R$:{:.2f}'.format(dis, pagar))