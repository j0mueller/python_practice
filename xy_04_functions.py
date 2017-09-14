# Source: https://learnxinyminutes.com/docs/python/ for python v2.7 with insertions for v3.x

####################################################
# 4. Functions
####################################################

# Use "def" to create new functions
def add(x, y):
    print "x is {0} and y is {1}".format(x, y)
    # v3.x => print("x is {} and y is {}".format(x, y))
    return x + y  # Return values with a return statement


# Calling functions with parameters
add(5, 6)  # => prints out "x is 5 and y is 6" and returns 11

# Another way to call functions is with keyword arguments
add(y=6, x=5)  # Keyword arguments can arrive in any order.


# You can define functions that take a variable number of
# positional args, which will be interpreted as a tuple by using *
def varargs(*args):
    return args

varargs(1, 2, 3)  # => (1, 2, 3)

# You can define functions that take a variable number of
# keyword args, as well, which will be interpreted as a dict by using **
def keyword_args(**kwargs):
    return kwargs


# Let's call it to see what happens
keyword_args(big="foot", loch="ness")  # => {"big": "foot", "loch": "ness"}


# You can do both at once, if you like
def all_the_args(*args, **kwargs):
    print args
    print kwargs

"""
all_the_args(1, 2, a=3, b=4) prints:
    (1, 2)
    {"a": 3, "b": 4}
"""

# When calling functions, you can do the opposite of args/kwargs!
# Use * to expand positional args and use ** to expand keyword args.
args = (1, 2, 3, 4)
kwargs = {"a": 3, "b": 4}
all_the_args(*args)  # equivalent to foo(1, 2, 3, 4)
all_the_args(**kwargs)  # equivalent to foo(a=3, b=4)
all_the_args(*args, **kwargs)  # equivalent to foo(1, 2, 3, 4, a=3, b=4)

# you can pass args and kwargs along to other functions that take args/kwargs by expanding them with * and ** respectively
def pass_all_the_args(*args, **kwargs):
    all_the_args(*args, **kwargs)
    print varargs(*args)
    print keyword_args(**kwargs)

##############  V 3.x  ###############
# Returning multiple values (with tuple assignments)
def swap(x, y):
    return y, x  # Return multiple values as a tuple without the parenthesis.
# (Note: parenthesis have been excluded but can be included)

x = 1
y = 2
x, y = swap(x, y)     # => x = 2, y = 1
# (x, y) = swap(x,y)  # Again parenthesis have been excluded but can be included.
######################################


# Function Scope
x = 5

def set_x(num):
    # Local var x not the same as global variable x
    x = num  # => 43
    print x  # => 43    # v3.x => print(x)


def set_global_x(num):
    global x
    print x  # => 5     # v3.x => print(x)
    x = num  # global var x is now set to 6
    print x  # => 6     # v3.x => print(x)


set_x(43)
set_global_x(6)


# Python has first class functions
def create_adder(x):
    def adder(y):
        return x + y
    return adder

add_10 = create_adder(10)
add_10(3)  # => 13

# There are also anonymous functions
(lambda x: x > 2)(3)  # => True
(lambda x, y: x ** 2 + y ** 2)(2, 1)  # => 5

# There are built-in higher order functions
map(add_10, [1, 2, 3])  # => [11, 12, 13]
map(max, [1, 2, 3], [4, 2, 1])  # => [4, 2, 3]

filter(lambda x: x > 5, [3, 4, 5, 6, 7])  # => [6, 7]

##############  V 3.x  ###############  => wrap with 'list'
list(map(add_10, [1, 2, 3]))          # => [11, 12, 13]
list(map(max, [1, 2, 3], [4, 2, 1]))  # => [4, 2, 3]

list(filter(lambda x: x > 5, [3, 4, 5, 6, 7]))  # => [6, 7]
######################################

# We can use list comprehensions for nice maps and filters
[add_10(i) for i in [1, 2, 3]]  # => [11, 12, 13]
[x for x in [3, 4, 5, 6, 7] if x > 5]  # => [6, 7]

# You can construct set and dict comprehensions as well.
{x for x in 'abcddeef' if x in 'abc'}  # => {'a', 'b', 'c'}
{x: x ** 2 for x in range(5)}  # => {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
