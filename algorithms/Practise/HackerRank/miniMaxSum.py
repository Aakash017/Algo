def miniMaxSum(arr):
    # Write your code here
    _sum = sum(arr)
    _max_sum = _sum - min(arr)
    _min_sum = _sum - max(arr)
    print(_max_sum)
    print(_min_sum)


miniMaxSum([1, 3, 5, 7, 9])
