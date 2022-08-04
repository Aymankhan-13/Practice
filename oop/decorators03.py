# Multiple functions with parameters
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('wrapper() ran this before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function


@decorator_function
def display():
    print('display() ran')


@decorator_function
def display_info(name, age):
    print('display_info() ran with arguments '.format(name, age))


display()
display_info('John', 25)