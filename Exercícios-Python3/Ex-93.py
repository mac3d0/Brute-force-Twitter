def linhas():
    print('-=' * 30)

jogador = dict()
gols = list()

jogador['nome'] = str(input('Nome do jogador: '))
jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
for partidas in range(jogador["partidas"]):
    jogador['gols'] = int(input(f'Quantos gols na partida {partidas}: '))
    gols.append(jogador["gols"])
gols = jogador[:]
linhas()
print(jogador)
linhas()
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
linhas()


