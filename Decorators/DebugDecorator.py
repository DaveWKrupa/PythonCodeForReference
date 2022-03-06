import functools


def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper


@debug
def print_name():
    print("John")


# print_name()
# Calling print_name()
# John
# 'print_name' returned None

@debug
def print_name2(name):
    print(name)


print_name2("fred")
# Calling print_name2('fred')
# fred
# 'print_name2' returned None

