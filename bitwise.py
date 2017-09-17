# Bitwise operations are operations that directly manipulate bits.

# 6 basic bitwise operations.
print 5 >> 4  # Right Shift => 0
print 5 << 1  # Left Shift  => 10
print 8 & 5   # Bitwise AND => 0
print 9 | 4   # Bitwise OR  => 13
print 12 ^ 42 # Bitwise XOR => 38
print ~88     # Bitwise NOT => -89



print 0b1,    #1
print 0b10,   #2
print 0b11,   #3
print 0b100,  #4
print 0b101,  #5
print 0b110,  #6
print 0b111   #7
print "******"
print 0b1 + 0b11
print 0b11 * 0b11
# =>
# 1 2 3 4 5 6 7
# ******
# 4
# 9

one = 0b1
two = 0b10
three = 0b11
four = 0b100
five = 0b101
six = 0b110
seven = 0b111
eight = 0b1000
nine = 0b1001
ten = 0b1010
eleven = 0b1011
twelve = 0b1100


# bin() takes an integer as input and returns the binary representation of that integer in a string. (Keep in mind that after using the bin function, you can no longer operate on the value like a number.)
# You can also represent numbers in base 8 and base 16 using the oct() and hex() functions.

print bin(2) # => 0b10  (note: this is a string)


# Use int() function to feed it a number its base and have it converted to base 10
print int("1",2)            # => 1
print int("10",2)           # => 2
print int("111",2)          # => 7
print int("0b100",2)        # => 4
print int(bin(5),2)         # => 5
print int("11001001", 2)    # => 201


# Shift bits left or right to designated spot (always a positive integer)
# Left Bit Shift (<<)
0b000001 << 2 == 0b000100 (1 << 2 = 4)
0b000101 << 3 == 0b101000 (5 << 3 = 40)

# Right Bit Shift (>>)
0b0010100 >> 3 == 0b000010 (20 >> 3 = 2)
0b0000010 >> 2 == 0b000000 (2 >> 2 = 0)

# Bitwise AND: &  -- Results are always <= smaller of 2 inputs
# The bitwise AND (&) operator compares two numbers on a bit level and returns a number where the bits of that number are turned on if the corresponding bits of both numbers are 1
# Example:
#      a:   00101010   42
#      b:   00001111   15
# ===================
 # a & b:   00001010   10

# For every given bit in a and b:
# 0 & 0 = 0
# 0 & 1 = 0
# 1 & 0 = 0
# 1 & 1 = 1

0b111 (7) & 0b1010 (10) = 0b10  # => equals 2
print bin(0b1110 & 0b101) # => 0b100

# Bitwise OR: |  -- Results are always >= larger of 2 inputs
# The bitwise OR (|) operator compares two numbers on a bit level and returns a number where the bits of that number are turned on if either of the corresponding bits of either number are 1.
# Exampe:
#     a:  00101010  42
#     b:  00001111  15
# ================
# a | b:  00101111  47

# For every given bit in a and b:
# 0 | 0 = 0
# 0 | 1 = 1
# 1 | 0 = 1
# 1 | 1 = 1

110 (6) | 1010 (10) = 1110 (14)
print bin(0b1110 | 0b101)

# The XOR (Exclusive OR): ^  (returns if either but not both)
#     a:  00101010   42
#     b:  00001111   15
# ================
# a ^ b:  00100101   37

# 0 ^ 0 = 0
# 0 ^ 1 = 1
# 1 ^ 0 = 1
# 1 ^ 1 = 0

111 (7) ^ 1010 (10) = 1101 (13)
print bin(0b1110 ^ 0b101)


# Bitwise NOT: ~
# Flips all the bits in a single number
# Equivalent to adding one to the number and then making it negative
print ~1    # => -2
print ~2    # => -3
print ~3    # => -4
print ~42   # => -43
print ~123  # => -124


# A bit mask is just a variable that aids you with bitwise operations. A bit mask can help you turn specific bits on, turn others off, or just collect data from an integer about which bits are on or off.
# How does it take in an integer and compare with bit?
def check_bit4(input):
  mask = 0b1000
  desired = input & mask
  if desired > 0:
    return "on"
  else:
    return "off"

print check_bit4(20)


# Using the bitwise | operator will turn a corresponding bit on if it is off and leave it on if it is already on.
a = 0b110 # 6
mask = 0b1 # 1
desired =  a | mask # 0b111, or 7

a = 0b10111011
mask = 0b0100
desired = a | mask
print bin(desired)  # directed to print as string

# Using XOR ^ to flip all bits
a = 0b110 # 6
mask = 0b111 # 7
desired =  a ^ mask # 0b1

a = 0b11101110
mask = 0b11111111
desired = a ^ mask
print bin(desired) # => 0b10001

# to turn on the 10th bit from the right of the integer a.
a = 0b101
# Tenth bit mask
mask = (0b1 << 9)  # One less than ten
desired = a ^ mask


# Flip the nth bit (with the ones bit being the first bit) and store it in result
def flip_bit(number, n):
    bit_to_flip = 0b1 << (n -1)
    result = number ^ bit_to_flip
    return bin(result)
