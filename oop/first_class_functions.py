'''
First Class Functions:
A programming language is said to have first class functions if it treats its functions as first
class citizens.

First Class Citizens:
First class citizens (first class objects) are entities which support all operations generally available to
other entities. These operations typically include being passed as an argument, returned from a function and
assigned to a variable.

Higher Order Function:
A function which accepts other functions as arguments or returns other functions as a result is called
a higher order function.

Map function:
Takes a function and an array as arguments and runs each value of the array through the function to return
a new array with those results.
'''


# Assigning function to a variable

def square(x):
    return x*x


def cube(x):
    return x*x*x


f = square
print(f(5))


# Accepting function as an argument

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result


squares = my_map(square, [1, 3, 5, 8])

print(squares)


cubes = my_map(cube, [1, 2, 5, 6, 7])
print(cubes)


# Return a function from a function

def logger(msg):
    def log_message():
        print('Log:', msg)

    return log_message


log_hi = logger('Hi')           #Closure
log_hi()

print('\n\n')


def html_tag(tag):
    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))

    return wrap_text


print_h1 = html_tag('h1')
print_h1('Test headline')
print_h1('Another headline')

print_p = html_tag('p')
print_p('Test paragraph.')

