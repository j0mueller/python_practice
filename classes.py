# Syntax:
# keyword 'class'
# class Name (capitalized)
# class from which new class INHERITS (in parens)
# colon

# note: the pass keyword doesn't do anything but is useful as a placeholder

class Square(object):
  def __init__(self):
    self.sides = 4

my_shape = Square()
print my_shape.sides

# ----------------------------------------------------
class Animal(object):
  """Makes cute animals."""
  # For initializing our instance objects
  def __init__(self, name, age, is_hungry):
    self.name = name
    self.age = age
    self.is_hungry = is_hungry

zebra = Animal("Jeffrey", 2, True)
giraffe = Animal("Bruce", 1, False)
panda = Animal("Chad", 7, True)

print zebra.name, zebra.age, zebra.is_hungry  # => Jeffrey 2 True
print giraffe.name, giraffe.age, giraffe.is_hungry  # => Bruce 1 False
print panda.name, panda.age, panda.is_hungry # => Chad 7 True

# -----------------------------------------------------
class Fruit(object):
    """A class that makes various tasty fruits."""
    def __init__(self, name, color, flavor, poisonous):
        self.name = name
        self.color = color
        self.flavor = flavor
        self.poisonous = poisonous

    def description(self):
        print "I'm a {} {} and I taste {}.".format(self.color, self.name, self.flavor)

    def is_edible(self):
        if not self.poisonous:
            print "Yep! I'm edible."
        else:
            print "Don't eat me! I am super poisonous."

lemon = Fruit("lemon", "yellow", "sour", False)

lemon.description()
lemon.is_edible()

# -----------------------------------------------------
# SCOPE
# global variables
# member variables
# instance variables
class Animal(object):
    """Makes cute animals."""
    is_alive = True         # <= this is a member variable
    health = "good"
    def __init__(self, name, age):
        self.name = name    # <= this is an instance variable
        self.age = age
  # Add your method here!
    def description(self):
        print self.name
        print self.age

hippo = Animal("Alice", 5)
hippo.description()         # <= function calls end in ()
hippo.health                # <= attribute calls don't

# ------------------------------------------------------------

class ShoppingCart(object):
    """Creates shopping cart objects
    for users of our fine website."""
    items_in_cart = {}
    def __init__(self, customer_name):
        self.customer_name = customer_name

    def add_item(self, product, price):
        """Add product to the cart."""
        if not product in self.items_in_cart:
            self.items_in_cart[product] = price
            print product + " added."
        else:
            print product + " is already in the cart."

    def remove_item(self, product):
        """Remove product from the cart."""
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print product + " removed."
        else:
            print product + " is not in the cart."

my_cart = ShoppingCart("Jane")
my_cart.add_item("apples", 1.25)    # => apples added.

# ------------------------------------------------------------
# INHERITANCE

#class DerivedClass(BaseClass):
  # code goes here

class Shape(object):
  """Makes shapes!"""
  def __init__(self, number_of_sides):
    self.number_of_sides = number_of_sides

# Inherit from Shape class:
class Triangle(Shape):
  def __init__(self, side1, side2, side3):
    self.side1 = side1
    self.side2 = side2
    self.side3 = side3

# Override inherited methods or attributes
class Employee(object):
  """Models real-life employees!"""
  def __init__(self, employee_name):
    self.employee_name = employee_name

  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 20.00

# Inherit from Employee but override calculate_wage
# Use 'super' to directly access the attributes or methods of a superclass
# class Derived(Base):
#   def m(self):
#     return super(Derived, self).m()
# Where m() is a method from the base class.
class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00

    def full_time_wage(self, hours):
        return super(PartTimeEmployee, self).calculate_wage(hours)

milton = PartTimeEmployee("Milton")

print milton.full_time_wage(10)

# -------------------------------------------------------
class Triangle(object):
    number_of_sides = 3
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    def check_angles(self):
        if (self.angle1 + self.angle2 + self.angle3) == 180:
            return True
        else:
            return False

my_triangle = Triangle(90, 30, 60)
print my_triangle.number_of_sides   # => 3
print my_triangle.check_angles()    # => True

class Equilateral(Triangle):
  angle = 60
  def __init__(self):
    self.angle1 = self.angle
    self.angle2 = self.angle
    self.angle3 = self.angle

# ----------------------------------------------------------
class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg

    def display_car(self):
        print "This is a {} {} with {} MPG.".format(self.color, self.model, self.mpg)

    def drive_car(self):
        self.condition = "used"


my_car = Car("DeLorean", "silver", 88)
print my_car.model, my_car.color, my_car.mpg
print my_car.condition      # => "new"
my_car.drive_car()
print my_car.condition      # => "used"

class ElectricCar(Car):
  def __init__(self, model, color, mpg, battery_type):
    self.model = model
    self.color = color
    self.mpg   = mpg
    self.battery_type = battery_type

my_car = ElectricCar("DeLorean", "silver", 88, "molten salt")

# ----------------------------------------------------------
# Built-in __repr__() method  = "representation"

class Point3D(object):
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z

  def __repr__(self):
    return "({}, {}, {})".format(self.x, self.y, self.z)

my_point = Point3D(1, 2, 3)

print my_point
