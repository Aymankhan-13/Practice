# Decorator class
class decorator_class(object):
    def __init__(self, original_func):     # used to pass function into decorator class
        self.original_func = original_func

    def __call__(self, *args, **kwargs):   # used to add functionality to original function
        print('call method executed this before {}'.format(self.original_func.__name__))
        return self.original_func(*args, **kwargs)


@decorator_class
def display():
    print('display() ran')


@decorator_class
def display_info(name, age):
    print('display_info ran with arguments {}, {}'.format(name, age))


display()
display_info('John', 25)

