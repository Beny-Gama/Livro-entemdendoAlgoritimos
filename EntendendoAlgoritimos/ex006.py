# algortimo de elclides

# função de soma:
def soma(arr):
    total = 0
    for x in arr:
        total += x
    return total
print('soma:', soma([1,2,3,4]))


# função de soma recursiva: 
def somaRec(arr, total=0):
    if not arr:  # Se a lista estiver vazia, retorna o total acumulado
        return total
    return somaRec(arr[1:], total + arr[0])  # Soma o primeiro elemento e chama recursivamente para o resto da lista
# basicao arrey e vai somado.

print('somaRec:', somaRec([1, 2, 3, 4]))


def somaRecDC(arr):
    if len(arr) == 0:  # Caso base: lista vazia
        return 0
    if len(arr) == 1:  # Caso base: apenas um elemento
        return arr[0]

    meio = len(arr) // 2  # Divide a lista ao meio
    esquerda = somaRecDC(arr[:meio])  # Soma a primeira metade
    direita = somaRecDC(arr[meio:])   # Soma a segunda metade

    return esquerda + direita  # Combina os resultados

print('somaRecDC:', somaRecDC([1, 2, 3, 4, 5]))  # Saída esperada: 10
