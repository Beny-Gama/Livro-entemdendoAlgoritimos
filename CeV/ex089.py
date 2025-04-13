lista=[]
cont=0

while True:
    nome = str(input('Nome: '))
    nota1 = int(input('Nota 1: '))
    nota2 = int(input('Nota 2: '))

    media = (nota1 + nota2) / 2 

    lista.append([nome, [nota1, nota2], media])

    res = str(input('quer continuar? [S/N] '))
    if res in 'Nn':
        break

print('-='*10)
print('No. NOME       MÉDIA')
print('-'*20)

for i in range(len(lista)):
    nome = lista[i][0]
    media = (lista[i][1][0] + lista[i][1][1]) / 2
    print(f'{i:<4}{nome:<10}{media:>8.1f}')

print('-='*10)

i = 0
while i != 999:
    print('-'*20)
    i = int(input('Mostrar notas do que aluno: [999 interrompe] '))
    print(f'A nota do {lista[i][0]} são: {lista[i][1]}')
