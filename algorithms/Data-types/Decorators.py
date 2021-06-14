def uppercase_decorator(function):
    def wrapper():
        fn = function()
        make_uppercase = fn.upper()
        return make_uppercase

    return wrapper


@uppercase_decorator
def say_hi():
    return "hello there!"


print(say_hi())


def uppercase_decorator(fn):
    def wrapper():
        f = fn()
        return f.upper()

    return wrapper


@uppercase_decorator
def say_hi():
    return "say hi !"


print(say_hi())
