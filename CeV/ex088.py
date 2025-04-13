from random import randint
from time import sleep


print('-'*30)
print(f'    JOGOS NA MEGA SENA    ')
print('-'*30)

n = int(input('Quantos jogos vc quer sortear? '))
print('-='*3, f'Sortinado {n} Jogos', '-='*3)

for i in range(n):
    lista = [0,0,0,0,0,0]
    for s in range(6):
        lista[s] = randint(0, 60)
    print(f'Jogo {i+1}: {lista}')
    sleep(2.5)


