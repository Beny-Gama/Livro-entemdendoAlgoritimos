
def my1():
    numeros = list()
    while True:
        n = int(input('Figite um valor: '))
        if n not in numeros:
            numeros.append(n)
        r = str(input('Quer continurar? [S/N] '))
        if r in 'Nn':
            break

    numeros.sort()
    print('-='*30)
    print(f'Os valores a serem apresentados: {numeros}')


def my2():
    numeros = list()
    while True:
        n = int(input('Figite um valor: '))
        if n not in numeros:
            numeros.append(n)
        r = str(input('Quer continurar? [S/N] '))
        if r in 'Nn':
            break
    
    def quickSort(arr):
        if len(arr) <= 1:
            return arr
    
        pivot = arr[0]
        less = [i for i in arr[1:] if i<= pivot]
        greater = [i for i in arr[1:] if i > pivot]

        return quickSort(less) + [pivot] + quickSort(greater)


    print('-='*30)
    print(f'Os valores a serem apresentados: {quickSort(numeros)}')

    def CeV():
        lista = []
        for c in range(0, 5):
            n = int(input('Digite um valor: '))
            if c == 0 or n > lista[-1]:
                lista.append(n)
                print('Adicionado ao final da lista... ')
            else:
                pos = 0
                while pos < len(lista):
                    if n <= lista[pos]:
                        lista.insert(pos, n)
                        print(f'Adicionado na posição {pos} da lista...')
                        break
                    pos += 1

    print(f'=-'*30)
    print(f'Os valores digitados em ardem foram {lista}')


CeV()