from random import randrange 

num = int(input('Qual é o numero de 0 a 5: '))

rnun = randrange(6)

if num == rnun:
    print(f'PARABENS vc ganhou! \nO numero sorteado é {rnun}Tambem')
else:
    print(f'QUE PENA! \nO numero sorteado foi: {rnun}')