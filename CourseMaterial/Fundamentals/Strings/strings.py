# Strings can be surround by single or double quotes.
# NOTE: To make things simpler, start and end with the same quotations.
print("Yay, I am learning strings in Python.")
print('Works the same with single quotes')
print("Python's strings are very simple to use.")
print('You can do "quotes" within strings.')

# Concatenation is when you add multiple strings together
# Store strings into variables so that concatenation makes sense
greeting = "Hello"
name = "Moe"
print(greeting + ' ' + name) # Hello Moe

# Example with input from the user by assigning the variable to input function, and then printing after.
userInput = input("Please enter your name ")
print(greeting + ' ' + userInput) # Hello [Word typed in from user]

