listagem = ('Caderno', 25.60, 'Lápis', 0.50, 'Caneta', 1.50, 'Borracha', 2.40,
            'Tesoura', 3.50, 'Cola', 2.50, 'Corretivo', 4.20,
            'Apontador', 1.50, 'Bolsa', 135.90)
for itens in range(0, len(listagem)):
    if itens % 2 == 0:
        print(f'RS:{listagem[itens]:.<30}', end=' ')
    else:
        print(f'RS:{listagem[itens]:>7.2f}')