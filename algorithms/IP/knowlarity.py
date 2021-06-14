l = [10, 20, 30, 40, 50, 60, 70, 80, 90]
k = 80

# Linear Search
for i in range(len(l)):
    if l[i] == k:
        print("{k} found at index {i}".format(k=k, i=i))

# 2nd Linear search

if k in l:
    print("{k} found at {l}".format(k=k, l=l.index(k)))


# Binary Search

def binary_search(arr, k):
    l = 0
    r = len(arr)
    while l < r:
        m = (r + l) // 2
        if arr[m] == k:
            print("{k} found at {l}".format(k=k, l=m))
            return True
        elif arr[m] < k:
            l = m + 1
        else:
            r = m - 1


binary_search(l, k)

# Sorting

l = [10, 5, 2, 11, 1, 6, 9, 0]
# bubble sort

print("list before soerting ", l)
for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[i] > l[j]:
            l[i], l[j] = l[j], l[i]
print("after sorng", l)


# Quicksort

def quicksort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    l = quicksort([x for x in arr[1:] if x < pivot])
    r = quicksort([x for x in arr[1:] if x >= pivot])
    return l + [pivot] + r


l = [10, 5, 2, 11, 1, 6, 9, 0]
# bubble sort

print("list before sorting ", l)
print(quicksort(l))

# Merge sort
# bubble sort

print("list before sorting ", l)


def merge_sort(arr):
    if len(arr) > 1:
        m = len(arr) // 2
        L = arr[m:]
        R = arr[:m]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1


l = [10, 5, 2, 11, 1, 6, 9, 0]
print("before merge sort ", l)
merge_sort(l)
print("after merge sort")
print(l)


# Generator function


def my_gen():
    a = 1
    print("First Gen")
    yield a

    a += 1
    print("2nd gen")
    yield a

    print("3rd gen")
    yield a + 1


a = my_gen()
print(a.__next__())
print(a.__next__())

# Swap Bitwise

x = 23

m = x & 0XAAAAAAAA
print("m ", m)
n = x & 0X55555555
print("n", n)

m = m >> 1
n = n >> 1
print("m", m)
print("n", n)

a = m | n
print("final output", a)
y = bin(x)
z = bin(a)

print(y)

print(z)





stack=[]
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

print(stack)

print(stack.pop(0))
print(stack.pop(0))