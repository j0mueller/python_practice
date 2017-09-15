# Function Header: note the 'def' keyword, function name, parameters(if any), and colon
def hello_world():
  # Optional comment below
  """Prints 'Hello World!' to the console."""
  # Body: note indentation
  print "Hello World!"

# Bill calculation example
def tax(bill):
  """Adds 8% tax to a restaurant bill."""
  bill *= 1.08      # note the *= notation
  print "With tax: %f" % bill
  return bill       # note the 'return' keyword

def tip(bill):
  """Adds 15% tip to a restaurant bill."""
  bill *= 1.15
  print "With tip: %f" % bill   # %f is float placeholder
  return bill

meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)

# Simple example:
def spam():
  """Prints 'Eggs!' to the console."""
	print "Eggs!"

spam()

# squared function
def square(n):
  """Returns the square of a number."""
  squared = n ** 2
  print "%d squared is %d." % (n, squared)  # %d is integer??? placeholder
  return squared

square(10)

# power function
def power(base, exponent):
  result = base ** exponent
  print "%d to the power of %d is %d." % (base, exponent, result)

power(37, 4)


# a function can call another function:
def fun_one(n):
  return n * 5

def fun_two(m):
  return fun_one(m) + 7

# next example
def cube(number):
  return number ** 3

def by_three(number):
  if number % 3 == 0:
    return cube(number)
  else:
    return False


# Importing a MODULE. A module is a file that contains definitions—including variables and functions—that you can use once it is imported. If you dont' specify * or a specific function or variable, you will have to use math. before each method:
import math
print math.sqrt(25)

# Pulling in just a SINGLE FUNCTION from a module is called a FUNCTION IMPORT, and it's done with the FROM keyword:

#from module import function; Now you can just type sqrt() to get the square root of a number—no more math.sqrt()
from math import sqrt

# What if we still want all of the variables and functions in a module but don't want to have to constantly type math.? Universal import can handle this for you.
from math import *

# CAUTION! Universal imports fill your program with lots of variable and function names.
#If you have a function of your very own named sqrt and you import math, your function is safe: there is your sqrt and there is math.sqrt. If you do from math import *, however, you have a problem: namely, two different functions with the exact same name.
#Even if your own definitions don't directly conflict with names from imported modules, if you import * from several modules at once, you won't be able to figure out which variable or function came from where.
#For these reasons, it's best to stick with either import module and type module.name or just import specific variables and functions from various modules as needed.

import math # Imports the math module
everything = dir(math) # Sets everything to a list of things from math
print everything # Prints 'em all!


# Built-in functions: max, min, abs, type
def biggest_number(*args):
  print max(args)
  return max(args)

def smallest_number(*args):
  print min(args)
  return min(args)

def distance_from_zero(arg):
  print abs(arg)
  return abs(arg)

biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)

print type(42)
print type(4.2)
print type('spam')


# examples
def shut_down(s):
  if s == "yes":
    return "Shutting down"
  elif s == "no":
    return "Shutdown aborted"
  else:
    return "Sorry"

def distance_from_zero(number):
  if type(number) == int or type(number) == float:
    return abs(number)
  else:
    return "Nope"

# Vacation Exercise
def hotel_cost(nights):
  return 140 * nights

def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  else:
    # Flights to LA cost $475
    return 475

def rental_car_cost(days):
  cost = 40 * days
  if days >= 7:
    cost -= 50
  elif days >= 3:
    cost -= 20
  return cost

 # Summing up the cost:
 def trip_cost(city, days, spending_money):
  return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money

print trip_cost("Los Angeles", 5, 600)


######### 7: Lists & Functions ##########
n = [1, 3, 5]
n[1] *= 5
print n  # => [1, 15, 5]

# Removing items by index or by item name/value
n.pop(1)  # => removes the item at INDEX 1:  n = [1, 5]
n.remove(1)  # => removes the actual item: n = [3, 5]

# --- --- --- ---
n = [3, 5, 7]

def print_list(x):
  for i in range(0, len(x)):
    print x[i]

print print_list(n)

# WHEN TO USE for item in list VERSUS for i in range(len(list)):
# Method 1 - for item in list:
for item in list:
  print item

#Method 2 - iterate through indexes:
for i in range(len(list)):
  print list[i]

#Method 1 is useful to loop through the list, but it's not possible to modify the list this way.

#Method 2 uses indexes to loop through the list, making it POSSIBLE TO MODIFY THE LIST IF NEEDED. Since we aren't modifying the list, feel free to use either one on this lesson!


# Concatenating Lists:
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]

def flatten(lists):
    results = []
    for numbers in lists:
        for number in numbers:
            results.append(number)
    return results

print flatten(n)

########### BATTLESHIP GAME ##############
board = []
for i in range(5):
    board.append(['O'] * 5)

def print_board(board_in):
  for row in board_in:
    print row

print_board(board)

# ['O', 'O', 'O', 'O', 'O']
# ['O', 'O', 'O', 'O', 'O']
# ['O', 'O', 'O', 'O', 'O']
# ['O', 'O', 'O', 'O', 'O']
# ['O', 'O', 'O', 'O', 'O']

# Edited to remove commas and brackets:
def print_board(board_in):
    for row in board_in:
        print " ".join(row)

# O O O O O
# O O O O O
# O O O O O
# O O O O O
# O O O O O

from random import randint

def random_row(board_in):
    return randint(0, len(board_in) - 1)

def random_col(board_in):
    return randint(0, len(board_in) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
# print ship_row for testing
# print ship_col for testing

# Allow player to take 4 turns before game ends
for turn in range(4):
    print "Turn", turn + 1
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))

    # If guess is correct
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        # If guess is 'off the board'
        # Note: alternative check method:
        # elif guess_row not in range(5) or guess_col not in range(5):
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        # If guess is a repeat
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
    print_board(board)
    if turn == 3:
        print "Game Over"

# Suggestions for additional features and complexity
"""
1. Make multiple battleships: you'll need to be careful because you need to make sure that you don’t place battleships on top of each other on the game board. You'll also want to make sure that you balance the size of the board with the number of ships so the game is still challenging and fun to play.
2. Make battleships of different sizes: this is trickier than it sounds. All the parts of the battleship need to be vertically or horizontally touching and you’ll need to make sure you don’t accidentally place part of a ship off the side of the board.
3. Make your game a two-player game.
4. Use functions to allow your game to have more features like rematches, statistics and more!
"""
