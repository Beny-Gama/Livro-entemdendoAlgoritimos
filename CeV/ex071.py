print('='*40)
print('Banco de Benny'.upper().center(40))
print('='*40)


def whileS():
    valor = float(input('Qual é o valor que vc quer sacar? '))
    cont1, cont5, cont10, cont20, cont50, cont100 = 0, 0, 0, 0, 0, 0

    while valor >= 1:
        if valor < 100:
            cont1 += 1
            valor -= 100
        
        elif valor >= 50:
            cont1 += 1
            valor -= 50

        elif valor < 20:
            cont1 += 1
            valor -= 20

        elif valor < 10:
            cont1 += 1
            valor -= 10

        elif valor < 5:
            cont1 += 1
            valor -= 5

        elif valor < 1:
            cont1 += 1
            valor -= 1

    if cont100 != 0: print(f'Total de {cont100} de edulas de R$:100.00')
    if cont50  != 0:print(f'Total de {cont50} de edulas de R$:50.00')
    if cont20  != 0:print(f'Total de {cont20} de cedulas de R$:20.00')
    if cont10  != 0:print(f'Total de {cont10} de cedulas de R$:10.00')
    if cont5   != 0:print(f'Total de {cont5} de celulas de R$:5.00')
    if cont1   != 0:print(f'Total de {cont1} de celulas de R$:1.00')

print('The while solution'.center(40))
whileS()


def mathS(): # notação: O(1)
    valor = float(input('Qual é o valor que vc quer sacar? '))

    cont100 = valor // 100
    valor %= 100

    cont50 = valor // 50
    valor %= 50

    cont20 = valor // 20
    valor %= 20

    cont10 = valor // 10
    valor %= 10

    cont5 = valor // 5
    valor %= 5

    cont1 = valor // 1
    valor %= 1


    if cont100 != 0: print(f'Total de {cont100} de cedulas de R$:100.00')
    if cont50  != 0: print(f'Total de {cont50} de cedulas de R$:50.00')
    if cont20  != 0: print(f'Total de {cont20} de cedulas de R$:20.00')
    if cont10  != 0: print(f'Total de {cont10} de cedulas de R$:10.00')
    if cont5   != 0: print(f'Total de {cont5}  de celulas de R$:5.00')
    if cont1   != 0: print(f'Total de {cont1}  de celulas de R$:1.00')

print('The math solution'.center(40))
mathS()