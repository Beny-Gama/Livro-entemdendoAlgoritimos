lista = []
while True:
    num = int(input('Digite um valor: '))
    for n in lista:
        if n <= num:
            lista.insert(n, num)
            break
    else:
        lan()
    res = str(input('Deseja continuar? [S/N] ')).upper()[0]
    if res in 'Nn':
        break
    
print('-='*40)
print('Os valores em erdem decressente são: ', lista)

if 5 in lista:
    print('O valor 5 foi encontrado na lista. ')  
else:
    print('O valor 5 não foi encontrado na lista. ')   
