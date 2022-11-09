def subsets(nums):
    result = []
    for i in range(0, len(nums) + 1):
        for j in range(0, i):
            result.append(nums[j:i])
    print(result)


subsets([1, 2, 3])

l = 0
r = 0
nums = [1, 2, 3]


def subsets2(nums):
    output = [[]]
    for i in nums:
        output += [lst + [i] for lst in output]
    return output


print(subsets2([1, 2, 3]))
