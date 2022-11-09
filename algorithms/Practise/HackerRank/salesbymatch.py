def sockMerchant(n, ar):
    # Write your code here
    _set_a = set(ar)
    c = 0
    for i in _set_a:
        c += ar.count(i) // 2
    return c