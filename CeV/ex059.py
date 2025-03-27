n1 = int(input('digite o numero: '))
n2 = int(input('digite um segundo numero: '))
i = 4

while i != 5:
    print('==-==-==-==-==-==-==-==-=')
    print('[ 1 ] somar')
    print('[ 2 ] Multiplicar')
    print('[ 3 ] qual é o maior')
    print('[ 4 ] novos números')
    print('[ 5 ] sair do programa')
    print('==-==-==-==-==-==-==-==-=\n')
    
    i = int(input('>>>> Qual é a sua opsão? \n'))
    

    if i == 1:
        cont = n1 + n2
        print(f'Soma: {n1} + {n2} = {cont}')
    elif i == 2:
        cont = n1 * n2
        print(f'multiplicação: {n1} * {n2} = {cont}')
    elif i == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
        else: 
            print(f'{n2} é maior que {n1}')
    elif i == 4:
        n1 = int(input('Digite o Numero: '))
        n2 = int(input('Digite um Segundo Numero: '))

    elif i == 5:
        print('finalizado!...')
        
    else:
        print('algo deu errado...')


    