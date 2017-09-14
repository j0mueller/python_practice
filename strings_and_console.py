brian = "Hello life!"
print brian

# Escaping characters - use the backslash
'This isn\'t flying.'

# Access by index (each char in a string has an index)

c = "cats"[0]
n = "Ryan"[3]

# String methods:
#len() gives the length of a string
parrot = "Norwegian Blue"
print len(parrot)

#lower() remove all capitalization
parrot.lower()  # result: norwegian blue

#upper() makes all upper case
parrot.upper()  # result: NORWEGIAN BLUE

#str() converts non-strings to strings
pi = 3.14
str(pi) # converts 3.14 to "3.14"

# Methods that use dot notation ONLY work with strings.
# On the other hand, len() and str() can work on other data types.

# Adding strings (i.e., concatenation) with or without +
print "Life " + "of " + "Brian"
print "Life " "of " "Brian"

# Multiplying strings
"Hello" * 3 # => HelloHelloHello

# Explicit string converstion
print "I have " + str(2) + " coconuts!"

# String Formatting with %: (will be DEPRECATED in v3.1)
string_1 = "Camelot"
string_2 = "place"
print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)
print "The %s who %s %s!" % ("Knights", "say", "Ni")

# String formatting with .format (PREFERRED!):
"{} is a {}".format("This", "placeholder")
"{0} can be {1}".format("strings", "formatted")
# You can use keywords if you don't want to count.
"{name} wants to eat {food}".format(name="Bob", food="lasagna")

# Getting input in the console using "raw_input" combined with the question prompt:
name = raw_input("What is your name? ")
quest = raw_input("What is your quest? ")
color = raw_input("What is your favorite color? ")

print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color)


# Section SUMMARY

#Three ways to create strings
'Alpha'
"Bravo"
str(3)

#String methods
len("Charlie")
"Delta".upper()
"Echo".lower()

#Printing a string
print "Foxtrot"

#Advanced printing techniques
g = "Golf"
h = "Hotel"
print "%s, %s" % (g, h)
