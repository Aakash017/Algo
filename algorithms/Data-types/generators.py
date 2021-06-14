# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


# a=my_gen()
# next(a)
# next(a)
# next(a)
# next(a)
# next(a)
# next(a)
# next(a)


def find_sum_upto(n):
    sum = 0
    for i in range(n):
        sum += i
    yield sum


sum = find_sum_upto(100000000)
print(sum.__next__())