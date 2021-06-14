# Find pair having sum close to zero


l = [10, -1, 5, -4, -2, 6]


# Answer is [5,-4] = 1
def quick(lst):
    if len(lst) < 2:
        return lst
    pivot = lst[0]
    l = quick([x for x in lst[1:] if x < pivot])
    u = quick([x for x in lst[1:] if x >= pivot])
    return l + [pivot] + u


def find_pair(lst):
    lst = quick(lst)
    min_l, l = 0, 0
    min_r, r = len(lst) - 1, len(lst) - 1
    min_sum = lst[min_l] + lst[min_r]
    while l < r:
        sum = lst[l] + lst[r]
        if abs(sum) < abs(min_sum):
            min_sum = sum
            min_l = l
            min_r = r
        if sum > 0:
            r -= 1
        else:
            l += 1
    return lst[min_l], lst[min_r]


print(find_pair(l))
