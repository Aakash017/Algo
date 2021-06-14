"""List comprehension and MAP"""
from functools import reduce


def num(x):
    return x * x


def rum(x):
    if x % 3 == 0:
        return x


l = [3, 5, 6, 11, 4]

d = map(num, l)
print(list(d))

r = filter(rum, l)
print(list(r))


def add(x, y):
    return x + y


li = [2, 4, 7, 13, 14]
print(reduce(add, li))

# list of cities
cities = ["Berlin", "Vienna", "Zurich"]

# initialize the object
iterator_obj = iter(cities)

print(next(iterator_obj))
print(next(iterator_obj))
print(next(iterator_obj))


def sample_generator(x):
    yield x * x


print(sample_generator(4).__next__())

this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(this_dict["brand"])

# Changing and adding Dictionary Elements
my_dict = {'name': 'Jack', 'age': 27}

# update value

# Output: {'age': 27, 'name': 'Jack'}
print(my_dict)

# add item
my_dict['address'] = 'Downtown'

# Output: {'address': 'Downtown', 'age': 27, 'name': 'Jack'}
print(my_dict)
