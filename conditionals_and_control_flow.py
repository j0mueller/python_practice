# Control flow gives us this ability to choose among outcomes based off what else is happening in the program.

def clinic():
    print "You've just entered the clinic!"
    print "Do you take the door on the left or the right?"
    answer = raw_input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
        print "This is the Verbal Abuse Room, you heap of parrot droppings!"
    elif answer == "right" or answer == "r":
        print "Of course this is the Argument Room, I've told you that already!"
    else:
        print "You didn't pick left or right! Try again."
        clinic()

clinic()

# NOTE: conditionals include if, else, and elif with a colon at the end of each condition

# 6 control comparators:
# equal (==), not equal (!=), less than and greater than

# Make me false!
bool_two = 3 > 5

# Make me true!
bool_three = 0 == 5 - 5

# Make me false!
bool_four = 3 != 7 - 4

# Make me true!
bool_five = 10 >= 8 + 2


"""
Boolean Operators
------------------------
True and True is True
True and False is False
False and True is False
False and False is False

True or True is True
True or False is True
False or True is True
False or False is False

Not True is False
Not False is True
"""

# AND
# Set bool_one equal to the result of
False and False # False

# Set bool_two equal to the result of
-(-(-(-2))) == -2 and 4 >= 16 ** 0.5    # False

# Set bool_three equal to the result of
19 % 4 != 300 / 10 / 10 and False   # False

# Set bool_four equal to the result of
-(1 ** 2) < 2 ** 0 and 10 % 10 <= 20 - 10 * 2   # True

# Set bool_five equal to the result of
True and True   # True

# OR
# Set bool_one equal to the result of
2 ** 3 == 108 % 100 or 'Cleese' == 'King Arthur'    # True

# Set bool_two equal to the result of
True or False   # True

# Set bool_three equal to the result of
100 ** 0.5 >= 50 or False   # False

# Set bool_four equal to the result of
True or True    # True

# Set bool_five equal to the result of
1 ** 100 == 100 ** 1 or 3 * 2 * 1 != 3 + 2 + 1  # False


# Using the NOT Operator
#Set bool_one equal to the result of
not True    # false

#Set bool_two equal to the result of
not 3 ** 4 < 4 ** 3     # True

#Set bool_three equal to the result of
not 10 % 3 <= 10 % 2    # True

#Set bool_four equal to the result of
not 3 ** 2 + 4 ** 2 != 5 ** 2   # True

#Set bool_five equal to the result of
not not False   # False


# Order of Operations with Booleans:
# Unless parentheses are used,
# 1. not is evaluated first
# 2. and is evaluated next
# 3. or is evaluated last.

# Set bool_one equal to the result of
False or not True and True  # False

# Set bool_two equal to the result of
False and not True or True  # True

# Set bool_three equal to the result of
True and not (False or False)   # True

# Set bool_four equal to the result of
not not True or False and not True  # True

# Set bool_five equal to the result of
False or not (True and True)    #  False

# Note using Bool operators with ints
0 and 2  # => 0
-5 or 0  # => -5
0 == False  # => True
2 == True  # => False
1 == True  # => True

# Comparisons can be chained
1 < 2 < 3    # => True

# Conditional Syntax
# - uses a colon at the end of each condition statement, including the empty 'else' line
# - indents 2 or 4 spaces ?

# Defining functions and using if statements
# Function syntax indents 4 spaces
def using_control_once():
    if 3 < 5:
        return "Success #1"

def using_control_again():
    if 5 > 1:
        return "Success #2"

print using_control_once()
print using_control_again()

answer = "'Tis but a scratch!"

def black_knight():
    if answer == "'Tis but a scratch!":
        return True
    else:
        return False

def french_soldier():
    if answer == "Go away, or I shall taunt you a second time!":
        return True
    else:
        return False

# Feeding a parameter to a function:
def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:
        return -1
    else:
        return 0

print greater_less_equal_5(4)   # returns -1
print greater_less_equal_5(5)   # returns 0
print greater_less_equal_5(6)   # returns 1


# Checking for valid input:
# Checking for blank response:
original = raw_input("Enter a word: ")
if len(original) > 0:
	print original
else:
  	print "empty"

# Checking for letters vs numbers using .isalpha() method
if len(original) > 0 and original.isalpha():
	print original
else:
  	print "empty"

# Next steps
pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
  new_word = new_word[1:len(new_word)]
else:
    print 'empty'

print new_word
#Advanced Tip! When slicing until the end of the string, instead of providing len(new_word), you can also not supply the second index:

my_string = "Python"
my_string[1:] # "ython"
