string1 = "he's "
string2 = "thinking "
string3 = "about"
string4 = "something"
string5 = "stupid"

print(string1, string2, string3, string4, string5)

# Strings can also be multiplied
print("^_^ " * 5)  # ^_^ ^_^ ^_^ ^_^ ^_^
print("Hello " * (5 + 2))  # Hello Hello Hello Hello Hello Hello Hello
print("Hello " * 5 + "2")  # Hello Hello Hello Hello Hello 2

# To check if string is substring of another string you can use the keyword in.
today = "Tuesday"
print("day" in today)  # True
print("Tues" in today)  # True
print("Mon" in today)  # False
print("nope" in today)  # False
