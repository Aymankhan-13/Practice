# Adding timer functionality
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


@my_timer
def display_info(name, age):
    time.sleep(1)
    print('display_info ran with arguments {}, {}'.format(name, age))


display_info('John', 35)