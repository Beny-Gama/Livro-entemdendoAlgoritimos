nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3


for j in range(n):
    nums1[m+j] = nums2[j]
nums1.sort()
print(nums1)

# arrey = []
# for n in nums1:
#     if n != 0:
#         arrey.append(n)
# for n in nums2:
#     if n != 0:
#         arrey.append(n)
# arrey.sort()
# print(arrey)