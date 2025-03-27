# 283. Move Zeroes

# def moveZeroes(nums):

# qunado eu ordeno a lista, a acho os 0
def moveZeroes(nums):
    # nums.sort()
    less = 0
    greater = len(nums)
    for n in nums:
        media = (less + greater) // 2
        if n < 0:
            break
        if n == 0:
            del nums[0]
            nums.append(0)
    return nums

def moveZeroesDunp1(nums):
    nums.sort()
    for n in nums:
        if n < 0:
            break
        if n == 0:
            del nums[0]
            nums.append(0)
    return nums

nums = [0,1,0,3,12]

print('moveZeroes: ', moveZeroes(nums))
print('moveZeroes: ', moveZeroes(nums))
print('moveZeroesDunp1: ', moveZeroesDunp1(nums))

def quickSort(arr):
    less = []
    equal = []
    greater = []
    
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