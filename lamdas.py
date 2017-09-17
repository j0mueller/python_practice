#functional programming - allowed to pass functions around just as if they were variables or values

# Anonymous Function:
lambda x: x % 3 == 0

# Is the same as:
def by_three(x):
  return x % 3 == 0

# Lambdas are useful when you need a quick function to do some work for you.
# If you plan on creating a function you'll use over and over, you're better off using def and giving that function a name.

# When we pass the lambda to filter, filter uses the lambda to determine what to filter, and the second argument (my_list, which is just the numbers 0 – 15) is the list it does the filtering on.
my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)
# => [0, 3, 6, 9, 12, 15]

languages = ["HTML", "JavaScript", "Python", "Ruby"]
print filter(lambda x: x == "Python", languages)

cubes = [x ** 3 for x in range(1, 11)]
filter(lambda x: x % 3 == 0, cubes)

squares = [x ** 2 for x in range(1, 11)]
print filter(lambda x: x in range(30, 71), squares)


#######
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"

print filter(lambda x: x != "X", garbled)
