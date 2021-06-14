def find_pairs(l, k):
    for i in l:
        if k - i in l:
            print("pair", (i, k - i))


# find_pairs([1, 4, 3, 9, 2, ], 5)


def find_pairs_optimized(l, k):
    i = 0
    j = len(l)-1
    while i < j:
        if l[i] + l[j] == k:
            print(l[i], l[j])
            i += 1
            j -= 1
        elif l[i] + l[j] <= k:
            i += 1
        elif l[i] + l[j] >= k:
            j -= 1


find_pairs_optimized([1, 2, 3, 4, 5, 6], 5)
