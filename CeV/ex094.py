
cadastro = dict()
soma = 0

while True:
    cadastro['nome'] = str(input('Nome: '))
    
    while cadastro['sexo'] not in 'FfMm':
        cadastro['sexo'] = str(input('Sexo [F/M] ')).upper()[0]
        if cadastro['sexo'] not in 'FfMm': print('ERRO! Por favor, digite só M ou F')
    
    while cadastro['idade'] is not 
        cadastro['idade'] = int(input('Idade: '))

    
    
    if str(input('Deseja contunuar? [S/N] ')).upper()[0] in 'Nn': break

print(cadastro)