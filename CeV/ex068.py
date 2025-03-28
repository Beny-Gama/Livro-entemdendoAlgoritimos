from random import randint

print('-='*15)
print('vamos jogar par ou impar'.upper())
cont = 0

while True:
    print('-='*15)
    num = int(input('Diga um Valor: '))
    valor = str(input('Par ou Impar [P/I]')).upper()[0]

    PC_num = randint( 1, 100 )
    soma = PC_num + num

    if soma % 2 == 0:
        resultado = 'Par'
    else:
        resultado = 'Impar'


    print("-"*20)
    print(f'Você jogou {num} e o computador {PC_num}. A Soma é de {soma} o reultada {resultado}.')
    print("-"*20)
    

    if resultado == 'Par' and valor == 'P':
        print('Vocé Venceu!')
        cont += 1
    elif resultado == 'Impar' and valor == 'I':
        print('Vocé Venceu!')
        cont += 1
    else:
        print('Vocé Perdeu!')
        print(f"GAME OVER!!!")
        if cont != 0: print(f'Vocé ganhou {cont} veses')
        break
    print('VAMOS JOGAR DENOVO!!!')

    