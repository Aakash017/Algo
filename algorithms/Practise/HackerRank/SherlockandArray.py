"""
Watson gives Sherlock an array of integers. His challenge is to find an element of the array such that the sum of
all elements to the left is equal to the sum of all elements to the right.
"""


def balancedSums(arr):
    # Write your code here
    i = 0
    n = len(arr)
    l_sum = 0
    r_sum = sum(arr)
    while i < n - 1:
        r_sum -= arr[i]
        if l_sum == r_sum:
            return "YES"
        else:
            l_sum += arr[i]
            i += 1
    return "NO"


print(balancedSums([5, 6, 8, 11, 12, 22, 8]))
