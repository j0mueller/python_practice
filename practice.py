# 1. Function to check if number is an integer
def is_int(x):
    absolute = abs(x)
    rounded = round(absolute)
    return absolute - rounded == 0


# 2. Function that iterates through digits in a number
# Integers are not iterable and must be turned into strings first
# Then turned back into numbers for summing
def digit_sum(num):
    string = str(num)
    digits = []
    for digit in string:
        digits.append(int(digit))
    return sum(digits)

print digit_sum(7386) # => 24


# 3. Factorial Function
def factorial(x):
    factorial = 1
    while x > 1:
        factorial = factorial * x
        x -= 1
    return factorial

# 4. Prime number checker
def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
        return True

# 5. Reverse a string
def reverse(text):
    word = ""                   # initialize empty string for reversed word
    l = len(text) - 1           # gives last index of word based on length
    while l >= 0:               # index will go to zero
        word = word + text[l]   # letters added from end based on index
        l -= 1                  # index is decremented
    return word


# 6. Returning string stripped of vowels
def anti_vowel(text):
    phrase = ""
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for c in text:
        if c not in vowels:
            phrase = phrase + c
    return phrase

# 7. Accessing values based on keys that match chars iterated thru in a word
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

def scrabble_score(word):
    word_score = 0
    for c in word:
        word_score += score[c.lower()]  # accept uppercase input
    return word_score


# 8. Using string.split() and " ".join(list)
def censor(text, word):
    words = text.split()
    result = ''
    stars = '*' * len(word)
    count = 0
    for i in words:
        if i == word:
            words[count] = stars
        count += 1
    result =' '.join(words)

    return result

# 9. Count # of times item occurs in a list
def count(sequence, item):
    count = 0
    for i in sequence:
        if i == item:
            count += 1
    return count


# 10. Remove odds from list of numbers
def purify(numbers):
    new_list = []
    for number in numbers:
        if number % 2 == 0:
            new_list.append(number)
    return new_list

# 11. Multiply all items in a list
def product(numbers):
    product = 1
    for number in numbers:
        product *= number
    return product

# 12.
def remove_duplicates(list):
  new_list = []
  for element in list:
    if element not in new_list:
      new_list.append(element)
  return new_list

# 13.
def median(lst):
    sorted_list = sorted(lst)
    if len(sorted_list) % 2 != 0:
        #odd number of elements
        index = len(sorted_list)//2
        return sorted_list[index]
    elif len(sorted_list) % 2 == 0:
        #even no. of elements
        index_1 = len(sorted_list)/2 - 1
        index_2 = len(sorted_list)/2
        mean = (sorted_list[index_1] + sorted_list[index_2])/2.0
        return mean

print median([2, 4, 5, 9])

# 14 - 15 - 16 - 17: Sum, Average, Variance, Std Dev
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
  count = 0
  for score in scores:
    count += score
  return count
print grades_sum(grades)

def grades_average(grades_input):
  average = grades_sum(grades_input) / float(len(grades_input))
  return average
print grades_average(grades)

def grades_variance(scores):
  average = grades_average(scores)
  variance = 0
  for score in scores:
    variance += (average - score)**2
  return variance / len(scores)
print grades_variance(grades)

def grades_std_deviation(variance):
  return variance ** 0.5
variance = grades_variance(grades)
print grades_std_deviation(variance)

# 18. Use .items() to access elements in a dictionary
# .items() returns an ARRAY of TUPLES (not in order!)
my_dict = {"one": "dog", "two": 2, "three": [4, 5, 6], "four": True}

print my_dict.items()
# => [
#     ('four', True),
#     ('three', [4, 5, 6]),
#     ('two', 2),
#     ('one', 'dog')
#    ]

print my_dict.keys() # => returns array of keys
print my_dict.values() # => returns array of values

# 19. Use 'in' to iterate over: lists, tuples, dicts, Strings
my_dict = {
  'name': 'Nick',
  'age':  31,
  'occupation': 'Dentist',
}

for key in my_dict:
  print key, my_dict[key]


# 20. List Comprehensions: a powerful way to generate lists using the for/in and if keywords
evens_to_50 = [i for i in range(51) if i % 2 == 0]
new_list = [x for x in range(1, 6)]  # => [1, 2, 3, 4, 5]
doubles = [x * 2 for x in range(1, 6)] # => [2, 4, 6, 8, 10]
doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0] # => [6]
# Squares of the even numbers between 1 to 11.
even_squares = [x ** 2 for x in range(1, 12) if x % 2 == 0]
# Cubes of numbers from 1-10 if the number is divible by 4
cubes_by_four = [x ** 3 for x in range(1, 11) if (x ** 3) % 4 == 0]

# 21. List slicing [start:end:stride]
# "start" = where the slice starts (inclusive)
# "end" = where the slice ends (exclusive)
# "stride" = space between items (e.g., 2 means every other), from left to right
# "negative stride" = stride, but from right to left [1:10:-2]
l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print l[2:9:2]  # => [9, 25, 49, 81]


# 22. Omitting indices:
to_five = ['A', 'B', 'C', 'D', 'E']

print to_five[3:]  # start at index 3 and go to end
# prints ['D', 'E']

print to_five[:2]  # start at index 0 and go up to 2 (excl)
# prints ['A', 'B']

print to_five[::2]  # starts at 0 and goes to end by 2's
# print ['A', 'C', 'E']

garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = garbled[::-2]
print message # => I am the secret message!


# 23.
to_21 = [x for x in range(1, 22)]
odds = to_21[::2]
middle_third = to_21[7:14]


threes_and_fives = [x for x in range(1, 16) if (x % 3 == 0) or (x % 5 == 0)]
