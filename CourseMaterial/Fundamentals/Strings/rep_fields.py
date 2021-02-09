# Tedious to coerce int to a string
age = 24
print("My age is " + str(age) + " ears!")

# .format method was introduced to improve this problem
print("My age is {0} years".format(age))

# Better to split lines, easier to read, 8 total replacements
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, {7}"
      .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))

# Replacement fields do not have to be in order
print("Jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2}, Jun: {1}, Jul: {2}, Sep: {1}, Oct: {2}, Nov: {1}, Dec: {2}"
      .format(28, 30, 31))

# """ makes you able to allows for better formatting to create a new line for each month
print("""Jan: {2}
Feb: {0}
Mar: {2}
Apr: {1}
May: {2}
Jun: {1}
Jul: {2}
Sep: {1}
Oct: {2}
Nov: {1}
Dec: {2}""".format(28, 30, 31))
