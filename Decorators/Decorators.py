# there are function decorators and class decorators
# decorators extend the functionality of the function it is added to

# use cases
# Timer decorator to calculate time it takes for function to run
# Debug decorator
# Validator decorator that checks argument values going into a function


import functools

# @mydecorator
# def this_is_my_function():
#     pass


# define the decorator function
def start_end_decorator(func):

    @functools.wraps(func)
    def wrapper():
        print("start")
        func()  # this executes the code in the decorated function
        print("end")
    return wrapper


@start_end_decorator
def print_name():
    print("John")
# start
# John
# end

# print_name()  # this throws an error TypeError: 'NoneType' object is not callable


# define the decorator function
def start_end_decorator_args(func):

    def wrapper(*args, **kwargs):
        print("start")
        result_inner = func(*args, **kwargs)  # this executes the code in the decorated function
        print("end")
        return result_inner

    return wrapper


@start_end_decorator_args
def add5(x):
    print("here")
    return x + 5


# result = add5(4)
# print(result)
# start
# here
# end
# 9


# @functools.wraps(func)
# always use this decorator for the wrapped function inside all decorator functions
# what it does is preserves the wrapped function's identity

# the add5 function uses a decorator function without functools
# because of that checking the function with help returns
# the function wrapper, from within the decorator function

# print(help(add5))
# print(f"Function name: {add5.__name__}")
# Help on function wrapper in module __main__:
#
# wrapper(*args, **kwargs)
#
# None
# Function name: wrapper

# but when using the functools decorator the correct info about the function is returned
# print(help(print_name))
# print(f"Function name: {print_name.__name__}")
# Help on function print_name in module __main__:
#
# print_name()
#
# None
# Function name: print_name


# using an argument in a decorator
# this creates a wrapper around an internal function
# this decorator will repeat the function call a specified number of times
def repeat_decorator(num_times):
    def repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return repeat


@repeat_decorator(num_times=3)
def greet(name):
    print(f"Hello {name}")


# greet("Dave")
# Hello Dave
# Hello Dave
# Hello Dave


# multiple decorators can be applied
# the decorators are applied from top down
# so the top decorator wraps the decorator below it, which wraps whatever is below that

@start_end_decorator_args
@repeat_decorator(num_times=3)
def greet_two(name):
    print(f"Hello {name}")


# greet_two("John")
# start
# Hello John
# Hello John
# Hello John
# end


@repeat_decorator(num_times=3)
@start_end_decorator_args
def greet_three(name):
    print(f"Hello {name}")


# greet_three("Bob")
# start
# Hello Bob
# end
# start
# Hello Bob
# end
# start
# Hello Bob
# end



# class decorators are decorators made out of a class rather than a function
# define a class decorator
class CountCalls:

    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"This is executed {self.num_calls} times.")
        return self.func(*args, **kwargs)


@CountCalls
def say_hello():
    print('Hello')


# say_hello()
# say_hello()
# say_hello()
# This is executed 1 times.
# Hello
# This is executed 2 times.
# Hello
# This is executed 3 times.
# Hello
