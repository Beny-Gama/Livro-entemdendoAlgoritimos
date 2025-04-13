nome = str(input('Nome: '))
media = float(input(f'Média do {nome}: '))

pessoa = {"nome": nome, "media": media}

print('+=' * 20)
print(f'    - O Nome é: {pessoa["nome"]}')
print(f'    - A Media é: {pessoa["media"]}')


if 5 < media < 7:
    print(f'{pessoa["nome"]} está em recuperação!')
    pessoa['situação:'] = 'Recuperação'
elif media < 5:
    print(f'{pessoa["nome"]} passou de ano!')
    pessoa['situação:'] = 'Reprovado'
else:
    print(f'{pessoa["nome"]} passou de ano!')
    pessoa['situação:'] = 'Aprovado'