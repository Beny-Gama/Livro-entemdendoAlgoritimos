# matix 3x3
matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
         ]

pares, linha, coluna = 0, 0, 0

for l in range(3):
    for c in range(3):
        matrix[l][c] = int(input(f'Digite um valor [{l, c}]: '))
        if matrix[l][c] % 2 == 0:
            pares += matrix[l][c]
        if c + 1 == 3:
            coluna += matrix[l][c]
        if l + 1 == 2:
            linha += matrix[l][c]


print('=-'*40)

for l in range(3):
    for c in range(3):
        print(f'[{matrix[l][c]:^5}]', end='')
    print()

print('=-'*40)

print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceria coluna é {coluna}')
print(f'A soma dos valores da sequnda linha é {linha}')