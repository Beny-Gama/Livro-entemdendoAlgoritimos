n1 = float(input('Qual a primeira nota: '))
n2 = float(input('Qual a primeira nota: '))

media = (n1 + n2) / 2

if media < 5:
    print('REPROVADO')
    print(f'Sua Nota foi {media}')
elif media > 5 and media <= 6.9:
    print('RECUMERAÇÃO')
    print(f'Sua Nota foi {media}')
elif media >= 7:
    print('APROVADO')
    print(f'Sua Nota foi {media}')
