# Single and Double Quotes
print("Yay, I am learning strings in Python.")
print('Works the same with single quotes')
print("Python's strings are very simple to use.")
print('You can do "quotes" within strings.')

# Concatenation
greeting = "Hello"
name = "Moe"
print(greeting + ' ' + name)
# Hello Moe

# When using the + operator where one of the operands is a string, both operands must be a string.
# You can convert a numeric value to a string with the built-in function str().
str(3) + '3'    # '33
print('3' + '3')    # '33'

#  User Input
userInput = input("Please enter your name ")
print(greeting + ' ' + userInput)
# Hello [Word typed in from user]
# Start and end with exact same type of quotation.
# You can us concatenation to add multiple strings together.
# Storing strings into variables is a good way to reference them for later use.
# Assigning a variable to the input function allows you to store user input.

# ==================================================================================
age = 24
print(age)

#
print(type(greeting))
print(type(age))

age = "2 years"
print(age)
print(type(age))

# Example will create an TypeError bc Python can not concatenate a string to an int
# Adding strings to strings works and ints to ints
print(name + ' is ' + age + ' years old')
