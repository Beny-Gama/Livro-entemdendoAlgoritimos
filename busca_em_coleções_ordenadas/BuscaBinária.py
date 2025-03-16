
def binary_search(arr, target):
    leftPointer = 0
    rightPointer = len(arr) - 1  # Correção do erro de índice

    while leftPointer <= rightPointer:
        half = (leftPointer + rightPointer) // 2  # Correção da divisão inteira
        
        if arr[half] < target:
            leftPointer = half + 1
        else:
            rightPointer = half - 1

    return half + 1

arr = [0, 1, 2, 3, 4, 6, 8, 9, 10, 12, 14, 15, 16]

print(binary_search(arr, 11))  # Correção na chamada da função
