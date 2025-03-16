n1 = int(input('Digite o primero valor: '))
n2 = int(input('Digite o sengundo valor: '))
n3 = int(input('Digite o terceiro valor: '))

lista = [n1, n2, n3]
lista.sort()

print(f'O Menor numero é: {lista[0]}\nO Maior numero é: {lista[-1]}')