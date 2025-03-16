
from math import radians, sin, cos, tan
angulo = float(input('Digite o algulo que vc deseja: '))

seno = sin(radians(angulo))
print(f'O angulo de {angulo} tem o seno de {seno:.2f}')
cosseno = cos(radians(angulo))
print(f'O angulo de {angulo} tem o seno de {cosseno:.2f}')
tangente = tan(radians(angulo))
print(f'O angulo de {angulo} tem o seno de {tangente:.2f}')