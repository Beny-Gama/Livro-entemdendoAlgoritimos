termo = int(input('Qual é o Pirmerio TERMO: '))
rasao = int(input('Qual é a RASÃO da PA: '))


cont = 0
break_point = 10
while True:
    print(f'{termo} -> ',end='')
    termo += rasao
    cont += 1
    if cont == break_point:
        mais = int(input('\nQunatos mais termos vc quer colocar? '))
        break_point += mais
        if mais == 0:
            print(f'\nPrgreção finalizada com {break_point} termos mostrados. ')
            break

    