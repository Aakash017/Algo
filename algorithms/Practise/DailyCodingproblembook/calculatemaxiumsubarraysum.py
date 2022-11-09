"""Given an array of numbers, :find the maximum sum of any contiguous subarray of the array.
For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements
42, 14, - 5 , and 86. Given the array [ -5, -1, -8, -9], the maximum sum would be 0,
since we would choose not to take any elements.
Do this in O(n) time."""


def findmaxsubarrasum(array):
    # bruteforce
    max_sum = 0
    for i in range(len(array) - 1):
        for j in range(i, len(array)):
            max_sum = max(max_sum, sum(array[i:j]))
    return max_sum


print(findmaxsubarrasum([34, -50, 42, 14, -5, 86]))


def max_subarray_sum(arr):
    current_max = 0
    for i in range(len(arr) - 1):
        for j in range(i, len(arr)):
            current_max = max(current_max, sum(arr[i:j]))
    return current_max


print(max_subarray_sum([34, -50, 42, 14, -5, 86]))
