age = int(input("How old are you"))

if 16 <= age <= 65: # chained comparison is equivalent of if age >= 16 and age <= 65
	print("Have a good day at work")

# Boolean True or False
day = "Monday"
temperature = 90
raining = True

if day == "Saturday" and temperature > 75 and not raining:
	print("Go swimming")
else:
	print("Learn Python")

# When using chained conditionals with or and and, the and will take precedent.
# Use parenthesis to avoid bugs when chaining boolean operations
if 0:   # Will never reach statement
	print("True")
else:
	print("False")

name = input("Please enter your name: ")
if name != "":
	print("Hello, {}".format(name))
else:
	print("Are you a man with no name")