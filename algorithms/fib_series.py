from datetime import datetime


def fib_series(n):
    if n < 1:
        return n
    elif n < 2:
        n = n + 1
        return n
    else:
        n - 1
        d = fib_series(n)
        return d


# print(fib_series(1))

l = []


def fib_s2(n):
    for i in range(n + 1):
        if i < 2:
            l.append(i)
        else:
            d = l[i - 1] + l[i - 2]
            l.append(d)
    # print(l)
    yield l.pop()


start_time = datetime.now()
print(fib_s2(300000))
# print(fib_s2(300000))
end_time = datetime.now()
print(start_time)
print(end_time)
