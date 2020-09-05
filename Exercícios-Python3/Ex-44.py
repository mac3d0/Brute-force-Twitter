print('='*10, 'Lojas Guanabara', '='*10)

compras = float(input('Preço das compras R$:'))
print('Formas de pagamentos')

print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista no cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')

opção = int(input('Qual é a opção: '))

if opção == 1:
    desconto = compras - (compras * 10 / 100)
    print('Sua compra de R$:{:.2f} vai custar R$:{:.2f}'.format(compras, desconto))

elif opção == 2:
    desconto = compras -(compras * 5 / 100)
    print('Sua compra de R$:{:.2f} vai custar R$:{:.2f}.'.format(compras, desconto))

elif opção == 3:
    dividir = compras / 2
    print('Sua compra de R$:{:.2f} \nVai ficar em duas parcelas de R$:{:.2f}.'.format(compras, dividir))

elif opção == 4:
    parcelas = int(input('Quantas parcelas: '))
    total = compras +(compras * 20 / 100)
    parcela = total / parcelas
    print('Sua compra de R$:{:.2f} Vai ser parcelada em {} VEZES COM JUROS'.format(compras, parcelas))
    print('Sua compra de R$:{:.2f} vai custar R$:{:.2f} no final'.format(compras, total))

else:
    print('Opção invalida!')