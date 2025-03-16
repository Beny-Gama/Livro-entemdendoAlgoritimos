from datetime import date
ano = int(input('Escolha um data: '))
if ano == 0:
    ano = date.today().year
    print(f'O numero atual é: {ano}')
elif ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano atual {ano} É BISESTO')
else:
    print(f'O ano atual {ano} NÃO É BISESTO')

# cont = -10000
# for n in range(2025):
#     cont += 4
#     if cont == num:
#         print(f'O {num} é Bisesto')
#         break
