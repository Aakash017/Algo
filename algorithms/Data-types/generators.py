# A simple generator function
import datetime


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


def find_sum_upto_using_gen(n):
    sum = 0
    for i in range(n):
        sum += i
    yield sum

def find_sum_upto(n):
    sum = 0
    for i in range(n):
        sum += i
    return sum


start_time=datetime.datetime.now()
sum = find_sum_upto(100000000)
# sum = find_sum_upto_using_gen(100000000)
print(sum)
# print(sum.__next__())
end_time=datetime.datetime.now()

print("total time ", end_time-start_time)
