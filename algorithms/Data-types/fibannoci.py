# 1,1,2,3,5,8,13,21..........

s = {}


def fibannoci(n):
    if n in s:
        yield s[n]
    if n == 1:
        value = 1

    elif n == 2:
        value = 1
    elif n > 2:
        value = next(fibannoci(n - 1)) + next(fibannoci(n - 2))
    s[n] = value
    yield value


import sys

for i in range(1, 10101010):
    print(i, " : ", next(fibannoci(i)), "sizer", sys.getsizeof(fibannoci(i)))
