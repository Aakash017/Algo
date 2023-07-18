#   Created by Elshad Karimov on 04/04/2020.
#   Copyright © 2020 AppMillers. All rights reserved.
import array as arr

from array import *


# 1. Create an array and traverse.
#
# my_array = arr.array('i',[1,2,3,4,5])
#
# for i in my_array:
#     print(i)
#
#
# # 2. Access individual elements through indexes
# print("Step 2")
# print(my_array[3])
#
# # 3. Append any value to the array using append() method
#
# print("Step 3")
# my_array.append(6)
# print(my_array)
#
# # 4. Insert value in an array using insert() method
# print("Step 4")
# my_array.insert(3, 11)
# print(my_array)
#
#
# # 5. Extend python array using extend() method
# print("Step 5")
# my_array1 = array('i', [10,11,12])
# my_array.extend(my_array1)
# print(my_array)
#
# # 6. Add items from list into array using fromlist() method
# print("Step 6")
# tempList = [20,21,22]
# my_array.fromlist(tempList)
# print(my_array)
#
# # 7. Remove any array element using remove() method
# print("Step 7")
# my_array.remove(11)
# print(my_array)
#
# # 8. Remove last array element using pop() method
# print("Step 8")
# my_array.pop()
# print(my_array)
#
# # 9. Fetch any element through its index using index() method
# print("Step 9")
# print(my_array.index(21))
#
# # 10. Reverse a python array using reverse() method
# print("Step 10")
# my_array.reverse()
# print(my_array)
#
# # 11. Get array buffer information through buffer_info() method
# print("Step 11")
# print(my_array.buffer_info())
#
# # 12. Check for number of occurrences of an element using count() method
# print("Step 12")
# my_array.append(11)
# print(my_array.count(11))
# print(my_array)
# # 13. Convert array to string using tostring() method
# print("Step 13")
# strTemp = my_array.tostring()
# print(strTemp)
# ints = array('i')
# ints.fromstring(strTemp)
# print(ints)
#
# # 14. Convert array to a python list with same elements using tolist() method
# print("Step 14")
# # print(my_array.tolist())
# # 15. Append a string to char array using fromstring() method
#
# # 16. Slice Elements from an array
# print("Step 16")
# print(my_array[:])
#

# def twoSum(nums, target: int) :
#     seen = {}
#     for i in range(len(nums)):
#         if nums[i] in seen.keys():
#             return [seen[nums[i]], i]
#         else:
#             num_j = target - nums[i]
#             seen[num_j] = i
#
#         # if num_j not in seen:
#         #     seen.add(num_j)
#         # else:
#         #     return [seen[0],i]
#     print(seen)
#
#
# print(twoSum([2,7,11,15],9))

def diagonal_sum(matrix):
    # TODO
    _left_dia = 0
    _right_dia = 0
    r, c = 0, 0
    for i in range(len(matrix)):
        _left_dia += matrix[r][c]
        r += 1
        c += 1
    r = 0
    c = len(matrix) - 1
    print(c)
    print("_left_dia", _left_dia)
    for i in range(len(matrix)):
        print(matrix[r][c])
        _right_dia += matrix[r][c]
        c -= 1
        r += 1
    return _left_dia + _right_dia


myList2D = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# print(diagonal_sum(myList2D))


def pair_sum(myList, sum):
    # TODO
    out = []
    for i in range(len(myList)):
        for j in range(i + 1, len(myList)):
            if myList[i] + myList[j] == sum:
                out.append(str(myList[i]) + "+" + str(myList[j]))
    return out


# print(pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9], 7))


def rotate(matrix):
    # TODO
    # [[1,2,3],[4,5,6],[7,8,9]]
    # [[7,4,1],[8,5,2],[9,6,3]]
    r = 0
    c = len(matrix[0]) - 1
    for m in matrix:
        for i in m:
            matrix[r][c] = i
            r += 1
        c -= 1
        r = 0


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate(matrix)
print(matrix)
