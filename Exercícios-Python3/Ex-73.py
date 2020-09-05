times = ('Atlético-MG', 'Palmeiras', 'São Paulo', 'Santos', 'Bahia', 'Botafogo', 'Cruzeiro', 'Atlético-PR', 'Flamengo',
         'Chapecoense', 'Corithias', 'Ceará', 'Fluminense', 'Goiá', 'Internacional', 'Fortaleza', 'CSA', 'Grêmio',
         'Avaí', 'Vasco da Gama')
print('-=' * 15)
print('Lista de times do Brasileirão', times)
print('-=' * 15)
print('Os 5 primeiros são', times[0:5])
print('-=' * 15)
print('Os 4 últimos s', times[16:])
print('-=' * 15)
print('Times em ordem alfabética:', sorted(times))
print('-=' * 15)
print('O time da Chapecoense esta na {}ª posição.'.format(times.index('Chapecoense')))
