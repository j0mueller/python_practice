# Source: https://learnxinyminutes.com/docs/python/ for python v2.7 with insertions for v3.x

####################################################
# 2. Variables and Collections
####################################################

##############  V 2.7  ############### => Print doesn't use parentheses
# Python has a print statement
print "I'm Python. Nice to meet you!"  # => I'm Python. Nice to meet you!

# Simple way to get input data from console
input_string_var = raw_input("Enter some data: ")  # Returns the data as a string
input_var = input("Enter some data: ")  # Evaluates the data as python code
# Warning: Caution is recommended for input() method usage
# Note: In python 3, input() is deprecated and raw_input() is renamed to input()
######################################

##############  V 3.x  ###############  => Use Paretheses w/print
# Python has a print function
print("I'm Python. Nice to meet you!")  # => I'm Python. Nice to meet you!

# By default the print function also prints out a newline at the end.
# Use the optional argument end to change the end string.
print("Hello, World", end="!")  # => Hello, World!

# Simple way to get input data from console
input_string_var = input("Enter some data: ") # Returns the data as a string
# Note: In earlier versions of Python, input() method was named as raw_input()
######################################

# No need to declare variables before assigning to them.
some_var = 5  # Convention is to use lower_case_with_underscores
some_var  # => 5

# Accessing a previously unassigned variable is an exception.
# See Control Flow to learn more about exception handling.
some_other_var  # Raises a name error

# if can be used as an expression
# Equivalent of C's '?:' ternary operator
"yahoo!" if 3 > 2 else 2  # => "yahoo!"

# Lists store sequences
li = []
# You can start with a prefilled list
other_li = [4, 5, 6]

# Add stuff to the end of a list with append
li.append(1)  # li is now [1]
li.append(2)  # li is now [1, 2]
li.append(4)  # li is now [1, 2, 4]
li.append(3)  # li is now [1, 2, 4, 3]
# Remove from the end with pop
li.pop()  # => 3 and li is now [1, 2, 4]
# Let's put it back
li.append(3)  # li is now [1, 2, 4, 3] again.

# Access a list like you would any array
li[0]  # => 1
# Assign new values to indexes that have already been initialized with =
li[0] = 42
li[0]  # => 42
li[0] = 1  # Note: setting it back to the original value
# Look at the last element
li[-1]  # => 3

# Looking out of bounds is an IndexError
li[4]  # Raises an IndexError

# You can look at ranges with slice syntax.
# The start index is included, the end index is not
# (It's a closed/open range for you mathy types.)
li[1:3]  # => [2, 4]
# Omit the beginning
li[2:]  # => [4, 3]
# Omit the end
li[:3]  # => [1, 2, 4]
# Select every second entry
li[::2]  # =>[1, 4]
# Reverse a copy of the list
li[::-1]  # => [3, 4, 2, 1]
# Use any combination of these to make advanced slices
# li[start:end:step]

# Make a one layer deep copy using slices
li2 = li[:]  # => li2 = [1, 2, 4, 3] but (li2 is li) will result in false.

# Remove arbitrary elements from a list with "del"
del li[2]  # li is now [1, 2, 3]

# You can add lists
li + other_li  # => [1, 2, 3, 4, 5, 6]
# Note: values for li and for other_li are not modified.

# Concatenate lists with "extend()"
li.extend(other_li)  # Now li is [1, 2, 3, 4, 5, 6]

# Remove first occurrence of a value
li.remove(2)  # li is now [1, 3, 4, 5, 6]
li.remove(2)  # Raises a ValueError as 2 is not in the list

# Insert an element at a specific index ".insert(index, element)"
li.insert(1, 2)  # li is now [1, 2, 3, 4, 5, 6] again

# Get the index of the first item found
li.index(2)  # => 1
li.index(7)  # Raises a ValueError as 7 is not in the list

# Check for existence in a list with "in"
1 in li  # => True

# Examine the length with "len()"
len(li)  # => 6

# Tuples are like lists but are immutable.
tup = (1, 2, 3)
tup[0]  # => 1
tup[0] = 3  # Raises a TypeError

# You can do all those list thingies on tuples too
len(tup)  # => 3
tup + (4, 5, 6)  # => (1, 2, 3, 4, 5, 6)
tup[:2]  # => (1, 2)
2 in tup  # => True

# You can unpack tuples (or lists) into variables
a, b, c = (1, 2, 3)  # a is now 1, b is now 2 and c is now 3
# You can also do extended unpacking
a, *b, c = (1, 2, 3, 4)  # a is now 1, b is now [2, 3] and c is now 4
d, e, f = 4, 5, 6  # you can leave out the parentheses
# Tuples are created by default if you leave out the parentheses
g = 4, 5, 6  # => (4, 5, 6)
# Now look how easy it is to swap two values
e, d = d, e  # d is now 5 and e is now 4

# Dictionaries store mappings
empty_dict = {}
# Here is a prefilled dictionary
filled_dict = {"one": 1, "two": 2, "three": 3}

# Note keys for dictionaries have to be immutable types. This is to ensure that
# the key can be converted to a constant hash value for quick look-ups.
# Immutable types include ints, floats, strings, tuples.
invalid_dict = {[1,2,3]: "123"}  # => Raises a TypeError: unhashable type: 'list'
valid_dict = {(1,2,3):[1,2,3]}   # Values can be of any type, however.

# Look up values with []
filled_dict["one"]  # => 1

##############  V 2.7  ###############
# Get all keys as a list with "keys()"
filled_dict.keys()  # => ["three", "two", "one"]
# Note - Dictionary key ordering is not guaranteed.
# Your results might not match this exactly.

# Get all values as a list with "values()"
filled_dict.values()  # => [3, 2, 1]
# Note - Same as above regarding key ordering.
######################################

##############  V 3.x  ###############
#We need to wrap the call in list() to turn it into a list. We'll talk about those later.
list(filled_dict.keys())  # => ["three", "two", "one"]
list(filled_dict.values())  # => [3, 2, 1]
######################################

# Get all key-value pairs as a list of tuples with "items()"
filled_dict.items()  # => [("one", 1), ("two", 2), ("three", 3)]

# Check for existence of keys in a dictionary with "in"
"one" in filled_dict  # => True
1 in filled_dict  # => False

# Looking up a non-existing key is a KeyError
filled_dict["four"]  # KeyError

# Use "get()" method to avoid the KeyError
filled_dict.get("one")  # => 1
filled_dict.get("four")  # => None
# The get method supports a default argument when the value is missing
filled_dict.get("one", 4)  # => 1
filled_dict.get("four", 4)  # => 4
# note that filled_dict.get("four") is still => None
# (get doesn't set the value in the dictionary)

# set the value of a key with a syntax similar to lists
filled_dict["four"] = 4  # now, filled_dict["four"] => 4

##############  V 3.x  ###############
#Alternate way to add to a dict as shown above:
filled_dict.update({"four":4})  # => {"one": 1, "two": 2, "three": 3, "four": 4}
######################################

# "setdefault()" inserts into a dictionary only if the given key isn't present
filled_dict.setdefault("five", 5)  # filled_dict["five"] is set to 5
filled_dict.setdefault("five", 6)  # filled_dict["five"] is still 5

# Remove keys from a dictionary with del
del filled_dict["one"]  # Removes the key "one" from filled dict

##############  V 3.5  ###############  <= note version
# From Python 3.5 you can also use the additional unpacking options
{'a': 1, **{'b': 2}}  # => {'a': 1, 'b': 2}
{'a': 1, **{'a': 2}}  # => {'a': 2}
######################################

# Sets store ... well sets (which are like lists but can contain no duplicates)
empty_set = set()
# Initialize a "set()" with a bunch of values
some_set = set([1, 2, 2, 3, 4])  # some_set is now set([1, 2, 3, 4])

##############  V 3.x  ###############
# Initialize a set with a bunch of values. Yeah, it looks a bit like a dict. Sorry.
some_set = {1, 1, 2, 2, 3, 4}  # some_set is now {1, 2, 3, 4}

# Similar to keys of a dictionary, elements of a set have to be immutable.
invalid_set = {[1], 1}  # => Raises a TypeError: unhashable type: 'list'
valid_set = {(1,), 1}
#######################################

# order is not guaranteed, even though it may sometimes look sorted
another_set = set([4, 3, 2, 2, 1])  # another_set is now set([1, 2, 3, 4])

# Since Python 2.7, {} can be used to declare a set
filled_set = {1, 2, 2, 3, 4}  # => {1, 2, 3, 4}

# Add more items to a set
filled_set.add(5)  # filled_set is now {1, 2, 3, 4, 5}

# Do set intersection with &  ("and")
other_set = {3, 4, 5, 6}
filled_set & other_set  # => {3, 4, 5}

# Do set union with |  ("or")
filled_set | other_set  # => {1, 2, 3, 4, 5, 6}

# Do set difference with -
{1, 2, 3, 4} - {2, 3, 5}  # => {1, 4}

# Do set symmetric difference with ^
{1, 2, 3, 4} ^ {2, 3, 5}  # => {1, 4, 5}

# Check if set on the left is a superset of set on the right
{1, 2} >= {1, 2, 3}  # => False

# Check if set on the left is a subset of set on the right
{1, 2} <= {1, 2, 3}  # => True

# Check for existence in a set with in
2 in filled_set  # => True
10 in filled_set  # => False
