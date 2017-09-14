zoo_animals = ["pangolin", "cassowary", "sloth", "penguin"];

suitcase = []
suitcase.append("sunglasses")

# Your code here!
suitcase.append("shirts")
suitcase.append("pants")
suitcase.append("shoes")

list_length = len(suitcase) # Set this to the length of suitcase

# v2.7
print "There are %d items in the suitcase." % (list_length)
print suitcase

# v3.x
print("There are {} items in the suitcase.".format(list_length))
print(suitcase)

# Use the index to select elements from a list:
suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]
first = suitcase[0:2]  # 1st and 2nd items (index 0 and 1)
middle = suitcase[2:4] # 3rd and 4th items (index 2 and 3)
last =  suitcase[4:]   # The last two items (index 4 and 5)

# Use the index to select characters from a string:
animals = "catdogfrog"
cat = animals[:3]  # The first three characters of animals
dog = animals[3:6]  # The fourth through sixth characters
frog = animals[6:]  # From the seventh character to the end

# Finding an index and inserting a new item into a list
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")
animals.insert(duck_index, "cobra")
print animals


# Looping through lists:
my_list = [1,9,3,8,5,7]

for number in my_list:
    print number * 2      # v3.x  print(number * 2)

# Looping example
def fizz_count(x):
  count = 0
  for item in x:
    if item == 'fizz':
      count += 1
  return count

li = ['fizz', 'fizz', 'buzz', 'zero', 'fizz']
print fizz_count(li)  # => 3


# Sorting a list (.sort MODIFIES original list!)
start_list = [5, 3, 1, 2, 4]
square_list = []

# Your code here!
for number in start_list:
  square_list.append(number ** 2)

print square_list   # => [25, 9, 1, 4, 16]
square_list.sort()
print square_list   # => [1, 4, 9, 16, 25]

# Removing items from a list
backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']
backpack.remove('dagger')


############## DICTIONARIES ##############
# Accessing the values in a dict (dictionary):
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print residents['Puffin']           # => 104
print residents['Sloth']            # => 105
print residents['Burmese Python']   # => 106


# Deleting and reassigning items in a dictionary. Note multi-line notation for dictionary with many items.
zoo_animals = {
  'Unicorn' : 'Cotton Candy House',
  'Sloth' : 'Rainforest Exhibit',
  'Bengal Tiger' : 'Jungle House',
  'Atlantic Puffin' : 'Arctic Exhibit',
  'Rockhopper Penguin' : 'Arctic Exhibit'
}

del zoo_animals['Unicorn']
del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']
zoo_animals['Rockhopper Penguin'] = 'Antarctic Exhibit'

print zoo_animals


### Combining everything ###
inventory = {
  'gold' : 500,
  'pouch' : ['flint', 'twine', 'gemstone'],
  'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

inventory['pouch'].sort()

inventory['pocket'] = ['seashell', 'strange berry', 'lint']

inventory['backpack'].sort()
inventory['backpack'].remove('dagger')

inventory['gold'] += 50

print inventory  # =>
# {
#       'pocket': ['seashell', 'strange berry', 'lint'],
#     'backpack': ['bedroll', 'bread loaf', 'xylophone'],
#        'pouch': ['flint', 'gemstone', 'twine'],
#   'burlap bag': ['apple', 'small ruby', 'three-toed sloth'],
#         'gold': 550
# }


# Using two dictionaries with the same keys:
prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}

stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pear": 15
}

for key in prices:
  print key
  print "price: {}".format(prices[key])
  print "stock: {}".format(stock[key])

total = 0

for key in prices:
  item_total = prices[key] * stock[key]
  print item_total
  total += item_total

print total


shopping_list = ["banana", "orange", "apple"]
def compute_bill(food):
    total = 0
    for item in food:
        if stock[item] > 0:
            total += prices[item] # adds price if in stock
            stock[item] -= 1      # decrements stock by 1
    return total

print compute_bill(shopping_list)


# Student Grades Example:
lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

def average(numbers):
    total = sum(numbers)
    return total / float(len(numbers))

def get_average(student):
    homework = average(student['homework'])
    quizzes = average(student['quizzes'])
    tests = average(student['tests'])
    return homework * .10 + quizzes * .30 + tests * .60

def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print get_letter_grade(get_average(lloyd))

def get_class_average(class_list):
    results = []
    for student in class_list:
        results.append(get_average(student))
    return average(results)

print get_class_average([lloyd, alice, tyler])
