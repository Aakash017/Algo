from functools import reduce


def sqr(a):
    return a * a


def find_odd(a):
    if a % 2 == 0:
        return a


def sun(a, b):
    return a + b


l = [2, 3, 5, 6, 7]

d = map(sqr, l)
print(list(d))

f = filter(find_odd, l)
print(list(f))

r = reduce(sun, l)

print(r)

my_list = ['a', ['bb', 'cc'], 'd']
my_list[1].append('xx')
print(my_list)
d = lambda a: a * 2

print(d(3))
