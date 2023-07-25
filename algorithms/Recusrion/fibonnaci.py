"""
f(n)=f(n-1)+f(n-2)
"""
from functools import lru_cache

n = 100


# @lru_cache(maxsize=n)
def fab_no(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fab_no(n - 1) + fab_no(n - 2)


print(fab_no(100))
