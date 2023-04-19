import time
from functools import lru_cache

n = 99


@lru_cache(maxsize=n)
def fact(n):
    p = 1
    i = 1
    while i < n + 1:
        p = p * i
        i = i + 1
    yield p


t1 = time.perf_counter()
d = fact(n)
print(d)
print(next(d))
t2 = time.perf_counter()
print("time took in nsecs: ", t2 - t1)
