def diagonalDifference(arr):
    n = len(arr)
    # find right diagonal sim
    j = 0
    k = 0
    right_s = 0
    for _ in arr:
        right_s += arr[j][k]
        j += 1
        k += 1
    j = 0
    k = n - 1
    l_sum = 0
    for _ in arr:
        l_sum += arr[j][k]
        j += 1
        k -= 1
    print(abs(l_sum - right_s))


diagonalDifference([[1, 2, 3], [4, 5, 6], [9, 8, 9]])
