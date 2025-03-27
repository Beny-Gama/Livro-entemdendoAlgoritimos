sexo = str(input('informe o seu sexo [M/F]: ')).strip().upper()[0]

while sexo not in 'FfMm':
    sexo = str(input('Vc digitou erra: informe novamente [M/F]: ')).strip().upper()[0]

print(f'seu sexo é: {sexo}')
