"""
https://leetcode.com/problems/4sum/
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]]
such that:

    0 <= a, b, c, d < n
    a, b, c, and d are distinct.
    nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]


create hash of two elements sum
than sum - elemnets if found in map check for indexes
"""

# nums = [1, 0, -1, 0, -2, 2]
# nums = [-4, -3, -2, -1, 0, 0, 1, 2, 3, 4]
import datetime

# start_time = datetime.datetime.now()
nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20,
        20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30,
        30, 30, 30, 30, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 50, 50, 50, 50,
        50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60,
        60, 60, 60, 60, 60, 60, 60, 60, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70,
        80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 90, 90, 90, 90, 90, 90, 90, 90,
        90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
print(len(nums))

# nums = [-1, 0, 1, 2, -1, -4]

# print(nums)
target = 200
mp = {}
target_arr = set()
nums.sort()
_p = []
# for i in range(len(nums) - 1):
#     for j in range(i + 1, len(nums)):
#         if nums[i] + nums[j] in mp:
#             mp[nums[i] + nums[j]] += [(i, j)]
#         else:
#             mp[nums[i] + nums[j]] = [(i, j)]
#
# print(mp)
# for i in range(len(nums) - 1):
#     # if i > 0 and nums[i] == nums[i - 1]:
#     #     break
#     for j in range(i + 1, len(nums)):
#         # if j > i + 1 and nums[j] == nums[j - 1]:
#         #     break
#         x = target - (nums[i] + nums[j])
#         if x in mp:
#             # print(x)
#             y = mp[x]
#             # print(y)
#             for _y in y:
#                 if i != _y[0] and j != _y[1] and i != _y[1] and j != _y[0]:
#                     _t = (nums[i], nums[j], nums[_y[0]], nums[_y[1]])
#                     _t=tuple(sorted(_t))
#                     target_arr.add(_t)
print(nums[179])
start_time = datetime.datetime.now()
for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums) - 1):
        l = 0
        r = len(nums) - 1
        while l < len(nums) - 1 and r>0:
            # print(i,j,l,r)
            if nums[i] + nums[j] + nums[l] + nums[r] == target:
                if i != l and 1 != r and j != l and j != r:
                    _t = (nums[i], nums[j], nums[l], nums[r])
                    _t = tuple(sorted(_t))
                    target_arr.add(_t)
                    l += 1
                    r -= 1
            if nums[i] + nums[j] + nums[l] + nums[r] < target:
                l += 1
            else:
                r -= 1
print(target_arr)
end_time = datetime.datetime.now()
print("total time", end_time-start_time)


# l=0
# r=len(nums)-1
# while l<r:
#     if target - (nums[l]+nums[r]) in mp:
#
#
# print(target_arr)
# end_time =datetime.datetime.now()
# print("Time took ", end_time-start_time)


# A hashing based Python program to find if there are
# four elements with given summ.

# The function finds four elements with given summ X


def findFourElements(nums, target):
    mp = {}
    target_arr = []
    nums.sort()
    _p = []
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] in mp:
                mp[nums[i] + nums[j]] += [(i, j)]
            else:
                mp[nums[i] + nums[j]] = [(i, j)]

    # print(mp)
    for i in range(len(nums) - 1):
        if i > 0 and nums[i] == nums[i - 1]:
            break
        for j in range(i + 1, len(nums)):
            if j > i + 1 and nums[j] == nums[j - 1]:
                break
            x = target - (nums[i] + nums[j])
            if x in mp:
                # print(x)
                y = mp[x]
                # print(y)
                for _y in y:
                    if i != _y[0] and j != _y[1] and i != _y[1] and j != _y[0]:
                        _t = [nums[i], nums[j], nums[_y[0]], nums[_y[1]]]
                        _t.sort()
                        if _t not in target_arr:
                            target_arr.append(_t)
    return target_arr


# Driver code
import timeit

arr = [10, 20, 30, 40, 1, 2]
n = len(arr)
X = 91

nums = [1, 0, -1, 0, -2, 2]
target = 0


# Function call
# findFourElements(nums, 6, target)

# This is code is contributed by shubhamsingh10

def fourSum(nums, target):
    n = len(nums)

    nums.sort()

    res = set()

    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            low, high = j + 1, n - 1

            while low < high:
                if nums[low] + nums[high] + nums[i] + nums[j] == target:
                    res.add((nums[low], nums[high], nums[i], nums[j]))
                    low += 1
                    high -= 1
                elif nums[low] + nums[high] + nums[i] + nums[j] > target:
                    high -= 1
                else:
                    low += 1
    return res

# nums = [-1, 0, 1, 2, -1, -4]

# print(nums)
# target = -1
# start_time = datetime.datetime.now()
# print("fs", fourSum(
#     [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20,
#      20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30,
#      30, 30, 30, 30, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 50, 50, 50, 50,
#      50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60,
#      60, 60, 60, 60, 60, 60, 60, 60, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70,
#      80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 90, 90, 90, 90, 90, 90, 90, 90,
#      90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90], 200))
# end_time = datetime.datetime.now()
# print("total time , ", end_time - start_time)
