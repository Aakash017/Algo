# Find count of consecutive 1's
import itertools

nums = [1, 0, 1, 1, 1, 0, 1, 1]


def findMaxConsecutiveOnes(nums):
    c = 0
    r = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            c = 0
        else:
            c += 1
            r = max(r, c)
    return r


print(findMaxConsecutiveOnes(nums=nums))

nums = [12, 345, 2, 6, 7896, 24, 2]


def findNumbers(nums):
    c = 0
    nums = map(str, nums)
    for i in nums:
        if len(i) % 2 == 0:
            c += 1
    return c


print(findNumbers(nums))

# Squares of a Sorted Array
nums = [-4, -1, 0, 3, 10]


def sortedSquares(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    d = [num * num for num in nums]
    d.sort()

    return d


print(sortedSquares(nums))

# Find all Permutations
from itertools import permutations

l = list(permutations(range(1, 4)))
print(l)

a = [1, 2, 3]
p_obj = itertools.permutations(a)
permutations_object = list(p_obj)
print(permutations_object)

a = "AB"

# Duplicates Zero

list1 = [1, 0, 2, 3, 0, 4, 5, 0]
c = 9999
for i in range(len(list1)):
    if i != c:
        if list1[i] == 0:
            list1.pop()
            list1.insert(i + 1, 0)
            c = i + 1
        else:
            c = 0
print(list1)

nums = [3, 2, 2, 3]
v = 3


def removeElement(nums, val):
    nums = [num for num in nums if num != val]
    print(nums)
    return len(nums)


print(removeElement(nums, v))

nums = [1, 1, 2]


def removeDuplicates(nums):
    res = []
    [res.append(x) for x in nums if x not in res]
    return res


print(removeDuplicates(nums))

# Rotate Array Till K
nums = [1, 2, 3, 4, 5, 6, 7]
# output = [7,6,5,1,2,3,4]
# i = 0
# temp=nums[k+1:]
# temp
k = 0
nums = nums[k + 1:] + nums[:k + 1]
print(nums)


# Create Targated array
def createTargetArray(nums, index):
    temp = []
    for i in range(len(index)):
        print(i, nums[i])
        temp.insert(index[i], nums[i])
    return temp


nums = [0, 1, 2, 3, 4]
index = [0, 1, 2, 2, 1]
print("targated array", createTargetArray(nums, index))


# Next Greateest Element

def nextGreaterElements(nums):
    d = dict()
    temp = []
    nums2 = nums + nums
    for i in range(len(nums2)):
        if not nums2[i] in d.keys():
            if nums2[i] < nums2[i + 1]:
                d[nums2[i]] = nums2[i + 1]
            else:
                d[nums2[i]] = -1

    for _ in nums:
        temp.append(d[_])

    return temp


print(nextGreaterElements([5, 4, 3, 2, 1]))


def find_next_greates_element_2(start_index, index, temp, nums):
    for i in range(len(nums) - 1):
        if nums[i] < nums[i + 1]:
            temp.append(nums[i + 1])
    for j in range(start_index, index):
        if nums[j] > nums[index]:
            temp.append(nums[j])

    print("mytemp ", temp)
    return temp


def find_next_greates_element_(nums):
    temp = []
    for i in range(len(nums)):
        find_next_greates_element_2(start_index=0, index=i, temp=temp, nums=nums)


print("mysol", find_next_greates_element_([5, 4, 3, 2]))


def nextGreaterElements(nums):
    _target_array = []

    for _index in range(0, len(nums)):
        # search

        _search_val(_index, nums, _target_array)

    return _target_array


def _search_val(_start_index, _arr, _target_array):
    for _index_1 in range(_start_index, len(_arr)):
        if _arr[_index_1] > _arr[_start_index]:
            _target_array.append(_arr[_index_1])
            return None

    for _index_1 in range(0, _start_index):
        if _arr[_index_1] > _arr[_start_index]:
            _target_array.append(_arr[_index_1])
            return None

    _target_array.append(-1)


# print(nextGreaterElements([5, 4, 3, 2]))


# Python3 program for the above approach

# Function to find the NGE
def printNGE(A, n):
    temp = []
    # Formation of cicular array
    arr = [0] * (2 * n)
    print("arr", arr)

    # Append the given array
    # element twice
    for i in range(2 * n):
        arr[i] = A[i % n]
        print(arr[i], " ,", A[i % n])

    # Iterate for all the
    # elements of the array
    for i in range(n):

        # Initialise NGE as -1
        next = -1

        for j in range(i + 1, 2 * n):

            # Checking for next
            # greater element
            if arr[i] < arr[j]:
                next = arr[j]
                break

        # Print the updated NGE
        print(next, end=", ")
        temp.append(next)
    print("temp ", temp)


# Driver code

# Given array arr[]
arr = [1, 2, 3, 4, 5]

N = len(arr)

# Function call
printNGE(arr, N)

# This code is contributed by Shivam Singh


d = {1: 2, 2: 2, 4: 1}

for i, j in d.items():
    print(i, d[j])


def moveZeroes(nums):
    c = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[c], nums[i] = nums[i], nums[c]
            c += 1
    return nums


print(moveZeroes([1, 2, 0, 4, 0, 5]))


def twoSum(nums, target):
    n = len(nums)
    l = 0
    r = n - 1
    ans = []
    temp = [(num, ind) for num, ind in enumerate(nums)]
    temp.sort(key=lambda x: x[1])
    while l < r:
        if temp[l][1] + temp[r][1] == target:
            ans.append(temp[l][0])
            ans.append(temp[r][0])
            l += 1
            r -= 1
        elif temp[l][1] + temp[r][1] < target:
            l += 1
        else:
            r -= 1
    return ans


print(twoSum([3, 2, 4], 6))
print(twoSum([2, 7, 9, 11], 9))


def isValidSudoku(board):
    l = []
    for i in range(0, 9):
        for j in range(0, 9):
            if board[i][j] != ".":
                r_val = "ROW" + str(i) + "V" + board[i][j]
                l_val = "CLM" + str(j) + "V" + board[i][j]
                board_val = "BOX" + str((i // 3) * 3 + (j // 3)) + "V" + board[i][j]
                newl = [r_val, l_val, board_val]
                for val in newl:
                    if val not in l:
                        l.append(val)
                    else:
                        return False
    print(l)
    return True


print(isValidSudoku([[".", ".", "4", ".", ".", ".", "6", "3", "."], [".", ".", ".", ".", ".", ".", ".", ".", "."],
                     ["5", ".", ".", ".", ".", ".", ".", "9", "."], [".", ".", ".", "5", "6", ".", ".", ".", "."],
                     ["4", ".", "3", ".", ".", ".", ".", ".", "1"], [".", ".", ".", "7", ".", ".", ".", ".", "."],
                     [".", ".", ".", "5", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", "."],
                     [".", ".", ".", ".", ".", ".", ".", ".", "."]]))

# Rotate Image
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# out = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
# d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# c = [7, 4, 1, 8, 5, 2, 9, 6, 3]
# # m1=[]
# # m2=[]
# # m3=[]
# n=len(nums)
# for i in range(n):
#     for j in range(i,n):
#         print(matrix[i][j], matrix[j][i])
#         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
#     for i in matrix:
#         i.reverse()
# print(matrix)


def reverseString(s):
    l = 0
    r = len(s) - 1
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
    return s


s = ["h", "e", "l", "l", "o"]
print("result ", reverseString(s))


def reverseint(i):
    rev = 0
    while i > 0:
        a = i % 10  # remainder
        rev = rev * 10 + a
        i = i // 10  # Quotiont
    return rev


print(reverseint(123))


def firstUniqChar(s: str) -> int:
    for i in s:
        if s.count(i) == 1:
            return s.index(i)


print(firstUniqChar("loveleetcode"))

p = "aakasj"
print(p.count("a"))


def isPalindrome(self, s: str) -> bool:
    l = 0
    r = len(s) - 1
    pal = False
    s = s.lower()
    while l < r:
        if s[l] == s[r]:
            pal = True
            l += 1
            r -= 1
        else:
            pal = False
            return pal
    return pal


s = "A man, a plan, a canal: Panama"


def clean_data(s):
    k = ""
    for i in s:
        if i.isalnum():
            k += i
    return k


from collections import Counter


def count_and_say(s):
    s = Counter(str(s))
    print(s)
    k = ""
    for i, j in s.items():
        k += str(j) + str(i)
    print(k)


count_and_say(14)

strs = ["flower", "flow", "flight"]


def common_prefix(s):
    if len(s) == 0:
        return ""
    elif len(s) == 1:
        return s[0]
    else:
        len_char = 0
        short_str = min(strs, key=len)
        for i in range(len(short_str)):
            if len(set([word[i] for word in strs])) == 1:
                len_char += 1
            else:
                break
    if len_char == 0:
        return ""
    else:
        return short_str[:len_char]


common_prefix(strs)


# Generating permutation using Heap Algorithm
def heapPermutation(a, size):
    # if size becomes 1 then prints the obtained
    # permutation
    if size == 1:
        print(a)
        return

    for i in range(size):
        heapPermutation(a, size - 1)

        # if size is odd, swap 0th i.e (first)
        # and (size-1)th i.e (last) element
        # else If size is even, swap ith
        # and (size-1)th i.e (last) element
        if size & 1:
            a[0], a[size - 1] = a[size - 1], a[0]
        else:
            a[i], a[size - 1] = a[size - 1], a[i]


# Driver code
a = ["a", "b", "c"]
n = len(a)
# heapPermutation(a, n)

a = ["a", "b", "c"]
size = 3
a[0], a[size - 1] = a[size - 1], a[0]
print("a", a)
size = size - 1
a[0], a[size - 1] = a[size - 1], a[0]
print("a", a)
size = size - 1
a[0], a[size - 1] = a[size - 1], a[0]
print("a", a)
size = size - 1
a[0], a[size - 1] = a[size - 1], a[0]
print("a", a)
size = size - 1

from itertools import permutations

p = permutations(["a", "b", "c"])
for i in p:
    print(i)

from itertools import combinations

comb = combinations([1, 2, 3], 2)
for i in list1:
    print(i)


def checkInclusion(s1, s2):
    from itertools import permutations
    p = permutations(["a", "b"])
    for i in p:
        print(i)
    # for i in range (len(s2)):


checkInclusion("ab", "bcadab")


def reveserword(s):
    l = s.strip().split(" ")
    l = [i for i in l if i != ""]
    l.reverse()
    s = " ".join(l)
    return s


print(reveserword("a good   example"))


def find_leader(s):
    result = set()
    for i in range(len(s)):
        max = s[i]
        for j in range(i + 1, len(s)):
            if s[j] > max:
                max = s[j]
        result.add(max)
    return result


print(find_leader([13, 17, 5, 4, 6, 2]))


def find_anagrams(s1, s2):
    from collections import Counter
    n = len(s1)
    d = Counter(s1)
    for i in range(len(s2)):
        val = s2[i:n]
        # print(val)
        s = Counter(val)
        print(s)
        if s == d:
            return True
        n += 1
    return False


print(find_anagrams("abc", "dbacddabc"))


def reverse_strin_3(s):
    l = s.strip().split(" ")
    l = [i[::-1] for i in l if i != ""]
    s = " ".join(l)
    return s


print(reverse_strin_3("Let's take LeetCode contest"))


def compress_string(s):
    n = len(s)
    c = 1
    l = 0
    for i in range(1, n + 1):
        if i < n and s[i] == s[i - 1]:
            c += 1
        else:
            s[l] = s[i - 1]
            l += 1
            if c > 1:
                for k in str(c):
                    s[l] = k
                    l += 1
            c = 1
    s = s[:l]
    print(s)
    return l


print(compress_string(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))

from itertools import combinations

c = combinations(["1", "2", "3", "4"], 3)
print(list(c))



def find_sub_sets(s):
    result = []
    for i in range(len(s)+1):
        for j in range(i)   :
            result.append(s[j:i])
    print(result)

print(find_sub_sets(["1","2","3","4"]))
