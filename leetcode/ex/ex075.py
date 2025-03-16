def quicksort(arr, left, right):
    if left < right:
        pi = partition(arr, left, right)
        quicksort(arr, left, pi - 1)
        quicksort(arr, pi + 1, right)


def partition(arr, left, right):
    pivot = arr[right]

    i = left - 1

    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[right] = arr[right], arr[i+1]

    return i + 1

nums = [3,2,1,0,4,7,9,8,6,5]
quicksort(nums, 0, len(nums)-1)
print(nums)