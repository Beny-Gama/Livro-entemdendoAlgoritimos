from random import randint
from time import sleep
from operator import itemgetter

jogo = {}
print('Valores sorteados:')
for i in range(4):
    jogador = f'jogador{i+1}'
    valor = randint(1, 6)
    jogo[jogador] = valor
    print(f'{jogador} tirou {valor} no dado!')
    sleep(1)

print('-=' * 20)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('Ranking dos jogadores:')
for i, (jogador, valor) in enumerate(ranking):
    print(f'{i+1}º lugar: {jogador} com {valor}')
    sleep(1)