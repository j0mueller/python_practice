################ WHILE LOOPS ##################

# 1: validate input
choice = raw_input('Enjoying the course? (y/n)')
while choice != 'y' and choice != 'n':
    choice = raw_input("Sorry, I didn't catch that. Enter again: ")

# 2: While loop set to 'True' - guaranteed to run at least once. Uses 'if -- break' to exit loop.
count = 0
while True:
    print count
    count += 1
    if count >= 10:
        break

# 3: While / else loops - The else block executes when the while condition becomes false.
import random   # <=  notice difference with ex. 4

print "Lucky Numbers! 3 numbers will be generated."
print "If one of them is a '5', you lose!"

count = 0
while count < 3:
    num = random.randint(1, 6)  # <=  notice difference with ex. 4
    print num
    if num == 5:
        print "Sorry, you lose!"
        break
    count += 1
else:
    print "You win!"

# 4: Above, but with user input:
from random import randint   # <=  notice difference with ex. 3

random_number = randint(1, 10)  # <=  notice difference with ex. 3
guesses_left = 3

while guesses_left > 0:
    guess = int(raw_input("Your guess: "))
    if guess == random_number:
        print "You win!"
        break
    guesses_left -= 1
else:
    print "You lose."


################ FOR LOOPS ##################

# 5. Do something a specific number of times
hobbies = []
for i in range(3):
    hobby = raw_input("Enter a hobby:")
    hobbies.append(hobby)
print hobbies


# 6. Print individual characters in a word:
thing = "spam!"
for c in thing:
    print c


# 7. For loop with an 'if' statement
#    Note the use of trailing comma when printing to keep output  #    all on the same line
phrase = "A bird in the hand..."

# Add your for loop
for char in phrase:
  if char == "A" or char == "a":
    print "X",
  else:
    print char,


# 8. Looping through a dictionary
d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in d:
    # Your code here!
    print "{} {}".format(key, d[key])
# =>
# a apple
# c cherry
# b berry

# 9. Using the enumerate function to get index value
choices = ['pizza', 'pasta', 'salad', 'nachos']

print 'Your choices are:'
for index, item in enumerate(choices):
    print index + 1, item
# =>
# Your choices are:
# 1 pizza
# 2 pasta
# 3 salad
# 4 nachos

# 10. Using the zip function to pair elements in 2 or more lists: zip will create pairs of elements when passed two lists, and will stop at the end of the shorter list. zip can handle three or more lists as well!
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
    if a > b:
        print a
    else:
        print b


# 11.  For / else loops: the else block executes if the for loop ends normally. But if there is a break within the for loop that is activated, else does not execute.
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'
for f in fruits:
    if f == 'tomato':
        print 'A tomato is not a fruit!'
        break
    print 'A', f
else:
    print 'A fine selection of fruits!'
# =>
# You have...
# A banana
# A apple
# A orange
# A tomato is not a fruit!
