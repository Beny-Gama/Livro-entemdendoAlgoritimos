# pesquisa binaria: 
# Encontra a posição de um elemento em uma lista ordenada em log(n).
# Find the element position in a ordeneed list in log(n).

def binary_search(arr, target):
    if target in arr:
        start = 0
        end = len(arr)
        while start <= end:
            mid = (start + end) // 2
            if arr[mid] < target:
                start = mid + 1
            elif arr[mid] > target:
                end = mid - 1
            else:
                return mid
    print('Target not found')

numbers = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7

print(binary_search(numbers, target))