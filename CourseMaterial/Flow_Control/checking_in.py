parrot = "Norwegian Blue"
letter = input("Enter a character: ")

if letter in parrot:
	print("{} is in {}".format(letter, parrot))
else:
	print("I do not need that letter")

activity = input("What would you like to do today? ")
if "movies" not in activity.casefold():
	print("But I want to go the cinema")
