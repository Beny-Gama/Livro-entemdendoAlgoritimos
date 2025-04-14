from datetime import datetime	
now = datetime.now()
anoAtual = int(now.strftime("%Y"))

anosAposentBrasil2025 = 35

funcionarios = dict()
funcionarios['nome'] = str(input('Nome: '))
funcionarios ['nascimento'] = int(input('Ano de nascimento: '))
funcionarios['idade'] = anoAtual - funcionarios ['nascimento']
funcionarios['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

if funcionarios['ctps'] != 0:
    funcionarios['anoContratacao'] = int(input('Ano de Contratação: '))
    funcionarios['salario'] = float(input('Salário: '))
    funcionarios['anoAposentadoria'] = funcionarios['anoContratacao'] + anosAposentBrasil2025

print()  # só pra deixar a saída mais limpa
for chave, valor in funcionarios.items():
    print(f"{chave} tem o valor {valor}")
