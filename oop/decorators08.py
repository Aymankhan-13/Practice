# Fixing issue from decorators07 using functools

from functools import wraps


def my_logger(original_func):
    import logging
    logging.basicConfig(filename = '{}.log'.format(original_func.__name__), level = logging.INFO)

    @wraps(original_func)
    def wrapper(*args, **kwargs):
        logging.info('Ran with args: {}, AND kwargs: {}'.format(args, kwargs))
        return original_func(*args, **kwargs)
    return wrapper


def my_timer(original_func):
    import time

    @wraps(original_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(original_func.__name__, t2))
        return result
    return wrapper


import time


@my_logger          # same as my_logger(my_timer(display_info))
@my_timer
def display_info(name, age):
    time.sleep(1)
    print('display_info ran with arguments {}, {}'.format(name, age))

'''
after commenting out @my_logger and @my_timer, run the following to make sure functools is working:

display_info = my_timer(display_info)
print(display_info.__name__)

O/p should be display_info
'''
display_info('Tom', 68)
