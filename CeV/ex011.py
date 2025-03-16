largura = float(input('Largura da Parede: '))
altura = float(input('Altura da Parede: '))

area = largura*altura
tinta = area / 2

print(f'Sua parede tem a dimenção de {largura}X{altura} e a usa área é de {area}m2')
print(f'Para pintar vc vai presizar de {tinta}l de tinta')