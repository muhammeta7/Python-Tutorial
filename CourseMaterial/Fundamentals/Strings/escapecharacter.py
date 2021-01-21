# Escape character or Backslash character is used to escape the character that follows it.
# Good for formatting and IDES generally indicate these characters by changing color.

# \n is new line
splitString = "1. This string has been \n2. split into three \n3. separate lines\n\n"
print(splitString)

# \t tab
tabbedString = "1a\t2b\t3c\t4d\t5e\t\n\n"
print(tabbedString)

#  Must escape the same type of quotes that string begins with

# Single Quote
print('The NE coach said "We don\'t have the right QB".')
# Double Quote
print("The NE coach said \"We don't have the right QB\".")
# Triple Quote
print("""The NE coach said "Cam's not that good of a QB". """)

# To avoid issues reading with \n in order to use triple quotes
splitString2 = """This string has been
split into
three lines"""
print(splitString2)

# \ alone will automatically ignore the escape character
splitString3 = """This string has been \
split into \
three lines"""
print(splitString2)
