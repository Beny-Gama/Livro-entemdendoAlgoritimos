jogador = dict()
gols = list()
soma = 0

jogador['nome'] = str(input('Nome do Jogador: '))
partidas = int(input('Qunatas partidas ele jogou? '))

for i in range(partidas):
    gol = int(input(f'Qunatos gols na Partida {i}? '))
    gols.append(gol)
    soma += gol
jogador['gols'] = gols
jogador['total'] = soma

print('-=' * 20)
print(jogador)
print('-=' * 20)

for k, v in jogador.items():
    print(f'No campo {k} tem o valor {v}!')
print('-=' * 20)

for i, v in enumerate(jogador['gols']):
    print(f'    => Na Partida {i}, ele fes {v} gols!')
print(f'    Foi um total de {jogador["total"]} gols')

