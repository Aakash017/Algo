"""
https://leetcode.com/problems/unique-number-of-occurrences/

Given an array of integers arr, return true if the number of occurrences of each value in the array is unique, or
false otherwise.

"""


def uniqueOccurrences(arr) -> bool:
    _t = set()
    _c = set()
    for i in arr:
        if i not in _t:
            _c.add(arr.count(i))
            _t.add(i)
    return len(_c) == len(_t)
