salario = int(input(f'Qual é o salario: '))
limitador = 1250
if salario >= limitador:
    novoSalario = salario * 1.1
else:
    novoSalario = salario * 1.15
print(f'quem ganhava {salario:.2f} vai pasar a ganhar {novoSalario:.2f}')