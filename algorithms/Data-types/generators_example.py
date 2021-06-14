import random
import time
import sys

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']


def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    return result


def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield person


t1 = time.perf_counter_ns()
people = people_list(1000000)

# people = people_generator(1000000)
for p in people:
    print(p)
t2 = time.perf_counter_ns()
print(sys.getsizeof(people), "memory size")
print('Took {} NanoSeconds'.format(t2 - t1))


def func(a):
    yield a


a = [1, 3, 4]
b = func(a)
print(next(b))


def funb(a):
    return a


a = [1, 3, 4]
b = funb(a)
print(b)
