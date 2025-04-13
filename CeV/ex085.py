lista = [[],[]]
for i in range(7):
    num = int(input(f'Digite o {i+1}o. valor : '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)

lista[0].sort()
lista[1].sort()
print(f'os valores pares: {lista[0]}')
print(f'os valores impares: {lista[1]}')