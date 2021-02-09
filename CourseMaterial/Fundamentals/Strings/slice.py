# Strings are sequence type so you can index through each character
# [ ] used for indexing
parrot = "Norwegian Blue"
print(parrot)  # Norwegian Blue
print(parrot[3])  # w bc index starts at 0
# Add code to program to print out we win
# Each char on new line and get from string using indexing
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

print('=' * 15)
#########################   INDEXING NEGATIVELY THROUGH STRING  ##########################
# You can go index through strings using negative index values as well
print(parrot[-1])  # e at the last index
print(parrot[-14])  # N at the first index

print('=' * 15)
# Try printing we win now using negative indexing
print(parrot[-11])
print(parrot[-1])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

print('=' * 15)
# Note: The negative index of a character can be computed by taking the positive index
# numbers from the first example and subtracting the string length from it.
# i.e. parrot[3] = 'w'  parrot[3 - 14] AKA parrot[-11]

#########################   SLICING STRING  ##########################
# [ ]  used for slicing strings as well
# The first number is the start and the second value is up to and not including the end, similar to ranges
# parrot = "Norwegian Blue"
print(parrot[3:5])  # we
# starts at third index of string w and ends at the 4th index of start, the fifth index being excluded in result
print(parrot[0:6])  # Norweg
print(parrot[:6])  # Norweg same as above because no value on left side of : indicates indexing from start of string
print(parrot[0:9])  # Norwegian
print(parrot[:9])  # Norwegian
print(parrot[10:14])  # Blue
print(parrot[10:])  # Blue same as above because no value on right side of : indicates indexing to end of string
print('=' * 15)
print(parrot[6:] + parrot[6:])  # Norwegian Blue prints complete word because everything is included
print(parrot[:])  # Norwegian Blue   --> Not generally recommended but works well for lists to make copies
print('=' * 15)
# NEGATIVE SLICING
print(parrot[-4:2])  # Can't go backwords from starting position
print(parrot[-4:-2])  # Bl
print(parrot[-4:12])  # Bl
print('=' * 15)
# Do negative slicing versions of previous slicing example.
print(parrot[-14:-8])  # Norweg
print(parrot[-14:-5])  # Norwegian
print(parrot[-4:14])  # Blue

print('=' * 15)
#########################   USING STEPS IN SLICES  ##########################
print(parrot[0:6:2])  # Nre   --> start at 0 index and increment by 2 up to and excluding the 6th index
print(parrot[0:6:3])  # Nw    --> start at 0 index and increment by 3 up to and excluding the 6th index

number = '9,455,666,777,888,999'
print(number[1::4])  # ,,,,,,    --> starts at position 1 and slices every 4th character
# Good to use for separator data
number1 = '9,455;666 777,888;999'
separators = number1[1::4]
print(separators)
values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])
print('=' * 15)
# STEPPING BACKWARDS
letters = "abcdefghijklmnopqrstuvwxyz"
backwards = letters[25:0:-1]
print(backwards)    # zyxwvutsrqponmlkjihgfedcb
# NOTE does not include a bc stop value is not inclusive
print('=' * 15)
includes_a = letters[25::-1]    # zyxwvutsrqponmlkjihgfedcba
print(includes_a)
includes_a = letters[::-1]  # zyxwvutsrqponmlkjihgfedcba
print(includes_a)

print('=' * 15)
# Create slice to produce the following strings
# qpo
print(letters[16:13:-1])
# edbca
print(letters[4::-1])
# last 8 characters in reverse order
print(letters[:-9:-1])


# Idioms
print(letters[-4:]) # wzyz
print(letters[-1:]) # z
print(letters[:1]) # a --> useful for getting first index for empty string w/o code crushing


# Sequence
# 5 types include:
# String
# List
# tuple
# range
# byte & bytearray

# Defined as ordered set of items so you can index individual items in the sequence.
computer_parts = ['computer', 'monitor', 'keyboard', 'mouse']
print(computer_parts[1])    # monitor
# Since strings are also a sequence you can index into the string monitor as well sequence[][]
print(computer_parts[1][0]) # m
print(computer_parts[1][4]) # t

# Everything that you can do with strings you can do with other sequence types.
# NOTE: not all sequence types can be concatenated or multiplied. Range can not be concatenated.


