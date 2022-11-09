# def increasingTriplet(nums) -> bool:
#     for i in range(len(nums)):
#         temp = nums[i]
#         c = 0
#         for j in range(i + 1, len(nums)):
#             if nums[j] > temp:
#                 c += 1
#                 temp = nums[j]
#             if c >= 2:
#                 return True
#     return False


# print(increasingTriplet([2, 1, 5, 0, 4, 6]))
# print(increasingTriplet([20, 100, 10, 12, 5, 13]))
# print(increasingTriplet([0, 4, 2, 1, 0, -1, -3]))
# print(increasingTriplet([5, 1, 6]))

# t = [2, 1, 5, 0, 4, 6]
# t = [20, 100, 10, 12, 5, 13]
import math

t = [0, 4, 2, 1, 0, -1, -3]

# t = [1,5,0,4,1,3]

stack = [(1, 0), (5, 1)]


# stack=[]
# stack[(0,2), (1,4),(3,5)]
#
# stack=[0,1, 3]
#
# [2, 1, 5, 0, 4, 6]


# def increasingTriplet(nums) -> bool:
#     stack = []
#     for i in nums:
#         if not stack:
#             stack.append(i)
#         else:
#             if stack[-1] >= i:
#                 for k in stack.copy():
#                     if k >= i:
#                         stack.remove(k)
#                 stack.append(i)
#             else:
#                 stack.append(i)
#     if len(stack) >= 3:
#         return True
#     else:
#         return False


# print(increasingTriplet([2, 1, 5, 0, 4, 6]))
# print(increasingTriplet([20, 100, 10, 12, 5, 13]))
# print(increasingTriplet([0, 4, 2, 1, 0, -1, -3]))
# print(increasingTriplet([5, 1, 6]))
# print(increasingTriplet([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))
# print(increasingTriplet([6, 7, 1, 2]))


def increasingTriplet(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] < nums[j] < nums[k]:
                    return True
    return False


print(increasingTriplet([2, 1, 5, 0, 4, 6]))
print(increasingTriplet([20, 100, 10, 12, 5, 13]))
print(increasingTriplet([0, 4, 2, 1, 0, -1, -3]))
print(increasingTriplet([5, 1, 6]))
print(increasingTriplet(
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1]))
print(increasingTriplet([6, 7, 1, 2]))


def increasingTriplet(nums) -> bool:
    nums1 = math.inf
    nums2 = math.inf
    for i in nums:
        if i < nums1:
            nums1 = i
        elif nums1 < i < nums2:
            nums2 = i
        elif nums2 < i:
            return True
    return False


print(increasingTriplet([2, 1, 5, 0, 4, 6]))
print(increasingTriplet([20, 100, 10, 12, 5, 13]))
print(increasingTriplet([0, 4, 2, 1, 0, -1, -3]))
print(increasingTriplet([5, 1, 6]))
print(increasingTriplet(
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1]))
print(increasingTriplet([6, 7, 1, 2]))
