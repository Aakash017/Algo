# from itertools import permutations
#
# p = permutations(["a", "b", "c"])
# for i in p:
#     print(i)

# from itertools import combinations
#
# comb = combinations([1, 2, 3, 4], 2)
# for i in comb:
#     print(i)


def find_permutation_algo(a, l, r):
    if l == r:
        d = "".join(a)
        print(d)
    else:
        for i in range(l, r + 1):
            a[i], a[l] = a[l], a[i]
            find_permutation_algo(a, l + 1, r)


str_ = "ABC"
n = len(str_)
a = list(str_)
find_permutation_algo(a, 0, n - 1)


def fetch_sub_list(l):
    d = []
    for i in range(len(l) + 1):
        for j in range(i):
            d.append(l[j:i])
    return d


l1 = [1, 2, 3]

print(fetch_sub_list(l1))

chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]


def perform(s):
    stack = []
    for i in range(len(s)):
        if stack and stack[-1][0] == s[i]:
            val, c = stack.pop()
            c = c + 1
            stack.append([s[i], c])
        else:
            c = 1
            stack.append([s[i], c])
    return stack


def string_compress(s):
    result = perform(s)
    ans = []
    for i in result:
        if not i[1] == 1:
            ans.extend(i)
        else:
            ans.append(i[0])
    final = [str(i) for i in ans]
    return "".join(final)


print(string_compress(chars))


# Find Pemutation

def permute(self, nums):
    result = []
    from itertools import permutations
    p = permutations(nums)
    for i in p:
        result.append(list(i))
    return result


def max_product_sub_array(nums):
    N = len(nums)
    if N < 0: return 0
    _max = curr_max = curr_min = nums[0]
    for n in nums[1:]:
        tmp = curr_max
        curr_max = max(curr_max * n, curr_min * n, n)
        curr_min = min(tmp * n, curr_min * n, n)
        _max = max(_max, curr_max)
    return _max


print("mx", max_product_sub_array([2, 3, -2, 4]))
