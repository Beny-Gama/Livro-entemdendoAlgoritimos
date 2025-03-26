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
# print('moveZeroes: ', moveZeroes(nums))
print('moveZeroes: ', moveZeroes(nums))
print('moveZeroesDunp1: ', moveZeroesDunp1(nums))
