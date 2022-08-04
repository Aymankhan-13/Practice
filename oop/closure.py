'''
Closure is an inner function that remembers and has access to variables
in the local scope in which it was created even after the outer function is done executing
'''


def outer_func():
    message = 'Hi'

    def inner_func():
        print(message) # free variable - not defined w/n inner_func but we still have access to it

    return inner_func


my_func = outer_func()
print(my_func.__name__)
my_func()