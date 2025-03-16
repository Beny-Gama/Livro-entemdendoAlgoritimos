casa = float(input('Valor da casa R$: '))
salario = float(input('Salario do Comprador R$: '))
anos = float(input('Quantos anos de financiamento R$: '))

parelas = casa / anos

if salario * 0.3 >= parelas:
    print('Emprestimo é não foi aprovado')
else:
    print('Emprestimo Aprovado!')