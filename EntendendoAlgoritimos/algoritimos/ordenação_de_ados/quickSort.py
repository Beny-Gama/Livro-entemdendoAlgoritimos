def quickSort(arr):
    less = []
    equal = []
    greater = []
    
    print(arr)
    if len(arr) < 1:
        return arr
    
    pivot = arr[0]

    for i in arr:
        if i < pivot:
            less.append(i)
        elif i > pivot:
            greater.append(i)
        elif i == pivot:
            equal.append(i)
    return (quickSort(less) + equal + quickSort(greater))


array = [16, 0, 1, 4, 3, 6, 8, 10, 0, 10, 13, 15, 17, 2, 0, -1, -2, -3, 100]
print(f'Original Array: {array}')
sorted_array = quickSort(array)
print(f'sorted array: {sorted_array}')


def quickSort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    less = [i for i in arr[1:] if i<= pivot]
    greater = [i for i in arr[1:] if i > pivot]

    return quickSort(less) + [pivot] + quickSort(greater)


arr = [3, 6, 8, 10, 1, 2, 1]


def guickSort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    less, grater = [], []

    for i in arr[1:]:
        if i <= pivot:
            less.append(i)
        else:
            grater.append(i)
    
    return quickSort(less) + [pivot] + quickSort(grater)


arr = [3, 6, 8, 10, 1, 2, 1]
print(quickSort(arr))
