# matix 3x3
matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
         ]
for l in range(3):
    for c in range(3):
        matrix[l][c] = int(input(f'Digite um valor [{l, c}]: '))
        print(f'[{matrix[l][c]:^5}]', end='')

# print(matrix)

# for l in range(3):
#     for c in range(3):
#         print(f'[{matrix[l][c]:^5}]', end='')
#     print()