from datetime import date
nascimento = int(input('Ano de nascimento: '))
idade = date.today().year - nascimento 

if idade <= 9: cargo = "Mimir" 
elif idade <= 14: cargo = 'Infantil'
elif idade <= 19: cargo ='Junior'
elif idade <= 25: cargo = 'Senior'
elif idade > 25: cargo = 'Master' 

print(f'Sua idade é {idade} então seu cargo é: {cargo.upper()}')