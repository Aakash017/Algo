"""
Another sorting method, the counting sort, does not require comparison. Instead, you create an integer array whose
index range covers the entire range of values in your array to sort. Each time a value occurs in the original array,
you increment the counter at that index. At the end, run through your counting array, printing the value of each
non-zero valued index that number of times.
"""


def countingSort(arr):
    # Write your code here
    _z_arr = [0 for i in range(len(arr)-1)]
    for i in arr:
        _z_arr[i] += 1
    return _z_arr


print(countingSort([1, 1, 3, 2, 1]))
