# def uppercase_decorator(function):
#     def wrapper():
#         fn = function()
#         make_uppercase = fn.upper()
#         return make_uppercase
#
#     return wrapper
#
#
# @uppercase_decorator
# def say_hi():
#     return "hello there!"
#
#
# print(say_hi())
#
#
# def uppercase_decorator(fn):
#     def wrapper():
#         f = fn()
#         m = f.upper()
#         return m
#
#     return wrapper
#
#
# @uppercase_decorator
# def say_hi():
#     return "say hi !"
#
#
# print(say_hi())
#
#
# def uppercase(fn):
#     def wrapper():
#         f = fn()
#         return f()
#
#     return wrapper
#
#
# def hello():
#     print("hello")
#
#
# # hello()
#
# @uppercase_decorator
# def hello():
#     print("hello")
#
#
# hello()


def uppercase_decorator(function):
    def wrapper():
        f = function()
        m = f.upper()
        return m
    return wrapper


@uppercase_decorator
def hel():
    return "helo"


print(hel())

import time
from datetime import datetime


def time_taken(func):
    def inner_func(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        print(f"Function : {func.__name__}")
        print(f"Finished in : {(end - start):.2f}s")
        return result

    return inner_func


start_date = datetime.now().strftime("%Y-%m-%d 00:00:00")
end_date = datetime.now().strftime("%Y-%m-%d 23:59:59")


@time_taken
def abc():
    return [x for x in range(1000000000)]


abc()

