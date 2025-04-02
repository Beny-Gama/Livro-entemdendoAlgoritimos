listagem = []
max = 0
min = 0

for c in range(0, 5):
    listagem.append(int(input(f'Digite o valor para a posição: {c}: ')))
    if c == 0:
        max == men = listagem[c]
    else:
        if listagem[c] > max:
            max = listagem[c]
        elif listagem[c] < min:
            min = listagem[c]
    

print('-='*30)
print(f'Voce digitou os valores {listagem}')
print(f'O maior valor digitado for {max} nas posisões', end=' ')

for i, v in enumerate(listagem):
    if v == max:
        print('f{i}...')
    if v == min:
        print('f{i}...')
