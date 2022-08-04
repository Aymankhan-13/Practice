# Adding logging and timer decorators on same function
def my_logger(original_func):
    import logging
    logging.basicConfig(filename = '{}.log'.format(original_func.__name__), level = logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info('Ran with args: {}, AND kwargs: {}'.format(args, kwargs))
        return original_func(*args, **kwargs)
    return wrapper


def my_timer(original_func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(original_func.__name__, t2))
        return result
    return wrapper


import time

'''
the following stacking will create a different file called wrapper.log whereas 
stacking my_timer on top of my_logger will display 'wrapper' in the console
'''


@my_logger          # same as my_logger(my_timer(display_info))
@my_timer
def display_info(name, age):
    time.sleep(1)
    print('display_info ran with arguments {}, {}'.format(name, age))


display_info('John', 35)



