rangest = 4
soma = 0
cont = 0
media_idade = 0
mais_velho = 0
nome_mais_velho = ''
cont_m = 0

for i in range(rangest):
    print('----- {} Pessoas -----'.format(i + 1))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    
    soma += idade
    
    if sexo == 'M' and idade > mais_velho:
        nome_mais_velho = nome
        mais_velho = idade
    
    if sexo == 'F' and idade < 20:
        cont_m += 1

media_idade = soma / rangest

# media de idade do grupo
print(f'A Media de idade é iqual: {media_idade}')
# o homem com mais idade & seu nome
print(f'O Homem mais velho é {nome_mais_velho} usa idade é {mais_velho}')
# todas as mulher que são menores de 20 anos
print(f'As Mulheres com com menos de 20 anos são: {cont_m}')
