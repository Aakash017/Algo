"""
Get product ofall other elements
Given an array of integers, return a new array such that each element at index i of the new array is the product of all
the numbers in the original array except the one at i.
For example, ifour input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. Ifourinputwas
[3, 2, 1],
theexpectedoutputwouldbe [2, 3, 6].
Follow-up: What if you can't use division?
"""


def productExceptSelf(nums) -> int:
    product_suffix = []
    product_prefix = []
    target = []
    for i in nums:
        if product_prefix:
            product_prefix.append(product_prefix[-1] * i)
        else:
            product_prefix.append(i)
    _nums = nums[::-1]
    for i in _nums:
        if product_suffix:
            product_suffix.append(product_suffix[-1] * i)
        else:
            product_suffix.append(i)
    product_suffix = product_suffix[::-1]
    print("pre",product_prefix)
    print("suf",product_suffix)
    for i in range(len(nums)):
        if i == 0:
            target.append(product_suffix[i + 1])
        elif i == len(nums) - 1:
            target.append(product_prefix[i - 1])
        else:
            target.append(product_prefix[i - 1] * product_suffix[i + 1])
    return target

print(productExceptSelf([1,2,3,4,5]))