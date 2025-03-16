from datetime import date

nascimento = int(input(f'qual é sau data de nascimento: ')) 
hoje = date.today().year
idadeMilitar = 18
idade = 0

if nascimento > hoje:
    idade = nascimento - hoje
elif nascimento < hoje:
    idade = hoje - nascimento

if idade > idadeMilitar:
    print(f'vc já se alistou!') 
    print(f'Tem {idade - idadeMilitar} anos que vc se alistou')
    print(f'Vc se alistou em {hoje - (idade - idadeMilitar)} ')
elif idade < idadeMilitar:
    print(f'vc vai se alistar!')
    print(f'Tem {idadeMilitar - idade} anos vc vai se laistar')
    print(f'Vc vai se alistar {hoje + (idadeMilitar - idade)} ')
else:
    print(f'Vc esta ma idade de se alistar!!!')


