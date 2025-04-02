listagem = []
max = 0
min = 0

def refactored():
    while True:
        listagem.append(int(input('Digite um valor: ')))
        v = str(input('Deseja Continuar: [S/N] '))[0] 
        if v in 'Ss':
            break
        

    for c in range(len(listagem)):
        if c == 0:
            max == men = listagem[c]
        else:
            if listagem[c] > max:
                max = listagem[c]
            elif listagem[c] < min:
                min = listagem[c]
        

    print('-='*30)
    print(f'Voce digitou os valores {listagem}')
    print(f'O maior valor digitado for {max} nas posisões', end=' ')

    for i, v in enumerate(listagem):
        if v == max:
            print('f{i}...')
        if v == min:
            print('f{i}...')


def CeV():
    numeros = list()
    while True:
        n = int(input('Figite um valor: '))
        if n not in numeros:
            numeros.append(n)
        r = str(input('Quer continurar? [S/N] '))
        if r in 'Nn':
            break
