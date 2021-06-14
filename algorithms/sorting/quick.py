def quick(lst):
    if len(lst) < 2:
        return lst
    pivot = lst[0]
    l = quick([x for x in lst[1:] if x < pivot])
    u = quick([x for x in lst[1:] if x >= pivot])
    return l + [pivot] + u


print(quick([22, 3, 7, 1123, 1234, 11, 43, 123, 433, 55]))
