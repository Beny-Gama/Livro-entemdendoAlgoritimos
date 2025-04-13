

def my():
    lista, listaPar, listaImp = list(), list(), list()
    res = 's'

    while res not in 'Nn':
        num = int(input('Digite um numero: '))
        lista.append(num)
        if num % 2 == 0:
            listaPar.append(num)
        else:
            listaImp.append(num)
        res = str(input('Deseja continuar? [N/S] ')).upper()[0]

    print(f'A lista completa é: {lista}')
    print(f'A lista com pares é: {listaPar}')
    print(f'A lista impares é: {listaImp}')

my()

