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
people_list = people_list(1000000)
t2 = time.perf_counter_ns()
print("people_list = ", sys.getsizeof(people_list) / (1024 * 1024), "MB")
# print('Took {} NanoSeconds'.format(t2 - t1))

t11 = time.perf_counter_ns()
people_gen = people_generator(1000000)
for _ in people_gen:
    # print(p)
    __s = _

t22 = time.perf_counter_ns()
print("people_gen = ", sys.getsizeof(people_gen) / (1024 * 1024), "MB")
print('Took {} NanoSeconds'.format(t22 - t11))


def time_taken(func):
    def inner_func(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        print(f"Function : {func.__name__}")
        print(f"Finished in : {(end - start):.2f}s")
        print(f"Memory in KB: {sys.getsizeof(result)/1024}")
        return result

    return inner_func


@time_taken
def funa():
    l = []
    for i in range(1000000):
        l.append(i)



@time_taken
def funb():
    for i in range(1000000):
        yield i


funa()
# b = funb()
# m = []
# for i in b:
#     print(i)
# print("execution completed.")
# print(sys.getsizeof(b) / (1024 * 1024), "MB")
#
# import sys
#
# list_1 = [x for x in range(100000000)]
# for i in range(10):
#     print(list_1[i])
# print("size of list_1 = ", sys.getsizeof(list_1) / (1024 * 1024), " MB")
#
# for i in range(100):
#     print("list1 =", list_1[i])
#
# gen_1 = (x for x in range(100000000))
# print("size of gen_1 = ", sys.getsizeof(gen_1) / (1024 * 1024), " MB")
#
# c = 0
# for i in gen_1:
#     print("gen1 ", i)
#     if c > 100:
#         break
#     else:
#         c += 1
