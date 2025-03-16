musicas = [
    ["Bohemian Rhapsody - Queen", 234],
    ["Hotel California - Eagles", 123],
    ["Imagine - John Lennon", 98],
    ["Stairway to Heaven - Led Zeppelin", 176],
    ["Smells Like Teen Spirit - Nirvana", 210],
    ["Billie Jean - Michael Jackson", 143],
    ["Like a Rolling Stone - Bob Dylan", 89],
    ["Shape of You - Ed Sheeran", 265],
    ["Someone Like You - Adele", 132],
    ["Blinding Lights - The Weeknd", 199]
]

# Esse algoritimo busca o menor numero em um arrey/lista...
# Subistitui a lower() em python
def buscaMenor(arr):
    menor = arr[0]
    menor_indice = 0
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice

# print(buscaMenor(musicas))

# A função ordenacaoPorSelecao ordena que subistui a função .sort() em python

def ordenacaoPorSelecao(arr):
    novoArr = []
    for i in range(len(arr)):
        menor = buscaMenor(arr)
        novoArr.append(arr.pop(menor))
    return novoArr

print(ordenacaoPorSelecao([5, 3, 6, 2, 10]))