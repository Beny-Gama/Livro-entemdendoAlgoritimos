lista = []
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)

    res = str(input('Deseja continuar? [S/N] ')).upper()[0]
    if res in 'N':
        break

print('-='*40)
lista.sort(reverse=True)
print('Os valores em erdem decressente são: ', lista)
if 5 in lista:
    print('O valor 5 foi encontrado na lista. ')  
else:
    print('O valor 5 não foi encontrado na lista. ')   
