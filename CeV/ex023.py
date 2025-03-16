num = int(input('Digite o numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'Analizando o numero {num}')
print(f'Unidade: {u}')
print(f'Desena: {d}')
print(f'Centena: {c}')
print(f'Mulhar: {m}')