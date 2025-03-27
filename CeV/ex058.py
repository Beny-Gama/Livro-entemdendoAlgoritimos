from random import randint

p = int(input('acabei de adivinhar em um numero entre 0 e 10: \nSera que vc descobre \nQual é o seu Palpite? '))
n = randint(0, 10)

while p == n:
    if p > n:
        p = int(input('Vocé chutou Alto... Terte outra vez: '))
    else:
        p = int(input('você chutou BAIXO... Tente outra vez: '))

print(f'Parabens vc acertou: {p} é  no certo!')
