res = str(input('Digite uma expreção: '))
cont = 0
for n in res:
    if n == '(':
        cont += 1
    if n == ')':
        cont -= 1
    if cont < 0:
        break

if cont == 0:
    print('Sua espreção é possivel! ')
else:
    print('Sua espreção é não possivel! ')
