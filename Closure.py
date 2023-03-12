# Closures
'''    A closure is the combination of a function bundled together (enclosed) with references to its surrounding state (the lexical environment). 
    In other words, a closure gives you access to an outer function's scope from an inner function. 
    
    More info: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures
'''

import logging
logging.basicConfig(filename='example.log', level=logging.INFO)


def logger(func):
    def log_func(*args):
        logging.info(
            'Running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))
    return log_func


def add(x, y):
    return x+y


def sub(x, y):
    return x-y

add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3, 3)
add_logger(4, 5)

sub_logger(10, 5)
sub_logger(20, 10)

# # example.log file content
# INFO:root:Running "add" with arguments (3, 3)
# INFO:root:Running "add" with arguments (4, 5)
# INFO:root:Running "sub" with arguments (10, 5)
# INFO:root:Running "sub" with arguments (20, 10)
