# Strings are sequence type so you can index through each character
parrot = "Norwegian Blue"
print(parrot)   # Norwegian Blue
print(parrot[3])    # w bc index starts at 0
# Add code to program to print out we win
# Each char on new line and get from string using indexing
print(parrot[4] )
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

print('='*15)

#########################   INDEXING NEGATIVELY THROUGH STRING  ##########################
# You can go index through strings using negative index values as well
print(parrot[-1])   # e at the last index
print(parrot[-14])  # N at the first index

# Try printing we win now using negative indexing
print('='*15)
print(parrot[-11])
print(parrot[-1])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

# Note: The negative index of a character can be computed by taking the positive index
# numbers from the first example and subtracting the string length from it.
# i.e. parrot[3] = 'w'  parrot[3 - 14] AKA parrot[-11]
