#  Move all zeros to starting of list

# TO:DO

a = [2, 0, 4, 0, 5, 5, 0, 9, 0, 0, 1, 0, 0, 1]
n = len(a)
c = 0
for i in range(n):
    if a[i] == 0:
        a[i], a[c] = a[c], a[i]
        c += 1
print(a)

#  Move all zeros to end of list
a = [2, 0, 4, 0, 5, 5, 0, 9, 0, 0, 1, 0, 0, 1]
n = len(a)
c = 0
for i in range(n):
    if a[i] != 0:
        a[i], a[c] = a[c], a[i]
        c += 1
print(a)

# Move all negatives to start of the array

a = [2, -1, 5, -2, 7, 3, 0, 9, -3]
c = 0
n = len(a)
for i in range(n):
    if a[i] < 0:
        a[i], a[c] = a[c], a[i]
        c += 1
print(a)

l1 = [3, 4, 5, 6]
l2 = [5]
d = list(set(l1) | set(l2))
print(d)

# Set operations
A = {0, 2, 4, 6, 8}
B = {1, 2, 3, 4, 5}

print("union", A | B)
print("intersection", A & B)
print("Difference", A - B)

# Python program to check if the list contains three consecutive common numbers in Python
l1 = [3, 4, 5, 6, 6, 6, 7, 9]

for i in range(len(l1) - 2):
    if l1[i] == l1[i + 1] == l1[i + 2]:
        print("three consecutive common number =", l1[i])

# Python | Check if list contains consecutive numbers
a = [2, 3, 1, 4, 5]
l1 = sorted(a)
l2 = [i for i in range(min(a), max(a) + 1)]
print(l1 == l2)

# Convert list to string

l = ["This", "is", "Programming"]
s = ""
print(s.join(l), "s")

# Merge Two Arrays

nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

i = 0
j = 0
while i < m and j < n:
    if nums1[i] > nums2[j]:
        i += 1
    elif nums1[i] < nums2[j]:
        nums1[i] = nums2[j]
        j += 1
    print("nums", nums1)


# Find triplets whose sum is equal to k

def find_triplets(a):
    a.sort()
    n = len(a)
    for i in range(0, n - 1):
        l = i + 1
        r = n - 1
        while l < r:
            if a[i] + a[l] + a[r] == 0:
                print([a[i], a[l], a[r]])
                l += 1
                r -= 1
            elif a[i] + a[l] + a[r] > 0:
                r -= 1
            else:
                l += 1


find_triplets(a=[0, -1, 2, -3, 1])


# python program to find triplets in a given
# array whose sum is zero

# function to print triplets with 0 sum
def findTriplets(arr, n):
    found = False

    # sort array elements
    arr.sort()

    for i in range(0, n - 1):

        # initialize left and right
        l = i + 1
        r = n - 1
        x = arr[i]
        while l < r:

            if x + arr[l] + arr[r] == 0:
                # print elements if it's sum is zero
                print(x, arr[l], arr[r])
                l += 1
                r -= 1
                found = True


            # If sum of three elements is less
            # than zero then increment in left
            elif x + arr[l] + arr[r] < 0:
                l += 1

            # if sum is greater than zero than
            # decrement in right side
            else:
                r -= 1

    if (found == False):
        print(" No Triplet Found")


# Driven source
arr = [0, -1, 2, -3, 1]
n = len(arr)
findTriplets(arr, n)


def lengthOfLongestSubstring(s):
    r = 0
    max = 0
    u = []
    for i in range(0, len(s)):
        if s[i] not in u:
            u.append(s[i])
            r += 1
            n = len(u)
            if max < n:
                max = n
        else:
            while s[i] in u:
                u.pop(0)
            u.append(s[i])
    return max


print("res-", lengthOfLongestSubstring("pwwkew"))

# Group Anagrams
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
