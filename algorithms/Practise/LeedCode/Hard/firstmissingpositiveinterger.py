def firstMissingPositive(nums) -> int:
    arr = set(nums)
    print(arr)
    data = (i for i in range(1, len(arr) + 2) if i not in arr)
    return min(data)


print(firstMissingPositive([3, 4, -1, 1]))
