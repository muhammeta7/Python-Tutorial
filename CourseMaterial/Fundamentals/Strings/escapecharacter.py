splitString = "1. This string has been \n2. split into three \n3. separate lines\n\n"
print(splitString)

tabbedString = "1a\t2b\t3c\t4d\t5e\t\n\n"
print(tabbedString)

# Single Quote
print('The NE coach said "We don\'t have the right QB".')
# Double Quote
print("The NE coach said \"We don't have the right QB\".")
# Triple Quote
print("""The NE coach said "Cam's not that good of a QB". """)

splitString2 = """This string has been
split into
three lines"""
print(splitString2)


splitString3 = """This string has been \
split into \
three lines"""
print(splitString3)

# Additional info on escape characters
print(r"C:\Users\tom\notes.py")  # r in front turns string into regular expression
print("C:\\Users\\tom\\notes.py")  # more preferable
