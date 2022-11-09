"""Given an array of integers that are out of order, determine the bounds of the smallest window that must be sorted
 in order for the entire array to be sorted. For example, given[3, 7, 5, 6, 9],
 youshouldreturn(1, 3).
"""


def window(array):
    l, r = None, None
    _new_arr = sorted(array)
    for i in range(len(array)):
        if array[i] != _new_arr[i] and l is None:
            l = i
        elif array[i] != _new_arr[i]:
            r = i
    print(l, r)


window([3, 7, 5, 6, 9])
window([9, 5, 3, 7, 6])
