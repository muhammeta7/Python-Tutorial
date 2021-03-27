name = input("Please enter your name: ")
age = int(input("How old are you? "))

if 18 <= age < 30:
	print("Welcome club 18-30 vacation, {0}".format(name))
else:
	print("I am sorry you are not coll enough to join us")
