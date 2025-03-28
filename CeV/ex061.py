termo = int(input('Qual é o Pirmerio TERMO: '))
rasao = int(input('Qual é a RASÃO da PA: '))



for i in range(10):
    termo += rasao
    print(f'{termo} -> ',end='')
print('Fim \n')


cont = 0
while cont != 10:
    termo += rasao
    print(f'{termo} -> ',end='')
    cont += 1