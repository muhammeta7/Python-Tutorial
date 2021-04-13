for i in range(1, 13):
	print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))

print()
# {0:2} field width separated from index has number of characters it takes place of

"""
{0:<2}  --> left aligned
{0:>2}  -> left aligned
{0:^2}  -> left aligned
"""
for i in range(1, 13):
	print("No. {0:2} squared is {1:<3} and cubed is {2:<4}".format(i, i ** 2, i ** 3))

print()
# for floats
# precision is more important than field width
# Max precision is 51-53
print("Pi is approximately {0:12}".format(22 / 7))    # 15 values
print("Pi is approximately {0:12f}".format(22 / 7))   # 6 digits
print("Pi is approximately {0:12.50f}".format(22 / 7))    # 50
print("Pi is approximately {0:52.50f}".format(22 / 7))    # 52 wont truncate number
print("Pi is approximately {0:62.50f}".format(22 / 7))    # 62 different field widths
print("Pi is approximately {0:<72.50f}".format(22 / 7))   # 72 digits and left aligned

for i in range(1, 13):
	print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))

"""
No field numbers 
No numbers then you can only use number once
"""