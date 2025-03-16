# leetcode: 268. Missing Number

def missingNumber(arr):
    soma1 = 0
    soma2 = 0
    for i, n in enumerate(arr):
        soma1 += i + 1
        soma2 += n
    return soma1 - soma2

arr = [0,1,7,9,3,5,6,4,2]
target = 8

print(missingNumber(arr))