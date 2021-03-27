parrot = "Norwegian Blue"

for character in parrot:
	print(character)

number = "9,223;372:036 854,775;807"
separators = ""
print(separators)

for char in number:
	if not char.isnumeric():
		separators = separators + char

print(separators)

user_numbers = input("Please enter a series of numbers, using any separators")
user_separators = ""
for char in user_numbers:
	if not char.isnumeric():
		user_separators = user_separators + char
values = "".join(char if char not in user_separators else " " for char in user_numbers).split()
print(sum([int(val) for val in values]))

# Extracting capitals
quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""
capitals = ""
for char in quote:
	if char.isupper():
		capitals = capitals + char
print(capitals)