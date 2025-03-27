from datetime import datetime

maior, menor, ano_atual = 0, 0, datetime.now().year

for i in range(7):
    ano = int(input('Em que ano {}a pessoa nasceu? '.format(i + 1)))
    if ano_atual - 18 >= ano:
        maior += 1
    else: 
        menor += 1

print(f'Das pessoas, {menor} são maiores, {maior} são maiores.')
