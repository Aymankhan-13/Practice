# Adding logging functionality
def my_logger(originial_func):
    import logging
    logging.basicConfig(filename = '{}.log'.format(originial_func.__name__), level = logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info('Ran with args: {}, kwargs: {}'.format(args, kwargs))
        return originial_func(*args, **kwargs)
    return wrapper


@my_logger
def display():
    print('display() ran')


@my_logger
def display_info(name, age):
    print('display_info() ran with arguments {}, {}'.format(name, age))


display()
display_info('John', 25)